"""Check semantic PDF invariants, without a cross-version pixel baseline."""
import argparse
import json
import os
from pathlib import Path

import pymupdf


def require(condition, message):
    if not condition:
        raise ValueError(message)


def inspect(root, name):
    path = root / name / (name + '.pdf')
    require(path.is_file(), 'PDF missing')
    with pymupdf.open(path) as doc:
        require(len(doc) > 0, 'Empty PDF')
        text = '\n'.join(p.get_text() for p in doc)
        require(len(text.strip()) > (5 if name == 'version-probe' else 20), 'PDF text missing')
        if name.startswith('frontmatter-caption'):
            require(len(doc) == 1 and 'OMITTED-' not in text, 'Frontmatter was not omitted')
            require('-1-' in ''.join(text.split()), 'Body page number is not 1')
            spans = [s for b in doc[0].get_text('dict')['blocks'] if 'lines' in b
                     for line in b['lines'] for s in line['spans']]
            for marker, size in [('中文图题', 10.5), ('中文表题', 10.5),
                                 ('English figure caption', 10.5), ('English table caption', 10.5),
                                 ('表内五号', 10.5), ('Table text', 10.5), ('正文应为', 12)]:
                found = [s for s in spans if marker in s['text']]
                require(found and all(abs(s['size'] - size) < .05 for s in found),
                        f'Wrong or missing font size: {marker}')
        elif name == 'webpage-date':
            require(text.count('2024') == 1 and text.count('2023') == 1, 'Publication year count')
            require(text.count('2026-09-09') == 2, 'Access date count')
        elif name == 'signature-layout':
            pages = [p for p in doc if '独创性声明' in p.get_text()]
            require(len(pages) == 3, 'Expected three declaration pages')
            rows = [[(s['text'], tuple(round(v, 3) for v in s['bbox']))
                     for b in p.get_text('dict')['blocks'] if 'lines' in b
                     for line in b['lines'] for s in line['spans'] if s['bbox'][1] < 780]
                    for p in pages]
            require(len(rows[0]) > 20 and rows[0] == rows[1] == rows[2], 'Signature changes text coordinates')
            require(not pages[0].get_images() and pages[1].get_images() and pages[2].get_images(),
                    'Signature images missing or unexpectedly present')
        elif name in ('main', 'main-academic'):
            require('独创性声明' in text and 'Abstract' in text, 'Sample frontmatter missing')
        return f'{len(doc)} pages; PDF checks passed'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, required=True)
    args = parser.parse_args()
    manifest = Path(__file__).resolve().parents[1] / 'config/cases.json'
    names = [case['name'] for case in json.loads(manifest.read_text(encoding='utf-8'))]
    results = {}
    status_file = args.root / 'results.tsv'
    statuses = dict(line.split('\t') for line in status_file.read_text().splitlines()[1:]) if status_file.exists() else {}
    for name in names:
        try:
            require(statuses.get(name) == '0', f'Compile failed or not run (exit={statuses.get(name)})')
            detail = inspect(args.root, name)
            results[name] = {'passed': True, 'detail': detail}
        except Exception as error:
            results[name] = {'passed': False, 'detail': str(error)}
    args.root.mkdir(parents=True, exist_ok=True)
    (args.root / 'checks.json').write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding='utf-8')
    lines = ['# Template regression checks', '', '| Case | Status | Detail |', '|---|---|---|']
    for name, result in results.items():
        detail = result['detail'].replace('|', '/').replace('\n', ' ')
        lines.append(f"| {name} | {'PASS' if result['passed'] else 'FAIL'} | {detail} |")
    lines += ['', 'This checks compilation and PDF invariants. Visual baselines are checked separately.']
    summary = '\n'.join(lines) + '\n'
    (args.root / 'summary.md').write_text(summary, encoding='utf-8')
    if os.environ.get('GITHUB_STEP_SUMMARY'):
        with open(os.environ['GITHUB_STEP_SUMMARY'], 'a', encoding='utf-8') as f:
            f.write(summary)
    print(summary)
    return 0 if all(r['passed'] for r in results.values()) else 1


if __name__ == '__main__':
    raise SystemExit(main())
