# 更新日志

## 2026-10-29 — v2026.10

从 `final-paper` 迁回通用模板修复与接口，各模块保留独立提交。

### 修复与排版调整

- 修复 2023 年实验性标记模式下 `[H]` 图表绕过浮动体结构初始化、导致图题父结构编号为空的兼容问题；为旧路径补齐结构与链接锚点，保留原位排版。增加连续 `[H]` 图表题、父结构独立性、普通浮动图题及交叉引用回归。真实 TeX Live 2023 远程复测待执行。

- 修复旧版 `tabularx` 在实验性 PDF 标记模式下试排重复创建结构的问题：仅对尚无原生支持且未加载 latex-lab 表格模块的版本，在试排期间暂停标记，正式排版继续保留标记。2023 远程复测待执行。

- 为实验性题注格式增加 socket 接口存在性判断：旧版 latex-lab 未提供 `caption/label` 时保留原有生成路径，在文档初始化结束后包装最终题注命令以设置五号字，避免2023版不支持通用命令钩子的错误；保留原题注生成和标记逻辑，并增加 `phase-III` 实际图题字号及作用域断言。2023远程复测待执行。

- 签名图片改为不占排版尺寸的叠加层，调整高度或宽高比不会移动签名标签、日期及声明正文。更新已接受的声明页叠加图和指标基线，其他页面基线及容差不变。
- 修复启用 `\DocumentMetadata` 时 titletoc 与 latex-lab 目录链接机制的兼容问题，并补充独创性声明、中英文摘要的独立跳转锚点。
- 统一修复 `\ref` 和 `\ref*` 的中西文边界间距，保留标点及显式空格处理。
- 英文图表题注的编号与标题之间由 `\quad` 改为普通空格。
- 采用 V2 浮动体间距：页首/页底浮动体与正文、相邻浮动体为 `12bp plus 2bp minus 2bp`；普通文中浮动体上下为 12bp/2bp，标题后为 0bp/6bp；`[H]` 上方为 11bp（标题后不重复叠加），下方不追加间距，并修复其后标题段前间距被抑制的问题。
- 图题上间距为 4bp，表题不额外添加 caption 下间距，双语表题结束后为 4bp；ruled 算法横线内侧留白为 3bp。章节标题、正文行距、段落和公式间距保持原设置。

### 新增接口

- `\neutabnote`：在 table/table* 内按 tabular、tabular*、tabularx 表体宽度排印五号、左对齐表注。
- `neualgorithm` / `\neualgref`：集中管理按章编号的算法标题、标签、行号及引用，模板加载 algorithm 和 algorithmic；同步更新示例入口和算法示例。
- `start-at-abstract`：跳过封面、题名页和声明，保留摘要及目录；同时启用 `no-frontmatter` 时以后者为准。
- `thesispoints` / `thesispointsen`：中英文括号自动编号，首行缩进、续行保持正文宽度。

### 验证与兼容性

- 新增手动触发的 TeX Live 2023 容器兼容性工作流，固定历史镜像摘要并检查实际引擎年份；保留引擎和宏包版本、各样例编译结果、日志与 PDF。该工作流不更新历史工具链、不应用2026像素基线，首次远程运行成功前不视为已验证2023兼容。

- 新增签名大小、浮动体间距和表注回归样例，扩展交叉引用间距检查；README 保留当前接口使用说明，版本变更集中于本日志。
- Windows / TeX Live 2026 下，原有5个回归样例和专业/学术学位示例编译通过；核实题注及表内字号、审阅页隐藏、网页年份与访问日期；5项 PDF 基线检查全部通过。
- 检查默认、摘要起始、正文起始及组合模式，验证目录跳转目标，并抽查签名、浮动体和新接口页面。保留 tagpdf、xeCJK 及未设置元数据语言的提示。
- 本版调整会影响图表留白和分页；旧版 TeX Live 与 Overleaf 尚未针对本版复测。浮动体内核补丁不匹配时明确报错。
- 未迁移论文项目的构建脚本、环境配置、编辑器工具、章节导出或图片文字转轮廓功能。

## 2026-09-09 — v2026.09

从 `final-paper` 项目迁回通用模板修复：

- 新增默认关闭的 `no-frontmatter` 文档类选项，审阅时省略封面、声明、摘要和目录。
- 表格环境默认使用五号字，支持局部覆盖并在结束后恢复外部字号。
- 兼容 `DocumentMetadata` / `latex-lab` 的题注排版，恢复五号字号及编号后的空格，保留其结构标记实现。
- 修复图、子图和表引用后接中文时的自动间距，同时保持标点间距。
- 修复 2025 版参考文献样式中带出版者的网页条目重复输出年份。
- 新增引用间距、表格字号、题注与审阅模式、网页日期回归样例。迁移依据和运行方式见 `tests/README.md`。

