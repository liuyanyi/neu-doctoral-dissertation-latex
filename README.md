# 东北大学博士学位论文 LaTeX 模板（2026 版）

当前版本：`v2026.10`。版本变更见 [CHANGELOG.md](CHANGELOG.md)。

## 构建

推荐使用 XeLaTeX 编译：

```bash
latexmk -xelatex main.tex
```

### 兼容性

模板目标兼容 TeX Live 2023–2026。以下为项目历史验证环境；`v2026.10` 本次仅在 Windows / TeX Live 2026 完成回归，其他环境尚未复测：

#### 本地环境

- [x] TeX Live 2023 (Windows 11)
- [x] TeX Live 2026 (Windows 11)

#### 在线环境

- [x] 本地部署版本 Overleaf (TeX Live 2025)
- [x] Overleaf 云上版本 (TeX Live 2024, 2025)

> [!NOTE]
> Overleaf 上记得选择 XeLaTeX 编译器。云上版本容易出现编译超时的情况，建议在本地环境编译，或使用 Overleaf 的本地部署版本。

项目内置了 VS Code 的 LaTeX Workshop 插件配置，使用 latexmk 进行构建，有需要可以编辑 `.vscode/settings.json` 来调整构建方式。

同时，项目也提供了面向模板使用者的代码提示和 snippets：

- `.vscode/settings.json` 中配置了模板公开命令的 LaTeX Workshop 补全，例如 `\neudisetup`、`\neufigcaption`、`\neutabcaption`、`\neueqref`、`\upcite` 和 `\inlinecite`。
- `.vscode/neu-template.code-snippets` 中提供了常用结构片段。在 `.tex` 文件中输入 `neu-setup-basic`、`neu-setup-professional`、`neu-setup-blind`、`neu-figure`、`neu-subfigures`、`neu-table`、`neu-equation`、`neu-references` 等前缀，再从补全列表选择或按 `Tab`，即可插入对应骨架。
- 如果补全没有出现，请确认已安装 LaTeX Workshop、以仓库根目录打开 VS Code、当前文件语言模式为 LaTeX，并已信任工作区。

更多说明见 [VS Code 与 LaTeX Workshop 补全](docs/vscode-latex-workshop.md)。这些 snippets 只帮助输入模板接口，不负责论文内容写作。

## 模板使用说明

可以直接查看 `main.tex` 中第一章的示例内容，或参考以下说明来组织自己的论文内容。正式写作时，建议先保留 `chapter0-guide.tex` 作为排版对照；定稿前再从 `main.tex` 中删除或注释 `\input{chapter0-guide}`。

### 基本入口

```latex
\documentclass[
  final-cover
]{neudissertation}

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
  discipline = {工学},
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
  defense-chair-title = {教授},
  cover-year = {2016},
  cover-month = {7},
  online-release = {两年},
  signature-date = {},
  author-signature = {},
  supervisor-signature = {},
  signature-height = {8mm}
}
```

`blindreview`、`professional-degree` 和 `final-cover` 是全局模式开关，只写在 `\documentclass[...]` 里，让文件开头就能看出当前版本用途。开关裸写表示开启，例如 `final-cover`；不写表示关闭。

审阅正文时可使用 `\documentclass[no-frontmatter]{neudissertation}`：跳过封面、声明、中英文摘要和目录，按原有入口调用 `\mainmatter` 后，正文从阿拉伯页码 1 开始。该选项默认关闭；提交正式论文前应移除。摘要内容仍会被 LaTeX 处理，但不输出到页面。

`table`、`table*`（含 `[H]`）和 `longtable` 中的表内文字默认使用五号（10.5 bp），表格结束后恢复外部字号；仍可在表内显式覆盖。独立使用的 `tabular` 不自动改变字号。中英文图表题统一为五号，并兼容 `DocumentMetadata` 加载的 `latex-lab` 题注实现。

参考文献国标版本使用 `bibliography` 选项，默认 `2025`（GB/T 7714—2025），可选 `2015`（GB/T 7714—2015）：

```latex
\documentclass[bibliography=2025]{neudissertation} % GB/T 7714—2025（默认）
\documentclass[bibliography=2015]{neudissertation} % GB/T 7714—2015
```

两个版本均基于官方 gbt7714 v3.0.1 样式：2025 版西文作者姓不强制全大写（如 `Huang S C`），2015 版按标准仍输出全大写（如 `HUANG S C`）。随模板分发的 2025 版另修复了网页条目有出版者时重复输出年份的问题，保留括号内的创建或修改日期及访问日期。

