# Notebook to HTML Converter

This script converts Jupyter Notebook files (`.ipynb`) to HTML files, with the tab name (`<title>`) automatically set to the file name.

## Features
- Converts Jupyter Notebook to HTML.
- Automatically sets the HTML `<title>` to match the Notebook file name.
- Output file is saved in the same directory as the input file.

## Requirements
- Python 3.x
- `nbconvert` and `nbformat` modules

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/notebook-html-converter.git
   cd notebook-html-converter
   ```
2. Install dependencies:
   ```bash
   pip install nbconvert nbformat
   ```

## Usage
Run the script with the following command:

```bash
python notebook_to_html.py <input_notebook_path>
```

### Example
```bash
python notebook_to_html.py example_notebook.ipynb
```

The converted HTML file will be saved in the same directory as the input Notebook with the `.html` extension.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing
Feel free to fork this repository, submit pull requests, or report issues.
