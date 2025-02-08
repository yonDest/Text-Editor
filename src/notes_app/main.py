import tkinter as tk
from tkinter import filedialog, font, colorchooser, ttk
import subprocess
import os
import platform

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.geometry("700x700")
        self.root.title("Notes")
        
        # Icon setting
        try:
            icon_path = os.path.join(os.path.dirname(__file__), "resources", "icon.png")
            if platform.system() == "Windows":
                self.root.iconbitmap(icon_path)
            elif platform.system() == "Darwin":  # macOS
            # Convert the path to absolute path
                icon_path = os.path.abspath(icon_path)
                try:
                # Try PhotoImage first
                    icon = tk.PhotoImage(file=icon_path)
                    self.root.iconphoto(True, icon)
                except tk.TclError:
                # If fails try alternative method for macOS
                    from PIL import Image, ImageTk
                    icon = Image.open(icon_path)
                    icon = ImageTk.PhotoImage(icon)
                    self.root.iconphoto(True, icon)
            else:  # Linux
                icon = tk.PhotoImage(file=icon_path)
                self.root.iconphoto(True, icon)
        except Exception as e:
            print(f"Could not load icon: {e}")
        
        self.root.minsize(height=250, width=350)

        self.open_status_name = False
        self.selected = False

        self.setup_ui()
        self.setup_menu()
        self.setup_bindings()

    def setup_ui(self):
        # Toolbar Frame
        self.toolbar_frame = tk.Frame(self.root)
        self.toolbar_frame.pack(fill=tk.X)

        self.font_frame = tk.Frame(self.root)
        self.font_frame.pack(fill=tk.X, pady=5)

        # Main Frame
        self.frame_app = tk.Frame(self.root)
        self.frame_app.pack(expand=True, fill='both')

        # Scrollbars
        self.text_scroll = tk.Scrollbar(self.frame_app)
        self.text_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.horz_scroll = tk.Scrollbar(self.frame_app, orient='horizontal')
        self.horz_scroll.pack(side=tk.BOTTOM, fill=tk.X)

        # Text Box
        self.text_box = tk.Text(self.frame_app, width=97, height=25, font=("Helvetica", 16),
                                selectbackground="yellow", selectforeground="black", undo=True,
                                yscrollcommand=self.text_scroll.set, wrap="none",
                                xscrollcommand=self.horz_scroll.set)
        self.text_box.pack(expand=True, fill='both')

        # Configure scrollbars
        self.text_scroll.config(command=self.text_box.yview)
        self.horz_scroll.config(command=self.text_box.xview)

        # Status Bar
        self.status_bar = tk.Label(self.root, text='Ready   ', anchor=tk.E)
        self.status_bar.pack(fill=tk.X, side=tk.BOTTOM, ipady=5)

        self.setup_font_selector()
        self.setup_toolbar_buttons()
    
    def setup_menu(self):
        self.text_menu = tk.Menu(self.root)
        self.root.config(menu=self.text_menu)

        # File Menu
        self.file_menu = tk.Menu(self.text_menu, tearoff=False)
        self.text_menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Save As", command=self.save_as_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Print", command=self.print_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.root.quit)

        # Edit Menu
        self.edit_menu = tk.Menu(self.text_menu, tearoff=False)
        self.text_menu.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Cut", command=lambda: self.cut_text(False))
        self.edit_menu.add_command(label="Copy", command=lambda: self.copy_text(False))
        self.edit_menu.add_command(label="Paste", command=lambda: self.paste_text(False))
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Undo", command=self.text_box.edit_undo)
        self.edit_menu.add_command(label="Redo", command=self.text_box.edit_redo)

        # Color Menu
        self.color_menu = tk.Menu(self.text_menu, tearoff=False)
        self.text_menu.add_cascade(label="Colors", menu=self.color_menu)
        self.color_menu.add_command(label="Selected Text", command=self.text_color)
        self.color_menu.add_command(label="All Text", command=self.all_text_color)
        self.color_menu.add_command(label="Background", command=self.bg_color)

        # Add Sticky Notes Menu
        self.sticky_menu = tk.Menu(self.text_menu, tearoff=False)
        self.text_menu.add_cascade(label="Sticky Notes", menu=self.sticky_menu)
        self.sticky_menu.add_command(label="New Sticky Note", command=self.create_sticky_note)

    def setup_bindings(self):
        self.root.bind('<Control-x>', self.cut_text)
        self.root.bind('<Control-c>', self.copy_text)
        self.root.bind('<Control-v>', self.paste_text)

    def setup_font_selector(self):

        # Create a center frame within font_frame
        center_frame = tk.Frame(self.font_frame)
        center_frame.pack(expand=True)

        # Font selector
        font_frame = tk.Frame(center_frame)
        font_frame.pack(side=tk.LEFT, padx=(0, 10))

        tk.Label(font_frame, text="Font:").pack(side=tk.LEFT)
        self.font_combo = ttk.Combobox(font_frame, values=sorted(font.families()), state="readonly", width=30)
        self.font_combo.pack(side=tk.LEFT)
        self.font_combo.set(self.text_box.cget("font").split()[0])
        self.font_combo.bind("<<ComboboxSelected>>", self.change_font)

        # Size selector
        size_frame = tk.Frame(center_frame)
        size_frame.pack(side=tk.LEFT)

        tk.Label(size_frame, text="Size:").pack(side=tk.LEFT)
        sizes = [8, 9, 10, 11, 12, 14, 16, 18, 20, 22, 24, 26, 28, 36, 48, 72]
        self.size_combo = ttk.Combobox(size_frame, values=sizes, state="readonly", width=5)
        self.size_combo.pack(side=tk.LEFT)
        self.size_combo.set(self.text_box.cget("font").split()[1])
        self.size_combo.bind("<<ComboboxSelected>>", self.change_font_size)
        
        
    def setup_toolbar_buttons(self):
        tk.Button(self.toolbar_frame, text="Bold", command=self.bold_text).grid(row=0, column=0, sticky=tk.W, padx=5)
        tk.Button(self.toolbar_frame, text="Italics", command=self.italic_text).grid(row=0, column=1, padx=5)
        tk.Button(self.toolbar_frame, text="Undo", command=self.text_box.edit_undo).grid(row=0, column=2, padx=5)
        tk.Button(self.toolbar_frame, text="Redo", command=self.text_box.edit_redo).grid(row=0, column=3, padx=5)
        tk.Button(self.toolbar_frame, text="Text Color", command=self.text_color).grid(row=0, column=4, padx=5)

    # File operations
    def new_file(self):
        self.text_box.delete("1.0", tk.END)
        self.root.title('New File - Editor')
        self.status_bar.config(text="New File   ")
        self.open_status_name = False

    def open_file(self):
        self.text_box.delete("1.0", tk.END)
        text_file = filedialog.askopenfilename(title="Open File", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*")))
        if text_file:
            self.open_status_name = text_file
            self.status_bar.config(text=f'{text_file}   ')
            with open(text_file, 'r') as file:
                self.text_box.insert(tk.END, file.read())

    def save_as_file(self):
        text_file = filedialog.asksaveasfilename(defaultextension=".*", title="Save File", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*")))
        if text_file:
            self.open_status_name = text_file
            self.root.title(f'{text_file} - Editor')
            self.status_bar.config(text=f'Saved {text_file}   ')
            with open(text_file, 'w') as file:
                file.write(self.text_box.get(1.0, tk.END))

    def save_file(self):
        if self.open_status_name:
            with open(self.open_status_name, 'w') as file:
                file.write(self.text_box.get(1.0, tk.END))
            self.status_bar.config(text=f'Saved {self.open_status_name}   ')
        else:
            self.save_as_file()

    def print_file(self):
        self.status_bar.config(text="Printing")
        file_to_print = filedialog.askopenfilename(title="Open File", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*")))
        if file_to_print:
            try:
                subprocess.run(["lpr", file_to_print], check=True)
                print(f"Printing {file_to_print}")
            except subprocess.CalledProcessError as e:
                print(f"Error printing file: {e}")

    # Text operations
    def cut_text(self, e):
        if e:
            self.selected = self.root.clipboard_get()
        elif self.text_box.selection_get():
            self.selected = self.text_box.selection_get()
            self.text_box.delete("sel.first", "sel.last")
            self.root.clipboard_clear()
            self.root.clipboard_append(self.selected)

    def copy_text(self, e):
        if e:
            self.selected = self.root.clipboard_get()
        if self.text_box.selection_get():
            self.selected = self.text_box.selection_get()
            self.root.clipboard_clear()
            self.root.clipboard_append(self.selected)

    def paste_text(self, e):
        if e:
            self.selected = self.root.clipboard_get()
        elif self.selected:
            position = self.text_box.index(tk.INSERT)
            self.text_box.insert(position, self.selected)

    def bold_text(self):
        try:
            if self.text_box.tag_ranges("sel"):
                bold_font = font.Font(self.text_box, self.text_box.cget("font"))
                bold_font.configure(weight="bold")
                self.text_box.tag_configure("bold", font=bold_font)
                current_tags = self.text_box.tag_names("sel.first")
                if "bold" in current_tags:
                    self.text_box.tag_remove("bold", "sel.first", "sel.last")
                else:
                    self.text_box.tag_add("bold", "sel.first", "sel.last")
            else:
                print("No text selected")
        except tk.TclError:
            print("An error occurred. Please select text before applying formatting.")

    def italic_text(self):
        try:
            if self.text_box.tag_ranges("sel"):
                italic_font = font.Font(self.text_box, self.text_box.cget("font"))
                italic_font.configure(slant="italic")
                self.text_box.tag_configure("italic", font=italic_font)
                current_tags = self.text_box.tag_names("sel.first")
                if "italic" in current_tags:
                    self.text_box.tag_remove("italic", "sel.first", "sel.last")
                else:
                    self.text_box.tag_add("italic","sel.first", "sel.last")
            else:
                print("No text selected")
        except tk.TclError:
            print("An error occurred. Please select text before applying formatting.")

    def text_color(self):
        my_color = colorchooser.askcolor()[1]
        if my_color:
            if self.text_box.tag_ranges("sel"):
                color_font = font.Font(self.text_box, self.text_box.cget("font"))
                self.text_box.tag_configure("colored", font=color_font, foreground=my_color)
                current_tags = self.text_box.tag_names("sel.first")
                if "colored" in current_tags:
                    self.text_box.tag_remove("colored", "sel.first", "sel.last")
                else:
                    self.text_box.tag_add("colored","sel.first", "sel.last")
            else:
                print("An error occurred. Please select text before applying formatting.")

    def bg_color(self):
        my_color = colorchooser.askcolor()[1]
        if my_color:
            self.text_box.config(bg=my_color)

    def all_text_color(self):
        my_color = colorchooser.askcolor()[1]
        if my_color:
            self.text_box.config(fg=my_color)

    def change_font(self, event):
        selected_font = self.font_combo.get()
        current_font = font.Font(font=self.text_box['font'])
        self.text_box.configure(font=(selected_font, current_font.actual()['size']))

    def change_font_size(self, event):
        selected_size = int(self.size_combo.get())
        current_font = font.Font(font=self.text_box['font'])
        self.text_box.configure(font=(current_font.actual()['family'], selected_size))

    def create_sticky_note(self):
        StickyNote()

class StickyNote:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title("Sticky Note")
        self.window.geometry("250x250")
        self.window.configure(bg="#fff7aa")  # Light yellow background
        
        # Remove window decorations except close button
        self.window.overrideredirect(True)
        
        # Add custom title bar
        self.title_bar = tk.Frame(self.window, bg="#e6de99", relief="raised", bd=1)
        self.title_bar.pack(expand=0, fill=tk.X)
        
        # Add close button
        self.close_button = tk.Button(self.title_bar, text="×", command=self.window.destroy,
                                    bg="#e6de99", padx=2, pady=2, bd=0,
                                    font=("arial", "10", "bold"))
        self.close_button.pack(side=tk.RIGHT)
        
        # Add text widget
        self.text = tk.Text(self.window, wrap=tk.WORD, bg="#fff7aa",
                           relief="flat", font=("Arial", 12),
                           width=20, height=10)
        self.text.pack(expand=True, fill='both', padx=5, pady=5)
        
        # Bind mouse events for window dragging
        self.title_bar.bind("<Button-1>", self.start_move)
        self.title_bar.bind("<B1-Motion>", self.on_move)
        
        # Add right-click menu
        self.setup_context_menu()
        
    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def on_move(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.window.winfo_x() + deltax
        y = self.window.winfo_y() + deltay
        self.window.geometry(f"+{x}+{y}")
        
    def setup_context_menu(self):
        self.context_menu = tk.Menu(self.window, tearoff=0)
        self.context_menu.add_command(label="Change Color", command=self.change_color)
        self.text.bind("<Button-3>", self.show_context_menu)
        
    def show_context_menu(self, event):
        self.context_menu.post(event.x_root, event.y_root)
        
    def change_color(self):
        color = colorchooser.askcolor(title="Choose Sticky Note Color")[1]
        if color:
            self.window.configure(bg=color)
            self.text.configure(bg=color)

def main():
    root = tk.Tk()
    editor = TextEditor(root)
    root.mainloop()

if __name__ == "__main__":
    main()