参考研究生院的最新版本，2026新版似乎改变了页眉的样式为居中样式，使用 `header-2026` 可以控制页眉样式，默认为 2026 风格：

```latex
\neudisetup{header-2026=true} % 使用 2026 风格页眉
```

根据2026-06-24的最新版本，专业学位和学术学位的模板在封面上有所差异，所以新增了 `professional-degree` 设置用于调整。

`professional-degree` 用于控制中文题名页右侧字段标签。默认不写，表示学术学位并显示“学科门类：”；写上 `professional-degree` 时表示专业学位并显示“专业学位类别：”。字段值仍通过 `discipline` 填写：

```latex
\documentclass[professional-degree]{neudissertation}
\neudisetup{discipline={电子信息}}
```

日期字段使用数字填写年月：`submit-year/month`、`defense-year/month`、`degree-year/month`、`cover-year/month`。模板会自动生成中文日期（如 `2016年7月`）和英文题名页日期（如 `July 2016`），因此通常不需要再填写 `cover-date-en`。旧的 `submit-date`、`defense-date`、`degree-date`、`cover-date-cn`、`cover-date-en` 仍可作为兼容写法使用。

`author-signature` 和 `supervisor-signature` 支持 `png`、`jpg`、`pdf` 等 `\includegraphics` 可读取的签名文件；为空时声明页签名处留空。`signature-date` 为空时默认使用 `cover-year/month` 生成的中文日期，`signature-height` 用于调整签名图片高度。

签名图片以不占排版尺寸的叠加层显示，调整高度或更换宽高比不会移动签名标签、日期及声明正文。图片从签名标签后向右延伸；过大的图片仍可能覆盖相邻内容，应按声明页留白设置合适高度。

`final-cover` 用于控制是否在现有中英文题名页之前增加一页 TeX 化的 2026 最终版博士学位论文封面：

```latex
\documentclass[final-cover]{neudissertation} % 增加最终版封面
\documentclass{neudissertation}              % 不增加最终版封面
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
\documentclass[blindreview]{neudissertation}
```

### 正文结构

`main.tex` 的结构组织如下：

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

#### 页码说明

- 封面和题名页：无页码
- 声明、摘要、目录：罗马数字页码
- 正文：从第 1 章开始使用阿拉伯数字页码并从 1 起编

模板按双面打印组织分页，封面、题名页、声明、摘要、目录和正文章首页会自动从奇数页开始，必要时插入无页眉页脚的空白背面页。

### 正文写作与排版建议

正文从 `\mainmatter` 之后开始，每章建议单独放在 `chapter1.tex`、`chapter2.tex` 等文件中，并在 `main.tex` 中用 `\input{...}` 引入。

模板已经统一设置正文字体、字号、行距、段落首行缩进、页眉页脚和章节标题。一般正文中不需要手动使用 `\zihao`、`\song`、`\hei`、`\vspace` 等命令调版；只有在术语强调、样例展示或特殊页面确有需要时再局部使用。

默认宋体已经配置伪粗体，中文正文中可以使用 `\textbf{...}` 或 `\bfseries` 做局部强调。加粗适合术语、表格重点值或短语级强调，不建议用于整段正文；标题式强调优先交给章节标题层级或黑体命令。

脚注用于补充说明，不宜放置过长正文。LaTeX 的脚注位置跟随当前页的正文排版区：如果某页因为图表浮动、分页或标题避孤行而没有排满，脚注可能看起来没有贴到纸张最底部，这是正常现象。遇到这类页面时，优先检查图表位置、图表大小和是否使用了强制分页，而不是为脚注手动添加垂直空白。

正文中尽量避免随手使用 `\newpage`、`\clearpage`、`\FloatBarrier` 或大量手写 `\vspace`。这些命令会限制 LaTeX 自动分页，容易造成页底大块空白；只有在章节结构、附录或确实需要清空浮动体时再使用。

### 模板命令说明

本节列出模板面向作者提供的主要命令和环境。类文件内部使用的 `\neu@...` 命令不建议在正文中直接调用；正式写作优先使用下表中的公开接口。

#### 入口与页面生成

