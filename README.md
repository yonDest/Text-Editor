# Text Editor

A simple sticky note text editor built with Python and Tkinter.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.6%2B-blue)

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Development](#development)
- [License](#license)
- [Author](#author)

## Features

- **Rich text editing capabilities**: Edit text with various formatting options.
- **Font customization**: Change font family and size.
- **Text formatting**: Apply bold and italic styles.
- **Color customization**: Customize text and background colors.
- **File operations**: Create, open, save, and save files as new.
- **Print functionality**: Print documents directly from the editor.
- **Keyboard shortcuts**: Efficiently perform actions with shortcuts.
- **Undo/Redo support**: Easily revert or reapply changes.
- **Sticky Notes**: Create and manage multiple sticky notes.

## Installation

### From PyPI
```bash
pip install notes-app
```
### From Source
1. Clone the repository
```bash
git clone https://github.com/yonDest/Text-Editor.git
cd Text-Editor
```

2. Create and activate a virtual environment
```bash
# On macOS/Linux
python -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

3. Install the package and dependencies
```bash
pip install -e .
pip install pillow  # Required for icon support
```

## Usage

### Running the Application

After installation, you can run the text editor using:

```bash
notes-app
```

### Running from Python

```python
from notes_app.main import main
main()
```

### Features Guide

- **Creating a New File**: Click File → New or press `Ctrl + N`
- **Opening Files**: Click File → Open or press `Ctrl + O`
- **Saving Files**: Click File → Save or press `Ctrl + S`
- **Text Formatting**:
  - Bold: Select text and press `Ctrl + B`
  - Italic: Select text and press `Ctrl + I`
  - Change Font: Use the Format → Font menu
  - Change Color: Use the Format → Color menu

### Keyboard Shortcuts
- `Ctrl + N`: New file
- `Ctrl + O`: Open file
- `Ctrl + S`: Save file
- `Ctrl + Shift + S`: Save as
- `Ctrl + P`: Print
- `Ctrl + C`: Copy
- `Ctrl + X`: Cut
- `Ctrl + V`: Paste
- `Ctrl + Z`: Undo
- `Ctrl + Y`: Redo

## Development

### Setting up development environment

1. Clone the repository:
    ```bash
    git clone https://github.com/yonDest/Text-Editor.git
    cd Text-Editor
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install development dependencies:
    ```bash
    pip install -e ".[dev]"
    ```

### Running tests
```bash
pytest
```

## License

Copyright (c) 2024 Yoni Desta

This project is licensed under the MIT License. This means you can:
- Use the code commercially
- Modify the code
- Distribute the code
- Use the code privately

See the [LICENSE](LICENSE) file for full details.

## Author

**Yoni Desta**
- GitHub: [@yonDest](https://github.com/yonDest)
- Email: yonidesta9@gmail.com
- LinkedIn: [Yoni Desta](https://linkedin.com/in/yonidesta/)

### Contributing
Feel free to reach out if you'd like to:
- Report a bug
- Request a feature
- Submit a pull request
- Or, just to chat!

Your contributions are always welcome!

