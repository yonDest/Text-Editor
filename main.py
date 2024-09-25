from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import colorchooser
from tkinter import ttk
import subprocess

root = Tk() 
root.geometry("500x525") 
root.title("Notes") 
root.minsize(height=250, width=350)


global open_status_name
open_status_name = False

global selected
selected = False



# New File
def new_file():
    # Delete previous text
    text_box.delete("1.0", END)
    # Update status bar
    root.title('New File - Editor')
    status_bar.config(text="New File   ")
    global open_status_name
    open_status_name = False

# Open File
def open_file():
    # Delete previous text
    text_box.delete("1.0", END)
    # Grab Filename
    text_file = filedialog.askopenfilename(title="Open File", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*")))
    # Check if file name exists
    if text_file:
        # Make filename accessible
        global open_status_name
        open_status_name = text_file
    # Update status bars
    name = text_file
    status_bar.config(text=f'{name}   ')
    # Open the file
    text_file = open(text_file, 'r')
    content = open_file.read()
    text_box.insert(END, content)
    text_file.close()

# Save As File
def save_as_file():
    text_file = filedialog.asksaveasfilename(defaultextension=".*", title="Save File", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*")))
    if text_file:
        # Update status bars
        name = text_file
        root.title(f'{name} - Editor')
        status_bar.config(text=f'Saved {name}   ')
    # Save the file
    text_file = open(text_file, 'w')
    text_file.write(text_box.get(1.0, END))
    # Close the file
    text_file.close()

# Save the file
def save_file():
    global open_status_name
    if open_status_name:
        text_file = open(open_status_name, 'w')
        text_file.write(text_box.get(1.0, END))
        status_bar.config(text=f'Saved {open_status_name}   ')
        # Close the file
        text_file.close()       
    else:
        save_as_file()

# Cut the text
def cut_text(e):
    global selected
    # check keyboard shortcut used
    if e:
        selected = root.clipboard_get()
    else:
        if text_box.selection_get():
            # Grab selected text from text box
            selected = text_box.selection_get()
            # Delete selected text
            text_box.delete("sel.first", "sel.last")
            # Clear the clipboard and add
            root.clipboard_clear()
            root.clipboard_append(selected)

# Copy the text
def copy_text(e):
    global selected
    # check keyboard shortcut used
    if e:
        selected = root.clipboard_get()
    if text_box.selection_get():
        # Grab selected text from text box
        selected = text_box.selection_get()
        # Clear the clipboard and add
        root.clipboard_clear()
        root.clipboard_append(selected)

# Paste the text
def paste_text(e):
    global selected
    # check keyboard shortcut used
    if e:
        selected = root.clipboard_get()
    else:    
        if selected:
            position = text_box.index(INSERT)
            text_box.insert(position, selected)

# Bold Text
def bold_text():
    try:
        # Check if there's selected text
        if text_box.tag_ranges("sel"):
            # Create font
            bold_font = font.Font(text_box, text_box.cget("font"))
            bold_font.configure(weight="bold")
            # Configure a tag
            current_tags = text_box.tag_names("sel.first")
            text_box.tag_configure("bold", font=bold_font)
            # Check tag setting
            if "bold" in current_tags:
                text_box.tag_remove("bold", "sel.first", "sel.last")
            else:
                text_box.tag_add("bold", "sel.first", "sel.last")
        else:
            print("No text selected")
    except TclError:
        print("An error occurred. Please select text before applying formatting.")      

# Italics Text
def italic_text():
    try:
        # Check if there's selected text
        if text_box.tag_ranges("sel"):
            # Create font
            italic_font = font.Font(text_box, text_box.cget("font"))
            italic_font.configure(slant="italic")
            # Configure a tag
            current_tags = text_box.tag_names("sel.first")
            text_box.tag_configure("italic", font=italic_font)
            # Check tag setting
            if "italic" in current_tags:
                text_box.tag_remove("italic", "sel.first", "sel.last")
            else:
                text_box.tag_add("italic","sel.first", "sel.last")
        else:
            print("No text selected")
    except TclError:
        print("An error occurred. Please select text before applying formatting.") 

# Change selected text color
def text_color():
    # Pick a color
    my_color = colorchooser.askcolor()[1]
    if my_color:
        # Create font
        color_font = font.Font(text_box, text_box.cget("font"))
        # Configure a tag
        current_tags = text_box.tag_names("sel.first")
        text_box.tag_configure("colored", font=color_font, foreground=my_color)
        # Check tag setting
        if "colored" in current_tags:
            text_box.tag_remove("colored", "sel.first", "sel.last")
        else:
            text_box.tag_add("colored","sel.first", "sel.last")

# Change background color
def bg_color():
    my_color = colorchooser.askcolor()[1]
    if my_color:
        text_box.config(bg=my_color)

# Change all text color
def all_text_color():
    my_color = colorchooser.askcolor()[1]
    if my_color:
        text_box.config(fg=my_color)

# Print file function
def print_file():
    status_bar.config(text="Printing")
    # Grab filename
    file_to_print = filedialog.askopenfilename(title="Open File", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*")))
    if file_to_print:
        try:
            subprocess.run(["lpr", file_to_print], check=True)
            print(f"Printing {file_to_print}")
        except subprocess.CalledProcessError as e:
            print(f"Error printing file: {e}")


# Add toolbar frame
toolbar_frame = Frame(root)
toolbar_frame.pack(fill=X)

# Main Frame
frame_app = Frame(root)
frame_app.pack(expand=True, fill='both')

# adding scrollbar 
text_scroll = Scrollbar(frame_app)

# packing scrollbar 
text_scroll.pack(side=RIGHT, fill=Y) 

# Horizontal scrollbar
horz_scroll = Scrollbar(frame_app, orient='horizontal')
# packing scrollbar 
horz_scroll.pack(side=BOTTOM, fill=X)

# Text Box
text_box = Text(frame_app, width=97, height=25, font=("Helvetica", 16), selectbackground="yellow", selectforeground="black", undo=True, yscrollcommand=text_scroll.set, wrap="none", xscrollcommand=horz_scroll.set)
text_box.pack(expand=True, fill='both')

# configure scrollbar
text_scroll.config(command=text_box.yview)
horz_scroll.config(command=text_box.xview)

# Create Menu
text_menu = Menu(root)
root.config(menu=text_menu)

# File Menu
file_menu = Menu(text_menu)
text_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Print", command=print_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Edit Menu
edit_menu = Menu(text_menu, tearoff=False)
text_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=lambda: cut_text(False))
edit_menu.add_command(label="Copy", command=lambda: copy_text(False))
edit_menu.add_command(label="Paste", command=lambda: paste_text(False))
file_menu.add_separator()
edit_menu.add_command(label="Undo", command=text_box.edit_undo)
edit_menu.add_command(label="Redo")
edit_menu.add_command(label="Redo", command=text_box.edit_redo)

# Color Menu
color_menu = Menu(text_menu, tearoff=False)
text_menu.add_cascade(label="Colors", menu=color_menu)
color_menu.add_command(label="Selected Text", command=text_color)
color_menu.add_command(label="All Text", command=all_text_color)
color_menu.add_command(label="Background", command=bg_color)


# Status Bar
status_bar = Label(root, text='Ready   ', anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=5)

# Font selector
def get_all_fonts():
    return sorted(font.families())

def change_font(event):
    selected_font = font_combo.get()
    current_font = font.Font(font=text_box['font'])
    text_box.configure(font=(selected_font, current_font.actual()['size']))

# Create a frame for the font selector
font_frame = Frame(root)
font_frame.pack(pady=5)

# Create and pack a label
Label(font_frame, text="Font:").pack(side=LEFT)

# Create the combobox for font selection
font_combo = ttk.Combobox(font_frame, values=get_all_fonts(), state="readonly", width=30)
font_combo.pack(side=LEFT)
font_combo.set(text_box.cget("font").split()[0])  # Set current font as default

# Bind the combobox to the change_font function
font_combo.bind("<<ComboboxSelected>>", change_font)
def change_font_size(event):
    selected_size = int(size_combo.get())
    current_font = font(font=text_box['font'])
    text_box.configure(font=(current_font.actual()['family'], selected_size))

# Create and pack a label for font size
Label(font_frame, text="Size:").pack(side=LEFT, padx=(10, 0))

# Create the combobox for font size selection
sizes = [8, 9, 10, 11, 12, 14, 16, 18, 20, 22, 24, 26, 28, 36, 48, 72]
size_combo = ttk.Combobox(font_frame, values=sizes, state="readonly", width=5)
size_combo.pack(side=LEFT)
size_combo.set(text_box.cget("font").split()[1])  # Set current size as default

# Bind the size combobox to the change_font_size function
size_combo.bind("<<ComboboxSelected>>", change_font_size)

# Edit Bindings
root.bind('<Control-x>', cut_text)
root.bind('<Control-c>', copy_text)
root.bind('<Control-v>', paste_text)

# Buttons implementation

# Bold button
bold_button = Button(toolbar_frame, text="Bold", command=bold_text)
bold_button.grid(row=0, column=0, sticky=W, padx=5)
# Italics button
italics_button = Button(toolbar_frame, text="Italics", command=italic_text)
italics_button.grid(row=0, column=1, padx=5)
# Undo/Redo buttons
undo_button = Button(toolbar_frame, text="Undo", command=text_box.edit_undo)
undo_button.grid(row=0, column=2, padx=5)
redo_button = Button(toolbar_frame, text="Redo", command=text_box.edit_redo)
redo_button.grid(row=0, column=3, padx=5)

# Text color
color_text_button = Button(toolbar_frame, text="Text Color", command=text_color)
color_text_button.grid(row=0, column=4, padx=5)

# Resize according to buttons
root.update_idletasks()
root.geometry('')

root.mainloop() 