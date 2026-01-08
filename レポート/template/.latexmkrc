# レポート用 latexmkrc（参照文献あり・biber使用）

# LuaLaTeX を使用（pdf_mode=4）
$pdf_mode = 4;
$lualatex = 'lualatex -synctex=1 -interaction=nonstopmode -halt-on-error -file-line-error %O %S';

# 参照解決のため複数回コンパイル
$max_repeat = 5;

# biber を使用（biblatex用）
$bibtex_use = 2;
$biber = 'biber %O %S';

# 対象ファイル
@default_files = ('*.tex');

# 中間ファイルクリーンアップ
$clean_ext = 'aux bbl bcf blg fdb_latexmk fls log out toc run.xml synctex.gz';

# プレビュー設定
$pvc_view_file_via_temporary = 0;
$preview_continuous_mode = 0;
$pdf_update_method = 0;

# 出力設定
$silent = 1;
$recorder = 1;

# OS別プレビューア
if ($^O eq 'linux') {
    $pdf_previewer = "xdg-open %S";
} elsif ($^O eq 'darwin') {
    $pdf_previewer = "open %S";
} else {
    $pdf_previewer = "cmd /c start \"\" \"%S\"";
}
