# 更新日志

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
