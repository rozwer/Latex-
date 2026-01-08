# Plans.md - LaTeX プロジェクト タスク管理

## 🎯 プロジェクト: LaTeX 環境整備

### 概要
- **目的**: 3種類のレポートタイプに応じた LaTeX 環境の整備と自動化
- **対象**: 個人利用（学術・レポート）
- **スコープ**: 設定ファイル最適化、ディレクトリ構成、Python スクリプト作成

---

## ✅ 完了したタスク

### フェーズ1: 環境整備
- [x] biber, latexindent のインストール確認 `cc:完了`
  - ⚠️ 手動インストール必要: `sudo apt install biber texlive-extra-utils`

### フェーズ2: ディレクトリ構造作成
- [x] 簡易/ ディレクトリ作成 `cc:完了`
- [x] レポート/ ディレクトリ作成 `cc:完了`
- [x] 実験レポート/ ディレクトリ作成 `cc:完了`

### フェーズ3-5: 設定ファイル作成
- [x] 簡易/ の設定ファイル作成 `cc:完了`
- [x] レポート/ の設定ファイル作成 `cc:完了`
- [x] 実験レポート/ の設定ファイル作成 `cc:完了`

### フェーズ6-7: Python スクリプト作成
- [x] setup_subject.py 作成（3フォルダ全て）`cc:完了`
- [x] new_report.py 作成（3フォルダ全て）`cc:完了`

---

## 📁 新規作成したディレクトリ構造

```
tex/
├── 簡易/                      # 参照なし簡易レポート
│   ├── template/
│   │   ├── .latexmkrc         # BibTeX無効、1回コンパイル
│   │   ├── preamble.tex       # 最適化済みプリアンブル
│   │   ├── variables.tex      # 変数定義
│   │   ├── template.tex       # テンプレート本体
│   │   └── .vscode/settings.json
│   ├── setup_subject.py       # 科目フォルダ作成
│   └── new_report.py          # レポートファイル作成
│
├── レポート/                   # 参照ありレポート
│   ├── template/
│   │   ├── .latexmkrc         # biber有効、5回コンパイル
│   │   ├── preamble.tex       # biblatex + cleveref
│   │   ├── variables.tex
│   │   ├── template.tex
│   │   ├── references.bib     # 参考文献サンプル
│   │   └── .vscode/settings.json
│   ├── setup_subject.py
│   └── new_report.py
│
└── 実験レポート/               # 実験の詳細なレポート
    ├── template/
    │   ├── .latexmkrc         # biber + minted（-shell-escape）
    │   ├── preamble.tex       # minted + algorithm2e + tcolorbox
    │   ├── variables.tex      # 実験用変数（班、共同実験者等）
    │   ├── template.tex       # 実験レポートテンプレート
    │   ├── references.bib
    │   └── .vscode/settings.json
    ├── setup_subject.py
    └── new_report.py
```

---

## 🚀 使い方

### 1. 新しい科目フォルダを作成

```bash
cd 簡易/          # または レポート/ または 実験レポート/
python setup_subject.py 線形代数
```

結果:
```
簡易/
├── 線形代数/
│   ├── .latexmkrc
│   ├── preamble.tex
│   ├── variables.tex
│   ├── template.tex
│   ├── .vscode/settings.json
│   └── new_report.py
└── ...
```

### 2. 新しいレポートを作成

```bash
cd 簡易/線形代数/
python new_report.py 課題1
```

結果:
```
簡易/線形代数/
├── 課題1.tex      # 新規作成
├── template.tex
└── ...
```

### 3. コンパイル

```bash
latexmk 課題1.tex
```

または VS Code で保存時に自動コンパイル。

---

## 📊 3タイプの比較

| 項目 | 簡易 | レポート | 実験レポート |
|-----|------|---------|-------------|
| **用途** | 簡単な課題 | 参照文献あり | 詳細な実験レポート |
| **BibTeX** | なし | biber | biber |
| **コンパイル回数** | 1回 | 5回 | 5回 |
| **追加機能** | - | cleveref | minted, algorithm2e, tcolorbox |
| **-shell-escape** | 不要 | 不要 | 必要 |

---

## ⚠️ 手動で必要な作業

### パッケージインストール（未実行）

```bash
sudo apt install biber texlive-extra-utils
```

### 既存フォルダについて

以下のフォルダは編集していません（既存のまま）:
- 簡易latex/
- 一般LATEX/
- 簡易LATEX2/
- 三年春実験/

---

## 🔜 今後のタスク（オプション）

- [ ] 各タイプでサンプル文書のコンパイルテスト
- [ ] 既存フォルダから新フォルダへの移行
- [ ] Makefile の追加（latexmk の代替）
