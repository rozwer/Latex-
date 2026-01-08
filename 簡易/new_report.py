#!/usr/bin/env python3
"""
レポートファイル作成スクリプト

使い方:
    python new_report.py [レポート名]

例:
    python new_report.py 課題1
    python new_report.py "第1回レポート"
"""

import os
import shutil
import sys
from pathlib import Path


def new_report(report_name: str) -> None:
    """テンプレートをコピーして新しいレポートファイルを作成する"""

    # スクリプトのあるディレクトリを基準にする
    current_dir = Path(__file__).parent

    # テンプレートファイルを探す
    template_file = current_dir / "template.tex"

    if not template_file.exists():
        print(f"エラー: テンプレートファイルが見つかりません: {template_file}")
        sys.exit(1)

    # 新しいファイル名
    new_file = current_dir / f"{report_name}.tex"

    # ファイルが既に存在する場合
    if new_file.exists():
        print(f"エラー: ファイルが既に存在します: {new_file}")
        response = input("上書きしますか？ (y/N): ").strip().lower()
        if response != 'y':
            print("キャンセルしました")
            sys.exit(0)

    # テンプレートをコピー
    shutil.copy2(template_file, new_file)
    print(f"✅ 作成: {new_file}")

    print(f"\n🎉 完了！")
    print(f"\n次のステップ:")
    print(f"  1. {new_file} を編集")
    print(f"  2. variables.tex で情報を設定")
    print(f"  3. latexmk {report_name}.tex でコンパイル")


def main():
    if len(sys.argv) < 2:
        # 対話モード
        report_name = input("レポート名を入力してください: ").strip()
        if not report_name:
            print("エラー: レポート名を入力してください")
            sys.exit(1)
    else:
        report_name = sys.argv[1]

    # .tex 拡張子が付いていたら除去
    if report_name.endswith('.tex'):
        report_name = report_name[:-4]

    new_report(report_name)


if __name__ == "__main__":
    main()
