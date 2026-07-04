# VS Code 与 LaTeX Workshop 补全

本仓库提供了一组面向普通模板使用者的 VS Code 配置，用来改善 LaTeX Workshop 中的模板命令补全和常用结构输入体验。

LaTeX Workshop 是编辑器扩展，不是 TeX 引擎。它可以读取常见宏包和部分项目命令，但对本模板自定义命令、环境和 `\neudisetup` 字段不一定总能自动识别。因此，本仓库通过以下文件补充用户侧提示：

- `.vscode/settings.json`：为 LaTeX Workshop 增加模板公开命令补全。
- `.vscode/neu-template.code-snippets`：提供摘要、图、表、公式、参考文献等结构片段。
- `.vscode/extensions.json`：推荐安装 LaTeX Workshop 扩展。

这些配置只帮助输入模板接口，不负责论文内容写作，也不会改变模板排版效果。

## 使用方式

用 VS Code 打开仓库根目录后，在 `.tex` 文件中输入触发前缀即可看到补全候选。

常用结构片段包括：

- `neu-setup-basic`：插入基础 `\neudisetup{...}` 元数据骨架。
- `neu-abstract-cn`：插入中文摘要环境和 `\cnkeywords{...}`。
- `neu-abstract-en`：插入英文摘要环境和 `\enkeywords{...}`。
- `neu-chapter-input`：插入章节 `\input{...}`。
- `neu-figure`：插入单图结构和 `\neufigcaption{...}`。
- `neu-subfigures`：插入并列子图结构、`neusubfigure` 环境和子图题命令。
- `neu-table`：插入三线表结构和 `\neutabcaption{...}`。
- `neu-equation`：插入带 `\label{...}` 的公式结构和 `\neueqref{...}` 引用示例。
- `neu-references`：插入 `referencescn` 参考文献环境。
- `neu-achievements`：插入 `achievementscn` 学术成果环境。

模板命令补全还包括：

- `\makeneucovers`
- `\makeneudeclaration`
- `\neufigref{...}`
- `\neutabref{...}`
- `\neusubfigref{...}`
- `\upcite{...}`
- `\inlinecite{...}`

公开命令、环境和字段名来自 README 示例与当前模板实现。若后续模板接口发生变化，请以 README 示例和当前模板实现为准。

## 补全没有出现时

可以按顺序检查：

1. 确认已安装 LaTeX Workshop 扩展。
2. 确认是以本仓库根目录打开 VS Code，而不是只打开单个 `.tex` 文件。
3. 重新加载 VS Code 窗口。
4. 确认当前文件语言模式是 LaTeX。
5. 确认工作区信任已开启。

这些 snippets 只插入结构骨架。摘要正文、章节内容、图题表题、公式含义和参考文献信息仍需要作者自行填写。
