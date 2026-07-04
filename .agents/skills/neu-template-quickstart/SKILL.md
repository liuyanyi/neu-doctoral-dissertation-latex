---
name: neu-template-quickstart
description: 东北大学博士学位论文 LaTeX 模板快速开始。用于普通模板使用者第一次拿到仓库后，了解 main.tex 主入口、摘要文件、章节文件、references.bib、Figures 目录用途，判断应编辑和不应编辑的文件，完成 XeLaTeX/latexmk 最短编译，删除示例内容，新增章节并在 main.tex 中引入，以及在本地、Overleaf、VS Code 中开始使用模板。
---

# NEU 模板快速开始

## Purpose

帮助第一次使用东北大学博士学位论文 LaTeX 模板的用户认识项目结构、找到主入口、完成最短编译，并把示例内容替换成自己的论文内容。

## When to use

- 刚下载或解压模板，不知道从哪个文件开始。
- 需要判断哪些文件应当编辑，哪些文件一般不要改。
- 需要新增章节、删除示例章节或迁移到 Overleaf / VS Code。
- 需要快速确认本地是否能编译出 `main.pdf`。

## Key files

- `main.tex`：论文主入口，设置文档类、论文元数据、前置页、章节顺序、参考文献和后置内容。
- `abstract-cn.tex`：中文摘要正文和 `\cnkeywords{...}`。
- `abstract-en.tex`：英文摘要正文和 `\enkeywords{...}`。
- `chapter0-guide.tex`：模板集中示例章节，可先保留作排版对照，定稿前从 `main.tex` 删除或注释。
- `chapter1.tex`、`chapter2.tex` 等：正文各章文件，通常每章单独一个 `.tex`。
- `references.bib`：BibTeX 参考文献数据库。
- `thanks.tex`：致谢内容，已由 `main.tex` 在文末引入。
- `Figures/`：论文图片和签名图片等资源目录。
- `style/`：模板样式、校徽、字体和参考文献样式等内部资源，普通使用者通常不要改。
- `.vscode/settings.json`、`.latexmkrc`：VS Code LaTeX Workshop 和 latexmk 编译配置。
- `neudissertation.cls`：模板类文件，只用于确认公开接口；普通使用者一般不要直接修改。

## Rules

- 优先编辑 `main.tex`、摘要文件、章节 `.tex`、`references.bib`、`thanks.tex` 和 `Figures/`。
- 不要为了调整封面、题名页、声明页、页眉、目录、图表编号而直接修改 `neudissertation.cls`；先使用 README 和 `main.tex` 中的公开接口。
- `main.tex` 是唯一主入口；章节文件中不要再写 `\documentclass`、`\begin{document}` 或 `\end{document}`。
- 正文从 `\mainmatter` 后开始，章节用 `\input{chapter1}` 这类方式引入。
- 图片使用相对路径，例如 `Figures/oaspl_a.pdf`；文件名和大小写应与磁盘一致。
- 推荐使用 XeLaTeX / latexmk 编译，具体命令以 README 为准。
- 删除示例内容时，只删除或注释 `\input{chapter0-guide}` 和不需要的章节内容，不要删除模板必须的封面、摘要、目录、参考文献结构。

## Workflow

1. 打开 `README.md` 和 `main.tex`，先确认模板的入口结构和编译命令。
2. 在 `main.tex` 的 `\neudisetup{...}` 中填写题名、作者、学院、专业、导师、日期等元数据。
3. 在 `abstract-cn.tex` 和 `abstract-en.tex` 中替换摘要正文和关键词。
4. 先保留 `chapter0-guide.tex` 作为图、表、公式、引用示例；开始正式写作时从 `chapter1.tex` 起组织正文。
5. 新增章节时创建新的 `chapterN.tex`，并在 `main.tex` 的 `\mainmatter` 后按顺序加入 `\input{chapterN}`。
6. 把图片放入 `Figures/`，把文献条目放入 `references.bib`。
7. 在本地运行 `latexmk -xelatex main.tex`；若使用 VS Code，可使用项目内置 LaTeX Workshop 配方；若使用 Overleaf，选择 XeLaTeX 编译器。
8. 定稿前从 `main.tex` 删除或注释 `\input{chapter0-guide}`，检查示例内容、TODO 和占位符是否清理干净。

## Examples

`main.tex` 的核心组织方式：

```latex
\documentclass[professional-degree, final-cover]{neudissertation}

\neudisetup{
  title-cn = {论文中文题名},
  title-en = {English Dissertation Title},
  author-cn = {作者姓名},
  author-en = {Author Name},
  college-cn = {学院名称},
  major-cn = {专业名称},
  major-en = {Major Name},
  degree-level = {博士},
  discipline = {电子信息},
  supervisor-cn = {导师姓名},
  supervisor-title-cn = {教授},
  supervisor-affiliation-cn = {东北大学某学院},
  supervisor-en = {Professor Supervisor},
  cover-year = {2026},
  cover-month = {6}
}

\begin{document}

\makeneucovers
\frontmatter
\makeneudeclaration

\begin{abstractcn}
  \input{abstract-cn}
\end{abstractcn}

\begin{abstracten}
  \input{abstract-en}
\end{abstracten}

\tableofcontents
\mainmatter

\input{chapter1}
\input{chapter2}

\backmatter
\begin{referencescn}
  \bibliography{references}
\end{referencescn}

\input{thanks}

\end{document}
```

新增章节文件 `chapter2.tex` 的最小内容：

```latex
%!TEX root = ./main.tex
\chapter{相关工作}
\label{chap:related-work}

这里写第二章正文。
```

最短本地编译命令：

```bash
latexmk -xelatex main.tex
```

## Common mistakes

- 把正文直接写进 `neudissertation.cls`：应写入章节 `.tex` 文件，并由 `main.tex` 引入。
- 新建章节后忘记在 `main.tex` 加 `\input{chapterN}`：章节不会出现在 PDF 中。
- 章节文件里又写了一套完整导言区：删除章节文件中的 `\documentclass` 和 `document` 环境。
- 删除了 `\frontmatter`、`\mainmatter` 或 `\backmatter`：页码、目录和后文结构可能异常，应保留 `main.tex` 的基本结构。
- Overleaf 使用 pdfLaTeX：README 要求选择 XeLaTeX。
- 定稿时仍保留 `chapter0-guide.tex`、示例章节、示例文献或占位内容：提交前应全局搜索并清理。