| 命令或环境 | 用途 | 典型位置 |
| :--- | :--- | :--- |
| `\neudisetup{key=value, ...}` | 设置题名、作者、导师、日期、封面和声明页等元数据 | `\begin{document}` 前 |
| `\makeneucovers` | 生成最终版封面、中文题名页和英文题名页 | `\begin{document}` 后 |
| `\makeneudeclaration` | 生成独创性声明和版权使用授权书 | `frontmatter` 中 |
| `abstractcn` | 中文摘要环境，自动加入目录 | `frontmatter` 中 |
| `abstracten` | 英文摘要环境，自动加入目录 | `frontmatter` 中 |
| `\cnkeywords{...}` | 中文关键词 | `abstractcn` 环境内 |
| `\enkeywords{...}` | 英文关键词 | `abstracten` 环境内 |
| `referencescn` | 参考文献环境，内部放 `\bibliography{...}` | `backmatter` 中 |
| `achievementscn` | 学术成果环境，自动生成标题并加入目录 | `backmatter` 中 |

#### 图表公式与交叉引用

| 命令或环境 | 用途 | 输出或效果 |
| :--- | :--- | :--- |
| `\neufigcaption{label}{中文图题}{English figure title}` | 生成中英文双语图题并设置标签 | 中文图题在图下方，英文图题另起一行 |
| `\neutabcaption{label}{中文表题}{English table title}` | 生成中英文双语表题并设置标签 | 表题位于表格上方 |
| `neusubfigure` | 子图环境，用法类似 `subfigure` | 可排布并列子图或 2×2 子图 |
| `\neusubfigcaption{label}{中文子图题}` | 生成子图题并设置标签 | 子图编号为 `(a)`、`(b)` 等 |
| `\neufigref{label}` | 引用普通图或总图 | `图 x.y` |
| `\neusubfigref{label}` | 引用子图 | `图 x.y(a)` |
| `\neutabref{label}` | 引用表格 | `表 x.y` |
| `\neueqref{label}` | 引用公式 | `式（x.y）` |

#### 文献引用

| 命令 | 用途 | 示例 |
| :--- | :--- | :--- |
| `\upcite{key}` | 上标型文献引用，适合句末说明来源 | `已有研究...\upcite{key}` |
| `\inlinecite{key}` | 正文型文献引用，适合作为句子成分 | `文献 \inlinecite{key} 指出...` |

#### 字体与字号辅助命令

模板已经统一设置正文、标题、页眉和题注样式，正式论文中通常不需要手动切换字体和字号。确有局部展示或强调需求时，可使用以下辅助命令：

| 命令 | 含义 |
| :--- | :--- |
| `\song`、`\hei`、`\kai`、`\fs` | 宋体、黑体、楷体、仿宋 |
| `\sihao`、`\xiaosi`、`\wuhao`、`\xiaowu` | 四号、小四、五号、小五 |
| `\textbf{...}` 或 `\bfseries` | 局部加粗强调，适合术语、短语或表格重点值 |

### 参考文献

参考文献采用 GB/T 7714 顺序编码制，样式文件默认使用项目内的 `gbt7714-unsrt.bst`。

#### 引用方式

文献条目写在 `references.bib` 中，正文里通过条目的 key 引用。常用引用命令有两种：

- `\upcite{key}`：上标型引用，适合放在句末或段末，用来说明前面观点、数据或方法的来源。
- `\inlinecite{key}`：正文型引用，适合把文献作为句子成分使用，例如“文献 [1] 指出……”。

正文陈述处使用 `\upcite`：

```latex
已有研究表明...\upcite{guo_2023_research}
```

文献作为句子成分时使用 `\inlinecite`：

```latex
文献 \inlinecite{guo_2023_research} 详细讨论了这一问题。
```

两种命令都支持可选参数，通常用于补充页码或章节信息：

```latex
已有研究对该问题进行了讨论\upcite[第 12 页]{guo_2023_research}。
文献 \inlinecite[第 3 章]{guo_2023_research} 给出了相关定义。
```

多篇文献可以写在同一个引用命令中，key 之间用英文逗号分隔：

```latex
已有研究讨论了相关问题\upcite{guo_2023_research,thakkar_2018_performance}。
```

#### 参考文献环境

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

图题在图下方，表题在表上方，均按章编号。建议使用模板提供的 `\neufigcaption`、`\neutabcaption`、`\neufigref`、`\neutabref` 和 `\neueqref`。

图片示例：

