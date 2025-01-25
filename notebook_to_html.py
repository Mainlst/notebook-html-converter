import argparse
import os
from nbconvert import HTMLExporter
import nbformat

def convert_notebook_to_html(input_path):
    # Notebook ファイルを読み込む
    with open(input_path, 'r', encoding='utf-8') as f:
        notebook = nbformat.read(f, as_version=4)

    # HTML に変換
    html_exporter = HTMLExporter()
    html_data, _ = html_exporter.from_notebook_node(notebook)

    # 出力パスを決定 (入力ファイルと同じディレクトリに .html を作成)
    output_path = os.path.splitext(input_path)[0] + ".html"

    # HTML ファイルとして保存
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_data)

    print(f"Notebook を HTML に変換しました: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert Jupyter Notebook to HTML.")
    parser.add_argument("input", help="Input path to the Jupyter Notebook file (.ipynb).")

    args = parser.parse_args()

    convert_notebook_to_html(args.input)
