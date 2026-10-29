# 模板回归样例

从仓库根目录执行（输出目录已被 Git 忽略）：

```powershell
latexmk -xelatex -interaction=nonstopmode -halt-on-error -outdir=tests/build tests/reference-spacing.tex
latexmk -xelatex -interaction=nonstopmode -halt-on-error -outdir=tests/build tests/table-font.tex
latexmk -xelatex -interaction=nonstopmode -halt-on-error -outdir=tests/build tests/frontmatter-caption.tex
latexmk -xelatex -interaction=nonstopmode -halt-on-error -outdir=tests/build tests/frontmatter-caption-plain.tex
latexmk -xelatex -interaction=nonstopmode -halt-on-error -outdir=tests/build tests/webpage-date.tex
latexmk -xelatex main.tex
```

`reference-spacing` 对比真实引用与直接排印编号的宽度，覆盖中文、标点、空格、分组、子图和公式；需要 latexmk 完成引用解析后的编译。`table-font` 在各环境内断言字号，并检查局部覆盖、环境外恢复及独立 tabular、figure 不受影响。

两份 `frontmatter-caption` PDF 均应只有一页，正文页码为 1，不出现 `OMITTED-CN` / `OMITTED-EN`。检查两种模式中中文图表题（含编号）、英文题名和表内文字均为 10.5 bp，正文为 12 bp。`webpage-date` 中带出版者的第一条只应出现一次 2024；无出版者的第二条保留 2023；两条均保留访问日期。

## 2026-09-09 迁移依据

来源为 `D:/codes/final-paper` 当日工作区的 `neudissertation.cls`、2025 版 BST 及两份原有测试。仅迁入模板实现与测试，论文内容和个人配置不在迁移范围内。

- 题注：session `01a079ce-4823-7013-9b23-c7b8c9ab938e`（2026-09-07）。用户实测中文图题为 12 bp、英文为 10.5 bp；最终要求兼容 `DocumentMetadata`。保留最终 hook/socket 方案，不采用记录中已放弃的替换题注函数或移除元数据方案。
- 引用：session `01a0803d-5515-76a1-b6a5-9e470f82567c`（2026-09-08）。hyperref 结束链接节点遮蔽 xeCJK 的西文边界；恢复边界节点后，中文自动加间距、标点保持原有处理。
- 表内字号：session `01a08546-6462-74a3-8fc0-05aa43a7c3f4`（2026-09-09）。用户要求将默认五号放入模板；字体设置放在浮动体字体重置之后，并覆盖 longtable。
- `no-frontmatter`：依据来源类文件中的审阅用途说明迁入；当前可检索 session 未找到最初实现对话。摘要通过丢弃盒子隐藏，因此仍处理其内容。
- 网页年份：来源提交 `947cc54e5663357ce9231cb4f8654b2c72ed052a` 中的 BST 补丁。当前可检索 session 未找到最初讨论；从代码可确认网页已有创建/修改日期输出，删除出版者分支中额外的 `format.date`，并用带/不带出版者的样例验证。

本次运行环境为 TeX Live 2026；不将本机验证视为其他 TeX Live 版本已经复测。

验证结果：上述五个回归样例和 39 页 `main.pdf` 编译成功，`git diff --check` 通过。通过 PDF 文字对象核实两种题注模式的五号字号、单页审阅输出和网页年份次数；目视检查两份题注测试及主文档 PDF 第 15–21 页。主文档没有未解析引用或 Overfull/Underfull 提示，仍有 tagpdf 的 XeTeX 支持提示、xeCJK robust 提示及未设置元数据语言的提示。
