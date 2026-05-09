# 东北大学博士学位论文 LaTeX 模板（2026 版）

本模板依据 `2026-原始版本/2-学位论文格式（博士）（页眉部分只保留第几章的信息，2026版）.docx` 和 `format-checklist-2026.md` 重构，当前版本仅面向博士学位论文。

## 构建

推荐使用 XeLaTeX：

```powershell
latexmk -xelatex main.tex
```

模板目标兼容 TeX Live 2023--2026，已在如下环境进行测试：

- 本地环境
  [] TeX Live 2023 (Windows 11)
  [] TeX Live 2026 (Windows 11)
- 在线环境
  [] 本地部署版本 Overleaf (TeX Live 2025)
  [] Overleaf 云上版本 (TeX Live 20**)

项目内置了 vscode 的 LaTeX Workshop 插件配置，使用 latexmk 进行构建，有需要可以编辑 `.vscode/settings.json` 来调整构建方式。

## 模板使用说明

可以直接查看 main.tex 中第一章的示例内容，或参考以下说明来组织自己的论文内容。

### 基本入口

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
  submit-year = {2016},
  submit-month = {4},
  defense-year = {2016},
  defense-month = {6},
  degree-year = {2016},
  degree-month = {7},
  defense-chair = {王某某},
  cover-year = {2016},
  cover-month = {7},
  online-release = {两年},
  signature-date = {},
  author-signature = {},
  supervisor-signature = {},
  signature-height = {8mm},
  final-cover = true
}
```

参考研究生院的最新版本，2026新版似乎改变了页眉的样式为居中样式，使用 `header-2026` 可以控制页眉样式，默认为 2026 风格：

```latex
\neudisetup{header-2026=true} % 使用 2026 风格页眉
```

日期字段使用数字填写年月：`submit-year/month`、`defense-year/month`、`degree-year/month`、`cover-year/month`。模板会自动生成中文日期（如 `2016年7月`）和英文题名页日期（如 `July 2016`），因此通常不需要再填写 `cover-date-en`。旧的 `submit-date`、`defense-date`、`degree-date`、`cover-date-cn`、`cover-date-en` 仍可作为兼容写法使用。

`author-signature` 和 `supervisor-signature` 支持 `png`、`jpg`、`pdf` 等 `\includegraphics` 可读取的签名文件；为空时声明页签名处留空。`signature-date` 为空时默认使用 `cover-year/month` 生成的中文日期，`signature-height` 用于调整签名图片高度。

`final-cover` 用于控制是否在现有中英文题名页之前增加一页 TeX 化的 2026 最终版博士学位论文封面：

```latex
\neudisetup{final-cover=true}  % 增加最终版封面
\neudisetup{final-cover=false} % 不增加最终版封面
```

该封面默认复用 `title-cn`、`author-cn`、`student-id`、`college-cn`、`major-cn`、`supervisor-cn`、`supervisor-title-cn` 和 `cover-year/month`，并自动排成封面所需的 `2016 年    07 月` 样式。如需单独调整封面底部日期，可设置 `final-cover-year = {2016}`、`final-cover-month = {7}`；如需替换顶部校名校徽图片，可设置 `final-cover-logo = {path/to/logo.pdf}`。

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

### 正文结构

`main.tex` 组织为：

```latex
\makeneucovers
\frontmatter
\makeneudeclaration
\begin{abstractcn}...\end{abstractcn}
\begin{abstracten}...\end{abstracten}
\tableofcontents
\mainmatter
...
\backmatter
\begin{referencescn}
  \bibliography{references}
\end{referencescn}
\begin{achievementscn}...\end{achievementscn}
```

封面和题名页无页码；声明、摘要、目录使用罗马数字页码；正文从第 1 章开始使用阿拉伯数字页码并从 1 起编。模板按双面打印组织分页，封面、题名页、声明、摘要、目录和正文章首页会自动从奇数页开始，必要时插入无页眉页脚的空白背面页。

### 参考文献

参考文献采用 GB/T 7714 顺序编码制，类文件默认使用项目内的 `gbt7714-unsrt.bst`。正文陈述处使用上标引用：

```latex
已有研究表明...\upcite{guo_2023_research}
```

文献作为句子成分时使用正文型引用：

```latex
文献 \inlinecite{guo_2023_research} 详细讨论了这一问题。
```

参考文献部分统一放在 `referencescn` 环境内：

```latex
\begin{referencescn}
  \nocite{guo_2023_research}
  \bibliography{references}