```latex
\begin{figure}[!htbp]
  \centering
  \includegraphics[width=0.75\textwidth]{Figures/demo.pdf}
  \neufigcaption{fig:demo}{中文图题}{English figure title}
\end{figure}

如 \neufigref{fig:demo} 所示，图片应在正文中被引用。
```

普通并列图片示例：

```latex
\begin{figure}[!htbp]
  \centering
  \begin{minipage}[t]{0.49\linewidth}
    \centering
    \includegraphics[width=\linewidth]{Figures/demo-a.pdf}
  \end{minipage}
  \hfill
  \begin{minipage}[t]{0.49\linewidth}
    \centering
    \includegraphics[width=\linewidth]{Figures/demo-b.pdf}
  \end{minipage}
  \neufigcaption{fig:demo-side-by-side}{并列图中文总题名}{English caption for side-by-side figures}
\end{figure}

如 \neufigref{fig:demo-side-by-side} 所示，普通并列图片只有一个总图号，适合不需要分别引用左右图片的场景。
```

并列子图示例：

```latex
\begin{figure}[!htbp]
  \centering
  \begin{neusubfigure}{0.49\linewidth}
    \includegraphics[width=\linewidth]{Figures/demo-a.pdf}
    \neusubfigcaption{fig:demo-a}{子图中文题名}
  \end{neusubfigure}
  \hfill
  \begin{neusubfigure}{0.49\linewidth}
    \includegraphics[width=\linewidth]{Figures/demo-b.pdf}
    \neusubfigcaption{fig:demo-b}{子图中文题名}
  \end{neusubfigure}
  \neufigcaption{fig:demo-subfig}{并列图中文总题名}{English caption for subfigures}
\end{figure}

如 \neufigref{fig:demo-subfig}、\neusubfigref{fig:demo-a} 和 \neusubfigref{fig:demo-b} 所示，总图引用显示为“图 x.y”，子图引用显示为“图 x.y(a)”和“图 x.y(b)”。
```

二乘二子图示例：

```latex
\begin{figure}[!htbp]
  \centering
  \begin{neusubfigure}{0.49\linewidth}
    \includegraphics[width=\linewidth]{Figures/demo-2x2-a.pdf}
    \neusubfigcaption{fig:demo-2x2-a}{子图中文题名}
  \end{neusubfigure}
  \hfill
  \begin{neusubfigure}{0.49\linewidth}
    \includegraphics[width=\linewidth]{Figures/demo-2x2-b.pdf}
    \neusubfigcaption{fig:demo-2x2-b}{子图中文题名}
  \end{neusubfigure}

  \par\vspace{2bp}

  \begin{neusubfigure}{0.49\linewidth}
    \includegraphics[width=\linewidth]{Figures/demo-2x2-c.pdf}
    \neusubfigcaption{fig:demo-2x2-c}{子图中文题名}
  \end{neusubfigure}
  \hfill
  \begin{neusubfigure}{0.49\linewidth}
    \includegraphics[width=\linewidth]{Figures/demo-2x2-d.pdf}
    \neusubfigcaption{fig:demo-2x2-d}{子图中文题名}
  \end{neusubfigure}
  \neufigcaption{fig:demo-2x2}{四幅子图中文总题名}{English caption for two-by-two subfigures}
\end{figure}

如 \neufigref{fig:demo-2x2} 所示，四幅子图共享一个总图号；如 \neusubfigref{fig:demo-2x2-a} 至 \neusubfigref{fig:demo-2x2-d} 所示，子图可分别引用为“图 x.y(a)”至“图 x.y(d)”。
```

图形排版建议：

- 单张图片通常使用 `width=0.6\textwidth` 到 `width=0.8\textwidth`；如果图片本身信息密集，可适当放大到 `\textwidth`。
- 普通并列图片使用 `minipage`，适合多张图共享一个总图题且正文不需要分别引用每张图的场景。
- 并列子图使用 `neusubfigure` 和 `\neusubfigcaption`，适合需要在正文中引用“图 x.y(a)”、 “图 x.y(b)”的场景。
- 两列排布时，单个 `minipage` 或 `neusubfigure` 宽度建议取 `0.48\linewidth` 到 `0.49\linewidth`，中间用 `\hfill` 分隔。
- 多行子图之间可使用少量 `\par\vspace{2bp}` 调整垂直间距；若总图过高导致浮动困难，优先缩小图片宽度或拆成两幅总图。
- 同组子图的比例、坐标轴范围、字号和线宽应尽量一致；论文中优先使用 PDF 矢量图，照片或截图可使用 PNG/JPG。

