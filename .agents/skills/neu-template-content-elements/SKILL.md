---
name: neu-template-content-elements
description: 东北大学博士学位论文 LaTeX 模板正文元素使用。用于普通模板使用者在正文中正确插入图片、单图、子图、表格、公式、双语图题表题、label、图表公式交叉引用、BibTeX 参考文献、句末上标引用 \upcite、正文型引用 \inlinecite，并避免手写图表公式编号或编辑生成的 .bbl。
---

# NEU 模板正文元素

## Purpose

帮助用户在正文中按模板接口插入图、子图、表格、公式、交叉引用和参考文献，避免手写编号或破坏模板统一格式。

## When to use

- 需要在章节文件中插入图片、并列图或可单独引用的子图。
- 需要写中英文图题、表题，或在正文中引用图、表、公式。
- 需要添加 BibTeX 文献条目并在正文中引用。
- 需要确认参考文献在 `main.tex` 文末如何输出。
- 需要排查图表编号、引用编号或文献编号写法是否规范。

## Key files

- `chapter0-guide.tex`：图、子图、表格、公式、算法和引用的集中示例。
- `chapter1.tex`、`chapter2.tex` 等：正文写作位置。
- `Figures/`：图片文件目录，示例包含 `oaspl_a.pdf`、`oaspl_b.pdf` 等。
- `references.bib`：BibTeX 文献条目文件，正文用条目 key 引用。
- `main.tex`：文末 `referencescn` 环境内使用 `\bibliography{references}` 输出参考文献。
- `README.md`：模板公开命令表和示例的优先参考。

## Rules

- 图题使用 `\neufigcaption{label}{中文图题}{English figure title}`，放在图片下方。
- 表题使用 `\neutabcaption{label}{中文表题}{English table title}`，放在表格上方。
- 需要单独引用子图时，使用 `neusubfigure` 环境和 `\neusubfigcaption{label}{中文子图题}`。
- 正文引用普通图或总图用 `\neufigref{label}`，引用子图用 `\neusubfigref{label}`，引用表格用 `\neutabref{label}`，引用公式用 `\neueqref{label}`。
- 公式编号由 `equation`、`align` 等数学环境和 `\label{...}` 生成，不要手写公式编号。
- 文献条目放在 `references.bib`，正文句末来源用 `\upcite{key}`，作为句子成分用 `\inlinecite{key}`。
- 文末参考文献放在 `main.tex` 的 `referencescn` 环境内，并调用 `\bibliography{references}`。
- 不要手写“图 1.1”“表 2.1”“式（3.1）”或参考文献编号；让 LaTeX 自动生成。
- 不要手动编辑生成的 `.bbl` 文件；文献内容应改 `references.bib`。
- label 建议带类型前缀，如 `fig:`、`tab:`、`eq:`、`chap:`，并保持全项目唯一。

## Workflow

1. 将图片文件放入 `Figures/`，优先使用 PDF 矢量图；截图或照片可用 PNG/JPG。
2. 在首次引用附近插入 `figure` 或 `table` 浮动体，优先使用 `[!htbp]`。
3. 写图表时同时给中文题名和英文题名；label 写在模板 caption 命令第一个参数中。
4. 在正文中用模板引用命令引用图、表、公式，不直接写编号。
5. 对需要编号的重要公式使用 `equation` 或 `align` 并添加 `\label{...}`；不需要编号的短公式可用行内数学或无编号环境。
6. 把新的 BibTeX 条目加入 `references.bib`，用条目 key 调用 `\upcite{...}` 或 `\inlinecite{...}`。
7. 确认 `main.tex` 文末保留 `referencescn` 环境和 `\bibliography{references}`。
8. 编译后检查是否有 `??`、`[?]`、未显示文献或图表题注位置异常；必要时完整重编译。

## Examples

单图：

```latex
\begin{figure}[!htbp]
  \centering
  \includegraphics[width=0.75\textwidth]{Figures/oaspl_a.pdf}
  \neufigcaption{fig:single-demo}{中文图题}{English figure title}
\end{figure}

如 \neufigref{fig:single-demo} 所示，图片应在正文中被引用。
```

子图：

```latex
\begin{figure}[!htbp]
  \centering
  \begin{neusubfigure}{0.49\linewidth}
    \includegraphics[width=\linewidth]{Figures/oaspl_c.pdf}
    \neusubfigcaption{fig:sub-demo-a}{子图中文题名}
  \end{neusubfigure}
  \hfill
  \begin{neusubfigure}{0.49\linewidth}
    \includegraphics[width=\linewidth]{Figures/oaspl_d.pdf}
    \neusubfigcaption{fig:sub-demo-b}{子图中文题名}
  \end{neusubfigure}
  \neufigcaption{fig:sub-demo}{并列子图中文总题名}{English caption for subfigures}
\end{figure}

总图见 \neufigref{fig:sub-demo}，两个子图分别见 \neusubfigref{fig:sub-demo-a} 和 \neusubfigref{fig:sub-demo-b}。
```

表格：

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

公式：

```latex
\begin{equation}
  E = mc^2
  \label{eq:energy}
\end{equation}

如 \neueqref{eq:energy} 所示，重要公式应设置标签并在正文中引用。
```

文献引用和文末参考文献：

```latex
已有研究讨论了相关问题\upcite{guo_2023_research}。
文献 \inlinecite{thakkar_2018_performance} 给出了系统性能评测案例。
```

```latex
\begin{referencescn}
  \bibliography{references}
\end{referencescn}
```

`references.bib` 中的条目示例：

```bibtex
@article{guo_2023_research,
  title = {能耗优化的神经网络轻量化方法研究进展},
  journal = {计算机学报},
  author = {{郭朝鹏} and {王馨昕} and {仲昭晋} and {宋杰}},
  year = {2023},
  pages = {85--102}
}
```

## Common mistakes

- 使用普通 `\caption` 后又手写英文题注：应优先使用 `\neufigcaption` 或 `\neutabcaption`。
- 图表没有在正文中引用：应在正文首次提到处使用 `\neufigref`、`\neutabref` 等命令。
- label 重名：引用会跳到错误对象或编号混乱，应保证 label 唯一。
- 把图片路径写成绝对路径：换电脑或 Overleaf 后容易失败，应使用 `Figures/...` 相对路径。
- 手动写“图 1.1”：章节增删后编号会错，应使用模板引用命令。
- 文献 key 写错或 `references.bib` 没有对应条目：引用会显示异常，检查 key 是否完全一致。
- 改了 `references.bib` 但参考文献不更新：运行完整 `latexmk -xelatex main.tex`，必要时先清理辅助文件。
- 手动改 `.bbl`：清理或重编译后会丢失，应改 `references.bib`。
