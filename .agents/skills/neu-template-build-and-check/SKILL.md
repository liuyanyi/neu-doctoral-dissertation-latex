---
name: neu-template-build-and-check
description: 东北大学博士学位论文 LaTeX 模板编译、清理、排错和提交前自查。用于普通模板使用者运行 latexmk -xelatex main.tex、latexmk -C，配置本地/Overleaf/VS Code 编译，诊断 PDF 未生成、Undefined control sequence、Missing file、图片找不到、参考文献不显示、引用 ??、目录未更新、字体 warning、Overfull/Underfull hbox，并检查盲审版和最终版提交前事项。
---

# NEU 模板编译与自查

## Purpose

帮助用户按模板推荐方式编译、清理辅助文件、定位常见错误，并在提交前完成面向模板使用的自查。

## When to use

- 需要本地、VS Code 或 Overleaf 编译模板。
- PDF 没生成、引用显示 `??`、参考文献不显示或图片找不到。
- 编译日志中出现 `Undefined control sequence`、`Missing file`、字体 warning、Overfull / Underfull hbox。
- 定稿或提交盲审 / 最终版前，需要做一次 clean build 和格式自查。

## Key files

- `README.md`：推荐编译命令和 Overleaf / VS Code 提示。
- `main.tex`：主入口，所有编译命令应指向它。
- `.latexmkrc`：项目 latexmk 配置，使用 XeLaTeX，自动调用 BibTeX，并定义清理扩展名。
- `.vscode/settings.json`：LaTeX Workshop 配方，包含智能增量编译和强制全量编译。
- `main.log`：LaTeX 编译日志，优先看第一个真正的 fatal error。
- `main.blg`：BibTeX 日志，参考文献问题优先查看。
- `references.bib`：文献条目来源。
- `Figures/`：图片路径和文件名检查位置。

## Rules

- 推荐编译命令以 README 为准：`latexmk -xelatex main.tex`。
- 清理辅助文件可用 `latexmk -C`，再运行一次完整编译。
- 本地编译优先使用 TeX Live 2023-2026 和 XeLaTeX。
- Overleaf 上必须选择 XeLaTeX；云上版本可能超时，必要时改用本地环境或 Overleaf 本地部署版本。
- VS Code 使用项目内置 LaTeX Workshop 配置；默认工具通过 `.latexmkrc` 使用 XeLaTeX。
- 编译失败时先看 `.log` 中第一个真正的 fatal error，不要先处理后续连锁错误。
- 引用、目录和文献问题优先尝试完整重编译；文献问题再看 `.blg` 和 `references.bib`。
- 图片问题优先检查路径、文件名大小写、扩展名和是否已上传到 Overleaf。
- 字体 warning 和 Overfull / Underfull hbox 先判断是否影响最终 PDF；不要为了消除 warning 大量手工调版。
- 不要修改 `neudissertation.cls` 来绕过普通使用错误。

## Workflow

1. 在项目根目录运行：

```bash
latexmk -xelatex main.tex
```

2. 如果出现旧辅助文件导致的异常，清理后重新编译：

```bash
latexmk -C
latexmk -xelatex main.tex
```

3. 如果使用 VS Code，安装 LaTeX Workshop 后打开 `main.tex`，选择项目内置的 “XeLaTeXmk（智能增量编译）”；遇到引用或目录异常时选择 “XeLaTeXmk（强制全量编译）”。
4. 如果使用 Overleaf，把项目完整上传，编译器选择 XeLaTeX，主文件选择 `main.tex`。
5. 编译失败时打开 `main.log`，从上往下找第一个以 `!` 开头并导致停止的错误，结合错误附近的文件名和行号处理。
6. 参考文献不显示或引用异常时查看 `main.blg`，检查 `references.bib` 是否有语法错误、key 是否匹配。
7. 修改文献、目录、章节标题、图表 label 后，运行完整编译直到 `??` 和未解析文献消失。
8. 提交前执行 clean build，并逐页检查 PDF。

## Examples

推荐本地编译：

```bash
latexmk -xelatex main.tex
```

清理后完整重编译：

```bash
latexmk -C
latexmk -xelatex main.tex
```

文献输出结构应保留在 `main.tex` 的 `\backmatter` 后：

```latex
\backmatter

\begin{referencescn}
  \bibliography{references}
\end{referencescn}
```

VS Code 配置中已有两个 LaTeX Workshop recipe：

```text
XeLaTeXmk（智能增量编译）
XeLaTeXmk（强制全量编译）
```

## Common mistakes

- PDF 没生成：先确认命令在项目根目录执行，目标是 `main.tex`，并查看 `main.log` 第一个 fatal error。
- `Undefined control sequence`：常见原因是命令拼错、用了旧命令、宏包未加载，或把模板命令写错；按 README 的公开命令核对。
- `Missing file` 或 `File ... not found`：检查 `\input{...}`、`\includegraphics{...}`、签名图片和 `.bib` 文件路径。
- 图片找不到：确认图片在 `Figures/`，文件名大小写、扩展名和路径完全一致；Overleaf 上还要确认文件已上传。
- 参考文献不显示：确认正文有 `\upcite{key}` / `\inlinecite{key}` 或文末有需要的 `\nocite{key}`，并确认 `references.bib` 中存在对应 key。
- 引用显示 `??`：通常需要再次完整编译；若仍未解决，检查 label 是否存在、是否重名、是否拼写一致。
- 目录没更新：重新运行 `latexmk -xelatex main.tex`，必要时 `latexmk -C` 后再编译。
- 字体 warning：先确认 PDF 字体和中文显示是否正常；若只是不影响输出的 warning，不要急于改模板类文件。
- Overfull / Underfull hbox：先定位对应页和行，检查长英文、长 URL、过宽表格或图片；必要时局部换行、缩小表格或调整图片宽度。

提交前自查：

- clean 后能用 `latexmk -xelatex main.tex` 完整编译。
- PDF 中没有 `??`、`[?]` 或未解析引用。
- `main.blg` 中没有未找到文献 key 的错误。
- 封面模式正确：盲审版 / 非盲审版、学术学位 / 专业学位、最终版封面开关符合提交要求。
- 盲审版没有暴露作者、导师、课题组、项目、成果归属、签名或可识别文件名。
- 最终版封面、声明、签名、日期、在线公开时间正确。
- 图表清晰，图题在图下方，表题在表上方，图表和公式都在正文中被引用。
- 参考文献条目完整，正文引用和文末列表一致。
- 没有残留 `chapter0-guide` 示例内容、示例文献、TODO、占位符或无关测试文字。
