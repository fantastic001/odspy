# ODSPy

ODSPy is a Python library for parsing and working with OpenDocument Spreadsheet (ODS) files. It allows you to extract data from ODS files and manipulate it programmatically.

## Features

- Parse ODS files and extract sheet data.
- Access rows and cells with ease.
- Built-in support for XML parsing using `lxml`.

## Installation

You can install ODSPy using pip:

```bash
pip install odspy
```

## Usage

### Example: Reading an ODS File

```python
from odspy import ODSDocument

# Specify the path to the ODS file and the sheet name
path = "example.ods"
sheet = "Sheet1"

# Create an ODSDocument instance
document = ODSDocument(path, sheet)

# Access rows and cells
for row in document.rows:
    for cell in row:
        print(cell)
```

## Requirements

- Python 3.13 or higher
- `lxml` library

## Development

### Setting up the environment

1. Clone the repository.
2. Create a virtual environment:
   ```bash
   python3 -m venv env
   source env/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running Tests

Currently, there are no tests implemented.

## Distribution

To distribute the package, follow the instructions in the `distribute.sh` script.

## License

This project is licensed under the MIT License.