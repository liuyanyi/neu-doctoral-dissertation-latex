# 模板测试与维护

所有测试专用内容集中在本目录，命令从仓库根目录执行。公开模板示例仍为 `main.tex` 和各章节；学校原始 Word 资料仍在 `template_reference/`。

| 位置 | 用途 |
| --- | --- |
| `run.py` | 本地统一入口；CI 用 `--prepare-only` 准备用例 |
| `config/cases.json` | 唯一编译用例清单，本地、2023 CI 和 PDF 检查共用 |
| `cases/` | 版本探针、8 个回归样例及专用 BibTeX 数据 |
| `tools/` | PDF 检查、视觉比较和学术学位入口生成工具 |
| `config/pdf_compare_cases.json` | 5 项视觉对比配置 |
| `fixtures/reference-pages/` | 从学校样例提取的对比 PDF 页面 |
| `baseline/` | 已接受的视觉指标与叠加图；不自动刷新 |
| `archive/visual-comparisons/` | 早期对比图，仅供追溯，不参与判定 |
| `docs/migration-2026-09.md` | 历史迁移与验证记录，旧命令不作为当前入口 |
| `build/` | 被 Git 忽略的全部运行产物、临时入口、日志与报告 |

## 本地回归

需要可用的 XeLaTeX、latexmk 和 Python 3.10+。测试依赖与模板编译依赖分别管理：

```bash
python -m pip install -r tests/requirements.txt
python tests/run.py
python tests/tools/run_pdf_compare.py --check-baseline
```

第一条测试命令编译清单中的 11 项：版本探针、专业与学术学位完整示例、引用间距、表格字号与实验性图题、两种题注/正文起始模式、网页日期、签名布局、浮动体间距和表注。失败样例不会阻止剩余样例执行；任一编译失败、未解析引用或 PDF 断言失败都会使整体返回非零。

默认输出为 `tests/build/regression/<用例>/`，汇总在 `results.tsv`、`checks.json`、`summary.md`；不会更新根目录 `main.pdf`。`--output` 可以指定独立运行目录。视觉比较默认读取这组输出，并将结果写入 `tests/build/pdf-compare/`；使用自定义编译输出时，相应通过 `--config` 指定对比输入。

单项排错示例（测试入口中的相对路径均相对于仓库根目录）：

```bash
latexmk -xelatex -halt-on-error -outdir=tests/build/single/table-font tests/cases/table-font.tex
```

`table-font` 保留 `phase-III`，覆盖字号作用域、旧版 tabularx 试排标记、连续 `[H]` 图表题、独立父结构及普通浮动图题。`signature-layout` 检查不同尺寸签名不改变文本坐标。两份 `frontmatter-caption` 检查单页正文、隐藏前置页及实际字号；`webpage-date` 检查年份与访问日期次数。通过这些检查不等于 PDF/UA 合规认证。

新增用例时，把输入放入 `cases/`，在 `config/cases.json` 注册；如有新的 PDF 不变量，在 `tools/check_compatibility_pdfs.py` 添加检查。无需再在工作流中复制一份用例列表。

## 视觉基线

`config/pdf_compare_cases.json` 覆盖封面、声明页、中英文题名页及两种学位模式。判定使用 `baseline/diff_metrics.json` 的窗口：`changed_percent` 为 ±0.05，`mean_abs_diff` 为 ±0.1；保留原有指标及容差。叠加图供人工检查，不以 Word 页面与 LaTeX 页面像素完全相同为目标。

确认排版改变可以接受、实际查看新旧对照后，才显式更新基线：

```bash
python tests/run.py
python tests/tools/run_pdf_compare.py --check-baseline
# 审阅对比图之后执行，并单独审阅/提交 baseline 的差异
python tests/tools/run_pdf_compare.py --update-baseline
```

单页工具为 `tests/tools/compare_pdf_visual.py`，参数见 `--help`；输出也应放在 `tests/build/` 下。

## CI 与已验证环境

GitHub 要求工作流位于 `.github/workflows/`，这里只保留平台调度；测试定义、检查逻辑和数据均在 `tests/`。

- **TeX Live 2023 Compatibility**：手动触发固定摘要的历史容器。宿主机准备共享清单，容器内使用真实 2023 引擎编译，宿主机检查 PDF；不更新历史宏包、不套用 2026 像素基线。输出在 `tests/build/texlive-2023/`，artifact 保留 14 天。
- **PDF Compare**：执行统一回归，再检查 5 项视觉基线；`update_baseline=true` 仅生成供审阅的产物，不自动修改仓库基线。
- **Build**：单独编译公开 `main.tex` 示例。
- **Release**：依据 `.github/release-include.txt` 打包公开模板；测试目录不在发布包中。

2026-10-29，提交 `79a6e24` 的 [真实 TeX Live 2023 检查](https://github.com/liuyanyi/neu-doctoral-dissertation-latex/actions/runs/40830800143) 为 **11/11 通过**。Windows / TeX Live 2026 同样通过回归及 5 项视觉基线；Overleaf 的历史验证不代表本版本已复测。2023 CI 成功记录针对所链接的提交，测试管理重构后的工作流需以新的运行结果为准。
