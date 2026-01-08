#!/usr/bin/env python3
"""
科目フォルダ作成スクリプト

使い方:
    python setup_subject.py [科目名]

例:
    python setup_subject.py 線形代数
    python setup_subject.py "データ構造とアルゴリズム"
"""

import os
import shutil
import sys
from pathlib import Path


def setup_subject(subject_name: str) -> None:
    """科目フォルダを作成し、テンプレートファイルをコピーする"""

    # スクリプトのあるディレクトリを基準にする
    base_dir = Path(__file__).parent
    template_dir = base_dir / "template"
    subject_dir = base_dir / subject_name

    # テンプレートディレクトリの存在確認
    if not template_dir.exists():
        print(f"エラー: テンプレートディレクトリが見つかりません: {template_dir}")
        sys.exit(1)

    # 科目フォルダが既に存在する場合
    if subject_dir.exists():
        print(f"エラー: フォルダが既に存在します: {subject_dir}")
        sys.exit(1)

    # 科目フォルダを作成
    subject_dir.mkdir(parents=True)
    print(f"✅ フォルダ作成: {subject_dir}")

    # コピーするファイル/ディレクトリ
    items_to_copy = [
        ".latexmkrc",
        "preamble.tex",
        "variables.tex",
        "template.tex",
        ".vscode",
    ]

    # 参照ファイルがあればコピー（レポート/実験レポート用）
    if (template_dir / "references.bib").exists():
        items_to_copy.append("references.bib")

    for item in items_to_copy:
        src = template_dir / item
        dst = subject_dir / item

        if src.exists():
            if src.is_dir():
                shutil.copytree(src, dst)
            else:
                shutil.copy2(src, dst)
            print(f"  📄 コピー: {item}")

    # new_report.py をコピー
    new_report_script = base_dir / "new_report.py"
    if new_report_script.exists():
        shutil.copy2(new_report_script, subject_dir / "new_report.py")
        print(f"  📄 コピー: new_report.py")

    print(f"\n🎉 完了！")
    print(f"\n次のステップ:")
    print(f"  1. cd {subject_dir}")
    print(f"  2. python new_report.py [レポート名]")
    print(f"  または template.tex を直接編集")


def main():
    if len(sys.argv) < 2:
        # 対話モード
        subject_name = input("科目名を入力してください: ").strip()
        if not subject_name:
            print("エラー: 科目名を入力してください")
            sys.exit(1)
    else:
        subject_name = sys.argv[1]

    setup_subject(subject_name)


if __name__ == "__main__":
    main()
