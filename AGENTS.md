# AGENTS.md - LaTeX プロジェクト開発フロー

このプロジェクトは LaTeX 文書の作成・管理を行うディレクトリです。

## プロジェクト構造

```
tex/
├── 一般LATEX/        # 一般的な LaTeX 文書
├── 三年春実験/       # 実験レポート
├── 簡易LATEX2/       # 簡易 LaTeX テンプレート
├── 簡易latex/        # 簡易 LaTeX 文書
└── .claude/          # Claude Code 設定
    ├── memory/       # セッション記録
    └── state/        # 状態管理
```

## 開発フロー（Solo モード）

### 基本コマンド

| コマンド | 説明 |
|---------|------|
| `/plan-with-agent` | 新しい作業を計画 |
| `/work` | Plans.md のタスクを実行 |
| `/sync-status` | 現在の状態を確認 |
| `/harness-review` | 作業をレビュー |

### よく使うフレーズ

- 「新しい文書を作って」→ LaTeX テンプレートを生成
- 「コンパイルして」→ pdflatex/lualatex でビルド
- 「BibTeX を通して」→ 参考文献を処理
- 「フォーマットして」→ latexindent で整形

## LaTeX 関連ツール

| ツール | 用途 |
|-------|------|
| `pdflatex` | 基本的な PDF 生成 |
| `lualatex` | 日本語対応 PDF 生成 |
| `bibtex` / `biber` | 参考文献処理 |
| `latexmk` | 自動ビルド |
| `latexindent` | コードフォーマット |

## マーカー凡例

| マーカー | 状態 | 説明 |
|---------|------|------|
| `cc:TODO` | 未着手 | Claude Code が実行予定 |
| `cc:WIP` | 作業中 | Claude Code が実装中 |
| `cc:完了` | 完了 | タスク完了 |
| `cc:blocked` | ブロック中 | 依存タスク待ち |