表格示例：

```latex
\begin{table}[!htbp]
  \centering
  \neutabcaption{tab:demo}{中文表题}{English table title}
  \begin{tabular}{lcc}
    \toprule
    方法 & 指标一 & 指标二 \\
    \midrule
    Baseline & 0.85 & 0.84 \\
    Proposed & 0.92 & 0.91 \\
    \bottomrule
  \end{tabular}
\end{table}

如 \neutabref{tab:demo} 所示，表格应在正文中被引用。
```

浮动参数推荐使用 `[!htbp]`。它允许 LaTeX 在当前位置、页顶、页底或浮动页之间选择较合适的位置，通常比 `[H]` 更不容易造成上一页大面积留白。除非必须固定在源码所在位置，否则不建议在正文图表中使用 `[H]`；若图表仍造成空白，优先尝试把图表源码提前到首次引用附近、适当缩小图表，或将过大的表格拆分为多个表格。跨页长表建议使用 `longtable`。

公式示例：

```latex
\begin{equation}
  E = mc^2
  \label{eq:demo}
\end{equation}

如 \neueqref{eq:demo} 所示，重要公式应设置标签并在正文中引用。
```

中文摘要环境统一为 `abstractcn`，旧的 `zhabstract` 已不再提供。现有文档请直接改用 `\begin{abstractcn}` 和 `\end{abstractcn}`。

## 格式比较工具

为了快速比较模板生成的 PDF 与学校提供的样例 PDF 之间的格式差异，项目在 `dev/` 目录下提供了基于 Python 的 PDF 比较工具 `compare_pdf_visual.py`。该工具用于开发过程中，帮助确保模板生成的 PDF 与学校提供的样例 PDF 在格式上保持一致。

### 使用方法

```bash
uv run dev\compare_pdf_visual.py .\template_reference\word_page\cover_page.pdf main.pdf --word-page 1 --latex-page 1 --dpi 300 --output-dir tmp\pdf-diff --prefix cover_page --save-rendered
```

### 参数说明

| 参数 | 说明 |
| :--- | :--- |
| `--word-page` | Word PDF 的页码 |
| `--latex-page` | LaTeX PDF 的页码 |
| `--dpi` | 生成差异图像的分辨率 |
| `--output-dir` | 差异图像的输出目录 |
| `--prefix` | 差异图像文件的前缀 |
| `--save-rendered` | 保存渲染后的图像，便于进一步分析 |

### 开发中的比较命令

开发过程中的比较文件保留在 `template_reference/compare_result` 目录下，主要比较封面页、声明页、英文题名页、专业学位题名页和学术学位题名页。批量比较配置维护在 `dev/pdf_compare_cases.json` 中：

```bash
uv run --with-requirements dev/requirements.txt python dev/run_pdf_compare.py --output-dir tmp/pdf-compare
```

### CI 编译与 PDF 对比

仓库提供两个手动触发的 GitHub Actions：

- `Build`：只编译 `main.tex`，并上传 `main.pdf`、`main.log` 等构建产物。
- `PDF Compare`：编译默认专业学位版本，再生成并编译临时学术学位入口，随后按 `dev/pdf_compare_cases.json` 执行 PDF 视觉对比。
- `Release`：按 `.github/release-include.txt` 打包 TeX 模板、样例内容、`style/`、`Figures/`、`.agents/`、README、LICENSE 和 CHANGELOG，并发布到 GitHub Release。

### 版本与兼容性约定

- 发布版本使用 `vYYYY.MM`；同月追加发布使用 `vYYYY.MM.N`。`neudissertation.cls` 中的 `\ProvidesClass` 日期、版本必须与 Release tag 的年月和完整版本一致。
- `\documentclass` 选项、`\neudisetup` 配置项以及模板公开命令和环境原则上保持向后兼容。需要替换旧接口时，优先增加兼容别名并在更新日志中标记弃用。
- 如果确实必须进行破坏性变更，应在 `CHANGELOG.md` 中醒目标记，明确支持直接升级的最早版本、受影响的接口和具体迁移步骤；更早版本的用户应先升级到受支持版本，或按迁移说明手动调整。
- 每次发布都必须更新 `CHANGELOG.md`，说明功能变化、修复内容和兼容性影响，并写明“支持从哪个版本升级”；用户无需修改论文源码时也应明确写明“无需迁移”。
- Release workflow 会检查 tag 格式、类文件版本以及自上一个 tag 以来是否更新了 `CHANGELOG.md`，任一项不符合时停止发布。

