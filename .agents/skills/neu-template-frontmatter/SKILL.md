---
name: neu-template-frontmatter
description: 东北大学博士学位论文 LaTeX 模板前置页配置。用于普通模板使用者通过 \neudisetup 配置封面、中文/英文题名页、作者、学院、专业、导师、学号、日期、学术学位/专业学位、盲审版、最终版封面、声明页签名图片、中文摘要、英文摘要、中文关键词、英文关键词和 main.tex 前置部分顺序。
---

# NEU 模板前置页配置

## Purpose

帮助用户用模板公开接口配置封面、题名页、声明页、摘要、关键词、盲审版和最终版封面，不直接手写或修改生成页面。

## When to use

- 需要填写或修改论文题名、作者、学院、专业、导师、学号和日期。
- 需要切换学术学位 / 专业学位、盲审版 / 非盲审版、是否生成最终版封面。
- 需要配置声明页签名图片、签名日期或论文在线公开时间。
- 需要确认中文摘要、英文摘要和关键词环境的写法。
- 需要检查 `main.tex` 前置部分顺序是否正确。

## Key files

- `main.tex`：在 `\begin{document}` 前配置 `\documentclass[...]` 和 `\neudisetup{...}`，在文档开始后生成封面、声明、摘要和目录。
- `abstract-cn.tex`：中文摘要正文，末尾使用 `\cnkeywords{...}`。
- `abstract-en.tex`：英文摘要正文，末尾使用 `\enkeywords{...}`。
- `Figures/signature.jpeg` 或用户自己的签名图片：可通过 `author-signature`、`supervisor-signature` 引用。
- `README.md`：公开字段和示例的优先参考。

## Rules

- 封面、题名页和声明页信息优先通过 `\neudisetup{...}` 配置，不要在生成页面上手写元信息。
- `\neudisetup{...}` 放在 `\begin{document}` 前。
- 盲审版通过 `\documentclass[blindreview=true]{neudissertation}` 开启；普通版本使用 `blindreview=false`。
- `professional-degree=false` 表示学术学位，中文题名页右侧显示“学科门类”；`professional-degree=true` 表示专业学位，右侧显示“专业学位类别”。对应值仍写在 `discipline` 中。
- 日期优先使用 `submit-year/month`、`defense-year/month`、`degree-year/month`、`cover-year/month` 这类数字字段；模板会自动生成中文和英文日期。
- `author-signature`、`supervisor-signature` 可为空；为空时声明页签名处留空。
- `final-cover=true` 会在中英文题名页前增加 2026 最终版博士学位论文封面；是否启用以学校提交要求为准。
- 盲审版除了检查模板自动隐藏的作者和导师信息，还要人工检查摘要、致谢、项目来源、图片、文件名、成果列表等是否暴露个人或课题组信息。
- 摘要环境只负责排版；摘要内容质量不属于本 skill 范围。

## Workflow

1. 在 `main.tex` 顶部选择文档类模式：盲审用 `blindreview=true`，非盲审用 `blindreview=false`。
2. 在 `\neudisetup{...}` 中填写论文元数据：分类号、密级、UDC、学号、中文/英文题名、作者、学院、专业、学位层级、导师和日期。
3. 根据学位类型设置 `professional-degree` 和 `discipline`。
4. 根据提交版本设置 `final-cover`，必要时设置 `final-cover-year`、`final-cover-month` 或 `final-cover-logo`。
5. 如声明页需要签名图片，放入 `Figures/` 并设置 `author-signature`、`supervisor-signature`、`signature-height`；需要固定签名日期时设置 `signature-date`。
6. 在 `\begin{document}` 后保持推荐顺序：`\makeneucovers`、`\frontmatter`、`\makeneudeclaration`、中文摘要、英文摘要、目录。
7. 在 `abstract-cn.tex` 写中文摘要并用 `\cnkeywords{...}` 填关键词；在 `abstract-en.tex` 写英文摘要并用 `\enkeywords{...}` 填关键词。
8. 编译后逐页检查封面、中文题名页、英文题名页、声明页、摘要和目录。

## Examples

`main.tex` 中的最小元数据配置：

```latex
\documentclass[blindreview=false]{neudissertation}

\neudisetup{
  classification = {},
  security-level = {},
  udc = {},
  student-id = {2026000000},
  title-cn = {论文中文题名},
  title-en = {English Dissertation Title},
  author-cn = {作者姓名},
  author-en = {Author Name},
  college-cn = {计算机科学与工程学院},
  major-cn = {计算机技术},
  major-en = {Computer Software and Theory},
  degree-level = {博士},
  professional-degree = true,
  discipline = {电子信息},
  supervisor-cn = {导师姓名},
  supervisor-title-cn = {教授},
  supervisor-affiliation-cn = {东北大学计算机科学与工程学院},
  supervisor-en = {Professor Supervisor},
  submit-year = {2026},
  submit-month = {4},
  defense-year = {2026},
  defense-month = {5},
  degree-year = {2026},
  degree-month = {6},
  defense-chair = {答辩主席姓名},
  defense-chair-title = {教授},
  cover-year = {2026},
  cover-month = {6},
  online-release = {两年},
  signature-date = {},
  author-signature = {Figures/signature.jpeg},
  supervisor-signature = {Figures/signature.jpeg},
  signature-height = {8mm},
  final-cover = true
}
```

学术学位 / 专业学位切换：

```latex
% 学术学位：题名页显示“学科门类：”
\neudisetup{professional-degree=false, discipline={工学}}

% 专业学位：题名页显示“专业学位类别：”
\neudisetup{professional-degree=true, discipline={电子信息}}
```

盲审版入口：

```latex
\documentclass[blindreview=true]{neudissertation}
```

摘要文件写法：

```latex
% abstract-cn.tex
这里写中文摘要正文。

\cnkeywords{关键词一；关键词二；关键词三}
```

```latex
% abstract-en.tex
Here is the English abstract.

\enkeywords{keyword one; keyword two; keyword three}
```

`main.tex` 前置部分推荐顺序：

```latex
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
```

## Common mistakes

- 在封面 PDF 页面上手工改字：应修改 `\neudisetup{...}` 字段后重新编译。
- 把 `\neudisetup{...}` 写到 `\begin{document}` 后：元数据可能不会按预期用于前置页。
- 专业学位只改了 `discipline`，忘记设置 `professional-degree=true`：题名页字段标签会不匹配。
- 盲审时只依赖 `blindreview=true`：仍需人工检查正文、致谢、成果、项目号、图片和文件名。
- 摘要文件里使用旧环境名 `zhabstract`：README 明确中文摘要环境为 `abstractcn`。
- 关键词写在摘要环境外：应在 `abstract-cn.tex` 或 `abstract-en.tex` 内分别使用 `\cnkeywords{...}`、`\enkeywords{...}`。
- 签名图片路径写错或文件不存在：把图片放入 `Figures/`，并检查扩展名和大小写。
