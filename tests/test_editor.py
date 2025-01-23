import pytest
from notes_app.main import TextEditor
from tkinter import Tk
from pathlib import Path

@pytest.fixture
def editor():
    root = Tk()
    editor = TextEditor(root)
    yield editor
    root.destroy()

def test_new_file(editor):
    editor.new_file()
    assert editor.text_area.get(1.0, 'end-1c') == "" 

def test_save_file(editor, tmp_path):
    test_content = "Hello, World!"
    test_file = tmp_path / "test.txt"
    editor.text_area.insert(1.0, test_content)
    editor.filename = str(test_file)
    editor.save_file()
    assert test_file.read_text() == test_content

def test_open_file(editor, tmp_path):
    test_content = "Test content"
    test_file = tmp_path / "test.txt"
    test_file.write_text(test_content)
    editor.filename = str(test_file)
    editor.open_file()
    assert editor.text_area.get(1.0, 'end-1c') == test_content

def test_cut_copy_paste(editor):
    test_text = "Test text"
    editor.text_area.insert(1.0, test_text)
    editor.text_area.tag_add('sel', '1.0', 'end')
    editor.cut()
    assert editor.text_area.get(1.0, 'end-1c') == ""
    editor.paste()
    assert editor.text_area.get(1.0, 'end-1c') == test_text 