两个 workflow 会复用 `.github/texlive-packages.txt` 中的 TeX Live 包列表，并缓存 apt 下载包；`PDF Compare` 还会缓存 Python pip 依赖。

PDF 对比完成后会上传 `pdf-compare` artifact，包含 `main.pdf`、`main.log`、临时学术学位版本 PDF/log，以及每个 case 的 diff、增强 diff、红蓝 overlay、highlight、Word 渲染页、LaTeX 渲染页和 metrics。`summary.md` 和 `summary.json` 汇总所有 case 的指标。
对比脚本也会在 workflow 日志末尾输出指标表格，并写入 GitHub Actions 的 Step Summary，便于不下载 artifact 直接检查结果。

`template_reference/compare_result/baseline` 下保留已接受的红蓝 overlay PNG 供人工审阅。CI 的阻断条件只比较 `baseline/diff_metrics.json` 中的指标窗口，不直接以 Word 原始模板的 diff 大小或 PNG 像素级一致性作为失败条件。

默认指标窗口为：

- `changed_percent`: ±0.05
- `mean_abs_diff`: ±0.1

本地更新 baseline：

```bash
latexmk -xelatex main.tex
uv run --with-requirements dev/requirements.txt python dev/make_academic_entry.py
latexmk -xelatex -jobname=main-academic -outdir=tmp/ci-academic tmp/ci-academic/main-academic.tex
uv run --with-requirements dev/requirements.txt python dev/run_pdf_compare.py --output-dir tmp/pdf-compare --update-baseline
```

本地检查 baseline：

```bash
uv run --with-requirements dev/requirements.txt python dev/run_pdf_compare.py --output-dir tmp/pdf-compare --check-baseline
```

## 模板构建来源和参考信息

~~格式参考自 [东北大学研究生院-下载专区-申请博士学位相关表格材料（2026年版）](http://www.graduate.neu.edu.cn/_upload/article/files/13/40/aaeb638d41dc8f73ad0ac07c1cce/5884da82-cb8d-4323-96d9-9ab4b6f92932.zip)，模板相关的文件也包含在 `template_reference/` 目录下。~~
最新版格式参考自 [东北大学研究生院-下载专区-申请博士学位相关表格材料（2026年6月版）](http://www.graduate.neu.edu.cn/_upload/article/files/6d/66/f7fcab86409eb9ad3aca3852594b/4ec51440-f4e4-40ed-a7c2-4efbc7755b9d.zip)模板相关的文件也包含在 `template_reference/` 目录下。

> [!WARNING]
> 学校发布的模板中，部分样例与格式要求不符，因此参考了往届论文。为了视觉效果，部分内容经过调整，可能和学校提供的样例略有差异，但整体风格和格式要求保持一致。

### 参考项目

- [Gitee NEUCloudLab/NEU论文Latex模板](https://gitee.com/NEUCloudLab/NEU-dissertation-template) — 模板源码重构基础
- [GitHub sci-m-wang/NEU-Thesis](https://github.com/sci-m-wang/NEU-Thesis) — 部分内容参考

## 补充模板接口

### 表注

在表体之后使用 `\neutabnote{说明文字}`，自动输出“注：”，采用五号字并在与表体同宽的居中区域内左对齐。支持 table/table* 中的 tabular、tabular*、tabularx；不将此接口视为跨页 longtable 表注。测试见 `tests/table-note.tex`。


### 算法接口

模板加载 algorithm、algorithmic 并按章编号。使用 `\begin{neualgorithm}[!htbp]{alg:example}{算法标题}`，环境内直接写 `\STATE` 等伪代码，最后 `\end{neualgorithm}`；通过 `\neualgref{alg:example}` 引用。接口自动提供算法标题、标签和行号。


### 从摘要开始

文档类选项 `start-at-abstract` 跳过封面、题名页和独创性声明，保留中英文摘要与目录。`no-frontmatter` 仍跳过全部前置页，同时启用时以后者为准。默认模式不变。


### 段落式自动编号

`thesispoints` 使用中文括号编号（1），`thesispointsen` 使用英文括号编号 (1)。环境内以 `\item` 分项，首行缩进，续行保持正文宽度，适用于贡献与结论条目。

## License

GPL-2.0 License，详见 [LICENSE](LICENSE) 文件。
