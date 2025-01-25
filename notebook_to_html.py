import argparse
import os
from nbconvert import HTMLExporter
import nbformat


def convert_notebook_to_html(input_path, output_dir):
    """
    Convert a single Jupyter Notebook file to HTML and save it to a specified directory.

    Args:
        input_path (str): Path to the Jupyter Notebook file.
        output_dir (str): Path to the directory where the HTML file will be saved.
    """
    # Notebook ファイルを読み込む
    with open(input_path, "r", encoding="utf-8") as f:
        notebook = nbformat.read(f, as_version=4)

    # HTML に変換
    html_exporter = HTMLExporter()
    html_data, _ = html_exporter.from_notebook_node(notebook)

    # 出力パスを決定
    file_name = os.path.splitext(os.path.basename(input_path))[0] + ".html"
    output_path = os.path.join(output_dir, file_name)

    # HTML ファイルとして保存
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_data)

    print(f"Notebook を HTML に変換しました: {output_path}")


def process_directory(directory_path):
    """
    Process all .ipynb files in the specified directory (non-recursively) and save HTML files in an 'html' subdirectory.

    Args:
        directory_path (str): Path to the directory.
    """
    if not os.path.isdir(directory_path):
        print(f"無効なディレクトリです: {directory_path}")
        return

    # HTML サブディレクトリを作成
    output_dir = os.path.join(directory_path, "html")
    os.makedirs(output_dir, exist_ok=True)

    # 指定されたディレクトリ内のファイルのみ取得
    for file in os.listdir(directory_path):
        file_path = os.path.join(directory_path, file)
        if os.path.isfile(file_path) and file.endswith(".ipynb"):
            convert_notebook_to_html(file_path, output_dir)


def main(paths):
    """
    Process files or directories.

    Args:
        paths (list): List of paths to files or directories.
    """
    for path in paths:
        if os.path.isfile(path) and path.endswith(".ipynb"):
            # 単一ファイルの場合、親ディレクトリに 'html' サブディレクトリを作成
            parent_dir = os.path.dirname(path)
            output_dir = os.path.join(parent_dir, "html")
            os.makedirs(output_dir, exist_ok=True)
            convert_notebook_to_html(path, output_dir)
        elif os.path.isdir(path):
            # 指定ディレクトリの場合
            process_directory(path)
        else:
            print(f"無効なパスをスキップしました: {path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Convert Jupyter Notebooks or directories containing notebooks to HTML."
    )
    parser.add_argument(
        "paths",
        nargs="+",
        help="Paths to one or more Jupyter Notebook files (.ipynb) or directories.",
    )

    args = parser.parse_args()
    main(args.paths)
