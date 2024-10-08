import tkinter as tk
from tkinter import ttk

class Calculator:
    def __init__(self, window):
        self.window = window
        self.window.title("Máy tính")
        self.create_menu()
        self.create_tabs()
        self.create_frame()

    def create_menu(self):
        menubar = tk.Menu(self.window)
        self.window.config(menu=menubar)

        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Exit", command=self.window.quit)
        menubar.add_cascade(label="File", menu=file_menu)

        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about)
        menubar.add_cascade(label="Help", menu=help_menu)

    def show_about(self):
        about_window = tk.Toplevel(self.window)
        about_window.title("About")
        label = tk.Label(about_window, text="Máy tính")
        label.pack()

    def create_tabs(self):
        self.tabs = ttk.Notebook(self.window)
        self.tabs.pack(fill="both", expand=True)

        self.calc_tab = ttk.Frame(self.tabs)
        self.tabs.add(self.calc_tab, text="Calculator")

        self.conv_tab = ttk.Frame(self.tabs)
        self.tabs.add(self.conv_tab, text="Converter")

    def create_frame(self):
        self.entry_frame = ttk.Frame(self.calc_tab)
        self.entry_frame.pack(fill="x")

        self.entry = ttk.Entry(self.entry_frame, width=35)
        self.entry.pack(side="left")

        self.button_frame = ttk.Frame(self.calc_tab)
        self.button_frame.pack(fill="both", expand=True)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val = 0
        col_val = 0

        for button in buttons:
            ttk.Button(self.button_frame, text=button, width=5, command=lambda button=button: self.on_click(button)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def on_click(self, button):
        if button == '=':
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        else:
            self.entry.insert(tk.END, button)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    window = tk.Tk()
    calculator = Calculator(window) 
    calculator.run()