兼容性：支持从 `v2026.08.02` 直接升级到 `v2026.09`，无需迁移，现有论文源码可继续编译。`no-frontmatter` 默认关闭；表内未指定字号的文字改为默认五号，显式字号设置仍然生效。图表与正文的上下间距保持原设置。

验证：在 TeX Live 2026 下，五个回归样例及完整模板编译通过，并检查相关 PDF 页面；本次未重新验证其他 TeX Live 版本。

## 2026-08-28

- 新增参考文献国标版本选项，可通过文档类选项 `bibliography=2025`（默认）或 `bibliography=2015` 选择对应版本，并升级内置 gbt7714 样式。
- Release workflow 新增版本元数据检查：发布 tag 必须与 `neudissertation.cls` 中的版本和年月一致。
- Release workflow 新增更新日志检查：每次发布前，`CHANGELOG.md` 必须相对上一个 tag 有所更新。
- 升级兼容性：支持从 `v2026.08.01` 直接升级到 `v2026.08.02`。本次更新无需迁移，已有论文源码可继续编译。

## 2026-07-04

根据最近几个提交，补充编辑器支持、模板入口选项和发布包内容：

- 新增 VS Code / LaTeX Workshop 使用支持：推荐安装 LaTeX Workshop，并在 `.vscode/settings.json` 中补充模板公开命令的自动补全。
- 新增 `.vscode/neu-template.code-snippets`，提供 `neu-setup-basic`、`neu-setup-professional`、`neu-setup-blind`、`neu-figure`、`neu-subfigures`、`neu-table`、`neu-equation`、`neu-references` 等常用论文结构片段。
- 将 `professional-degree` 和 `final-cover` 调整为文档类开关，推荐写法分别为 `\documentclass[professional-degree]{neudissertation}` 和 `\documentclass[final-cover]{neudissertation}`；不再推荐在 `\neudisetup{...}` 中配置这两个全局模式。
- 更新 `main.tex` 示例、README 和 VS Code 补全文档，使学术学位、专业学位、盲审版和最终版封面的入口写法更加清晰。
- 更新 release 打包清单，发布包现在包含 `.vscode/neu-template.code-snippets`，便于下载压缩包后直接获得编辑器代码片段。
- 优化 Windows UTF-8 shell 技能文档，说明 PowerShell UTF-8 预处理脚本应按技能目录动态加载，避免中文内容读写或命令输出出现编码问题。

## 2026-07-03

补充模板使用说明和 Codex/Agents 辅助材料：

- 更新 README 和 `chapter0-guide.tex`，扩展正文写作、排版建议、模板公开命令、参考文献引用、图表公式与交叉引用说明。
- 新增并列子图支持：提供 `neusubfigure` 环境、`\neusubfigcaption` 和 `\neusubfigref`，支持按“图 x.y(a)”格式引用子图。
- 在示例章节中加入并列子图和 2x2 子图示例，说明总图题、子图题、浮动位置和图片尺寸的推荐写法。
- 新增 `.agents` 技能目录，包含快速开始、前置页配置、正文元素使用、编译检查和 Windows UTF-8 shell 等使用辅助说明。
- 更新 release 打包清单，将 `.agents` 目录纳入发布包。

## 2026-06-29

完善持续集成、PDF 对比和发布流程：

- 新增手动触发的 GitHub Actions：`Build` 用于编译 `main.tex`，`PDF Compare` 用于构建并对比专业学位和学术学位样例页面。
- 新增 `Release` workflow，按 `.github/release-include.txt` 打包模板源码、样例章节、字体样式、图片、README、LICENSE 和 CHANGELOG，并发布到 GitHub Release。
- 新增 `dev/run_pdf_compare.py`、`dev/pdf_compare_cases.json` 和 `dev/make_academic_entry.py`，用于批量生成 PDF 视觉对比结果和临时学术学位入口。
- 改进 CI 缓存：复用 TeX Live 包列表并缓存 apt 下载包，PDF 对比流程同时缓存 Python pip 依赖。
- 改进 PDF 对比摘要：在 artifact 中输出 diff、overlay、highlight、渲染页和指标文件，并在 GitHub Actions Step Summary 中汇总关键指标。
- 保留已接受的 PDF 对比 baseline，CI 阻断条件基于 `diff_metrics.json` 的指标窗口，而不是简单要求像素级完全一致。

## 2026-06-25

根据研究生院最新文件进行更新，共做出以下调整：

- 新增 `professional-degree` 配置项：通过 `\neudisetup{professional-degree=true/false}` 控制中文题名页右侧的字段标签。`true` 时显示"专业学位类别："，`false` 时显示"学科门类："。
- 调整最终版封面的风格并进行精细排版，顶部引入更清晰的图像Logo，下方日期居中
- 新增 `defense-chair-title` 配置项：可单独设置答辩委员会主席的职称，在封面中显示为"姓名 + 职称"格式
- 字体改进，通过FakeBold增加宋体的加粗支持
- 补充了新的参考材料和对比页面

## 初始版本

参照 2026 年 3 月，东北大学研究生院网站构建