\end{referencescn}
```

### 学术成果

学术成果部分统一放在 `achievementscn` 环境内，环境会自动生成“攻读博士学位期间取得的学术成果”标题：

```latex
\begin{achievementscn}
  \begin{enumerate}
    \item 第一作者. 示例论文题名[J]. 示例期刊，20xx，1（1）：1-10.
  \end{enumerate}
\end{achievementscn}
```

### 图表公式

图题在图下方，表题在表上方，均按章编号。

```latex
\neufigcaption{fig:demo}{中文图题}{English figure title}
\neutabcaption{tab:demo}{中文表题}{English table title}
\neueqref{eq:demo}
```

中文摘要环境统一为 `abstractcn`，旧的 `zhabstract` 已不再提供。现有文档请直接改用 `\begin{abstractcn}` 和 `\end{abstractcn}`。

模板保留旧别名 `\twofigcaption`、`\twotabcaption`、`\figref`、`\tabref`、`\equref`，便于旧示例章节继续编译。

## 格式比较工具

为了快速比较模板生成的 PDF 与学校提供的样例 PDF 之间的格式差异，项目在 `dev/` 目录下提供了一个基于 Python 的 PDF 比较工具 `compare_pdf_visual.py`，使用这个工具可以比较两份 PDF 文件的视觉差异，并生成一个差异图像，帮助开发者快速定位格式上的不一致之处。

这个工具用于开发过程中，帮助确保模板生成的 PDF 与学校提供的样例 PDF 在格式上保持一致。使用方法如下：

```bash
uv run dev\compare_pdf_visual.py .\template_reference\word_page\cover_page.pdf main.pdf --word-page 1 --latex-page 1 --dpi 300 --output-dir tmp\pdf-diff --prefix cover_page --save-rendered
```

其中：

- `--word-page` 和 `--latex-page` 分别指定要比较的 Word PDF 页码和 LaTeX PDF 页码。
- `--dpi` 指定生成差异图像的分辨率。
- `--output-dir` 指定差异图像的输出目录。
- `--prefix` 指定差异图像文件的前缀。
- `--save-rendered` 选项会保存渲染后的 Word PDF 和 LaTeX PDF 图像，便于进一步分析。

开发过程中的比较文件保留了一份在 `template_reference/compare_result` 目录下，开发中主要比较了封面页、首页、英文首页和声明页。

```bash
uv run dev\compare_pdf_visual.py .\template_reference\word_page\cover_page.pdf main.pdf --word-page 1 --latex-page 1 --dpi 300 --output-dir tmp\pdf-diff --prefix cover_page --save-rendered
uv run dev\compare_pdf_visual.py .\template_reference\word_page\title_page.pdf main.pdf --word-page 1 --latex-page 3 --dpi 300 --output-dir tmp\pdf-diff --prefix title_page --save-rendered
uv run dev\compare_pdf_visual.py .\template_reference\word_page\en_title_page.pdf main.pdf --word-page 1 --latex-page 5 --dpi 300 --output-dir tmp\pdf-diff --prefix title_page_en --save-rendered
uv run dev\compare_pdf_visual.py .\template_reference\word_page\declear.pdf main.pdf --word-page 1 --latex-page 7 --dpi 300 --output-dir tmp\pdf-diff --prefix declare --save-rendered
```

## 模板构建来源和参考信息

格式相关参考由见 [东北大学研究生院-下载专区-申请博士学位相关表格材料（2026年版）](http://www.graduate.neu.edu.cn/_upload/article/files/13/40/aaeb638d41dc8f73ad0ac07c1cce/5884da82-cb8d-4323-96d9-9ab4b6f92932.zip) ，模板相关的文件也包含在 `template_reference/` 目录下。

> [!WARNING]
> 但请注意，学校发布的模板中，后续的样例也有和格式不符的情况，因此还参考了往届的论文来做参考。
> 为了视觉效果，有些内容也是经过调整的，可能和学校提供的样例略有差异，但整体风格和格式要求是保持一致的。

模板源码以 [Gitee NEUCloudLab/NEU论文Latex模板](https://gitee.com/NEUCloudLab/NEU-dissertation-template) 的基础上重构，感谢原作者的贡献。部分内容参考了 [Github sci-m-wang/NEU-Thesis](https://github.com/sci-m-wang/NEU-Thesis)。

## License

GPL-2.0 License，详见 `LICENSE` 文件。
