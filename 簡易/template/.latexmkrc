# 簡易レポート用 latexmkrc（参照文献なし・高速ビルド）

# LuaLaTeX を使用（pdf_mode=4）
$pdf_mode = 4;
$lualatex = 'lualatex -synctex=1 -interaction=nonstopmode -halt-on-error -file-line-error %O %S';

# 参照なしのため少ない回数で十分
$max_repeat = 2;

# BibTeX 完全無効
$bibtex_use = 0;

# 対象ファイル
@default_files = ('*.tex');

# 中間ファイルクリーンアップ
$clean_ext = 'aux bbl blg fdb_latexmk fls log out toc synctex.gz';

# プレビュー設定
$pvc_view_file_via_temporary = 0;
$preview_continuous_mode = 0;
$pdf_update_method = 0;

# 高速化設定
$silent = 1;
$recorder = 1;
$go_mode = 1;

# OS別プレビューア
if ($^O eq 'linux') {
    $pdf_previewer = "xdg-open %S";
} elsif ($^O eq 'darwin') {
    $pdf_previewer = "open %S";
} else {
    $pdf_previewer = "cmd /c start \"\" \"%S\"";
}
