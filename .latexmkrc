# ============================================================
# .latexmkrc - LaTeX Workshop + XeLaTeX 编译配置
# 用于东北大学博士论文模板
# ============================================================

# --- 引擎配置 ---
# 使用 XeLaTeX（pdf_mode=5），选项直接嵌入引擎命令中，
# 避免通过 latexmk 转发时丢失参数，导致变更检测失效。
$pdf_mode = 5;
$xelatex = 'xelatex -synctex=1 -interaction=nonstopmode -file-line-error %O %S';

# --- 参考文献 ---
$bibtex = 'bibtex %O %S';
$biber = 'biber %O %B';

# --- 变更检测增强 ---
# 忽略 PDF/EPS 元数据中的 CreationDate（避免因元数据变化误判文件修改）
$hash_calc_ignore_pattern{'eps'} = '^%%CreationDate: ';
$hash_calc_ignore_pattern{'pdf'} = '^%%CreationDate: ';

# --- 自动清理的临时文件扩展名 ---
$clean_ext = 'acn acr alg aux bbl blg fdb_latexmk fls glg glo gls ist lof log lot nav out run.xml snm synctex.gz toc vrb xdv';
