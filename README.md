# Text Editor

A simple sticky note text editor built with Python and Tkinter.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.6%2B-blue)

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Development](#development)
- [Contributing](#contributing)
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

## Installation

### Method 1: Using pip

pip install notes-app


### Method 2: From source

1. Clone the repository
bash
git clone https://github.com/yonDest/Text-Editor.git
cd Text-Editor

2. Create and activate a virtual environment
bash
On macOS/Linux
python -m venv venv
source venv/bin/activate
On Windows
python -m venv venv
venv\Scripts\activate


3. Install the package
bash
pip install -e .


## Usage

### Running from command line
After installation, you can run the text editor using:

bash
notepad


### Running from Python

python
from notes_app.main import main
main()


### Keyboard Shortcuts
- `Ctrl + N`: New file
- `Ctrl + O`: Open file
- `Ctrl + S`: Save file
- `Ctrl + Shift + S`: Save as
- `Ctrl + C`: Copy
- `Ctrl + X`: Cut
- `Ctrl + V`: Paste
- `Ctrl + Z`: Undo
- `Ctrl + Y`: Redo

## Development

### Setting up development environment

1. Clone the repository
bash
git clone https://github.com/yonDest/Text-Editor.git
cd Text-Editor

2. Create and activate virtual environment
bash
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate


3. Install development dependencies
bash
pip install -e ".[dev]"


### Running tests
bash
pytest




