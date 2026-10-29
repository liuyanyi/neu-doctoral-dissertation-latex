"""Run the shared template regression suite from any working directory."""
import argparse
import json
import os
from pathlib import Path
import re
import subprocess
import sys

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / 'tests/tools'))
from make_academic_entry import disable_professional_degree


def prepare(output):
    cases = json.loads((REPO / 'tests/config/cases.json').read_text(encoding='utf-8'))
    names = [case['name'] for case in cases]
    if len(names) != len(set(names)) or any(not re.fullmatch(r'[a-z0-9-]+', n) for n in names):
        raise ValueError('Case names must be unique simple directory names')
    output.mkdir(parents=True, exist_ok=True)
    text, changed = disable_professional_degree((REPO / 'main.tex').read_text(encoding='utf-8'))
    if not changed:
        raise ValueError('Professional-degree option missing from main.tex')
    generated = output / 'generated/main-academic.tex'
    generated.parent.mkdir(parents=True, exist_ok=True)
    generated.write_text(text, encoding='utf-8')
    entries = [(c['name'], c['source'].replace('{output}', output.as_posix())) for c in cases]
    for _, source in entries:
        if not Path(source).is_file():
            raise FileNotFoundError(source)
    (output / 'cases.tsv').write_text(''.join(f'{n}\t{s}\n' for n, s in entries), encoding='utf-8')
    return entries


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('tests/build/regression'))
    parser.add_argument('--prepare-only', action='store_true', help='Prepare the shared case list for container CI')
    args = parser.parse_args()
    # All repository paths (including a relative --output) are rooted here.
    os.chdir(REPO)
    entries = prepare(args.output)
    if args.prepare_only:
        print(f'Prepared {len(entries)} cases in {args.output}')
        return 0
    with (args.output / 'environment.txt').open('w', encoding='utf-8') as stream:
        subprocess.run(['xelatex', '--version'], stdout=stream, stderr=subprocess.STDOUT, check=True)
    unresolved = re.compile(r'There were undefined (?:references|citations)|Reference .* undefined|Citation .* undefined', re.I)
    with (args.output / 'results.tsv').open('w', encoding='utf-8') as statuses:
        statuses.write('case\texit_code\n')
        statuses.flush()
        for name, source in entries:
            target = args.output / name
            target.mkdir(parents=True, exist_ok=True)
            with (target / 'console.txt').open('w', encoding='utf-8') as console:
                result = subprocess.run(['latexmk', '-xelatex', '-interaction=nonstopmode', '-halt-on-error',
                                         f'-outdir={target.as_posix()}', source], stdout=console, stderr=subprocess.STDOUT)
            code = result.returncode
            log = target / f'{name}.log'
            if code == 0 and (not log.is_file() or unresolved.search(log.read_text(encoding='utf-8', errors='replace'))):
                code = 1
                with (target / 'console.txt').open('a', encoding='utf-8') as console:
                    console.write('\nMissing log or unresolved references/citations.\n')
            statuses.write(f'{name}\t{code}\n')
            statuses.flush()
            print(f'{name}: exit {code}', flush=True)
            if code:
                print('\n'.join((target / 'console.txt').read_text(encoding='utf-8', errors='replace').splitlines()[-30:]), flush=True)
    return subprocess.call([sys.executable, 'tests/tools/check_compatibility_pdfs.py', '--root', str(args.output)])


if __name__ == '__main__':
    raise SystemExit(main())
