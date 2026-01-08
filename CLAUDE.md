# CLAUDE.md - LaTeX プロジェクト設定

## プロジェクト概要

- **種類**: LaTeX 文書管理ディレクトリ
- **言語**: 日本語
- **モード**: Solo（Claude Code のみ）

## ディレクトリ構造

| ディレクトリ | 内容 |
|-------------|------|
| `一般LATEX/` | 一般的な LaTeX 文書 |
| `三年春実験/` | 実験レポート |
| `簡易LATEX2/` | 簡易 LaTeX テンプレート |
| `簡易latex/` | 簡易 LaTeX 文書 |

## LaTeX コンパイル手順

### 基本的なコンパイル

```bash
# pdflatex（欧文向け）
pdflatex document.tex

# lualatex（日本語対応）
lualatex document.tex

# 参考文献付き（完全ビルド）
lualatex document.tex
bibtex document
lualatex document.tex
lualatex document.tex
```

### 自動ビルド（latexmk）

```bash
# PDF 生成（lualatex）
latexmk -lualatex document.tex

# クリーン
latexmk -c
```

## コーディング規約

### LaTeX スタイル

- インデント: 2スペース
- 1行は80文字以内を推奨
- セクション間は空行を入れる
- コメントは日本語可

### ファイル命名

- 日本語ファイル名可
- スペースは避ける（`_` を使用）
- 拡張子: `.tex`, `.bib`, `.sty`, `.cls`

## メモリ管理

- セッションログ: `.claude/memory/session-log.md`
- 意思決定記録: `.claude/memory/decisions.md`
- 再利用パターン: `.claude/memory/patterns.md`

## 注意事項

- 日本語文書は lualatex を使用
- BibTeX より biber を推奨（日本語対応）
- aux, log, synctex.gz などの中間ファイルは .gitignore に追加
