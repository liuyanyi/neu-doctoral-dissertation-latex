# 东北大学博士学位论文 LaTeX 模板（2026 版）

本模板依据 `2026-原始版本/2-学位论文格式（博士）（页眉部分只保留第几章的信息，2026版）.docx` 和 `format-checklist-2026.md` 重构，当前版本仅面向博士学位论文。

## 编译方式

推荐使用 XeLaTeX：

```powershell
latexmk -xelatex main.tex
```

如果根目录已有旧辅助文件被编辑器占用，可临时输出到 `build/`：

```powershell
latexmk -xelatex -outdir=build -jobname=neu2026 main.tex
```

## 基本入口

```latex
\documentclass[blindreview=false]{neudissertation}

\neudisetup{
  classification = {},
  security-level = {},
  udc = {},
  student-id = {},
  title-cn = {面向机械翻译的随机词汇语义驱动方法的研究},
  title-en = {Research on Stochastic Lexical Semantic Driven Methods for Machine Translation},
  author-cn = {李某某},
  author-en = {Moumou Li},
  college-cn = {计算机科学与工程学院},
  major-cn = {计算机软件与理论},
  major-en = {Computer Software and Theory},
  degree-level = {博士},
  discipline = {},
  supervisor-cn = {张某某},
  supervisor-title-cn = {教授},
  supervisor-affiliation-cn = {东北大学计算机科学与工程学院},
  supervisor-en = {Professor Moumou Zhang},
  submit-date = {2016年4月},
  defense-date = {2016年6月},
  degree-date = {2016年7月},
  defense-chair = {王某某},
  cover-date-cn = {2016年7月},
  cover-date-en = {July 2016},
  online-release = {两年},
  signature-date = {},
  author-signature = {},
  supervisor-signature = {},
  signature-height = {8mm}
}

注意：选项 `header-style` 已移除，使用 `header-2026` 来控制页眉样式：

```latex
\neudisetup{header-2026=true} % 使用 2026 风格页眉
```
```

`author-signature` 和 `supervisor-signature` 支持 `png`、`jpg`、`pdf` 等 `\includegraphics` 可读取的签名文件；为空时声明页签名处留空。`signature-date` 为空时默认使用 `cover-date-cn`，`signature-height` 用于调整签名图片高度。

可选第二导师字段为空时不会占位：

```latex
cosupervisor-cn = {},
cosupervisor-title-cn = {},
cosupervisor-affiliation-cn = {},
cosupervisor-en = {},
```

双盲评审版使用：

```latex
\documentclass[blindreview=true]{neudissertation}
```

## 正文结构

`main.tex` 已按 2026 版组织为：

```latex
\makeneucovers
\frontmatter
\makeneudeclaration
\begin{abstract-cn}...\end{abstract-cn}
\begin{enabstract}...\end{enabstract}
\tableofcontents
\mainmatter
...
\backmatter
\bibliography{references}
```

封面和题名页无页码；声明、摘要、目录使用罗马数字页码；正文从第 1 章开始使用阿拉伯数字页码并从 1 起编。模板按双面打印组织分页，封面、题名页、声明、摘要、目录和正文章首页会自动从奇数页开始，必要时插入无页眉页脚的空白背面页。

## 参考文献

参考文献采用 GB/T 7714 顺序编码制，类文件默认使用项目内的 `gbt7714-unsrt.bst`。正文陈述处使用上标引用：

```latex
已有研究表明...\upcite{guo_2023_research}
```

文献作为句子成分时使用正文型引用：

```latex
文献 \inlinecite{guo_2023_research} 详细讨论了这一问题。
```

## 图表公式

图题在图下方，表题在表上方，均按章编号。

```latex
\neufigcaption{fig:demo}{中文图题}{English figure title}
\neutabcaption{tab:demo}{中文表题}{English table title}
\neueqref{eq:demo}
```

中文摘要环境统一为 `abstract-cn`，旧的 `zhabstract` 已不再提供。现有文档请直接改用 `\begin{abstract-cn}` 和 `\end{abstract-cn}`。

模板保留旧别名 `\twofigcaption`、`\twotabcaption`、`\figref`、`\tabref`、`\equref`，便于旧示例章节继续编译。
