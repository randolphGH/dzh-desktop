import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Form1(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Form1")
        self.geometry("800x450")

        self.listbox1 = tk.Listbox(self)
        self.listbox1.place(x=355, y=350, width=133, height=24)

        self.combobox1 = ttk.Combobox(self)
        self.combobox1.place(x=72, y=65, width=151, height=28)

        self.button1 = tk.Button(self, text="button1")
        self.button1.place(x=156, y=249, width=94, height=29)

        self.label1 = tk.Label(self, text="label1")
        self.label1.place(x=125, y=118)

        self.textbox1 = tk.Entry(self)
        self.textbox1.place(x=172, y=127, width=125, height=27)

        self.bind("<Configure>", self.on_resize)
        
        self.button1.config(command=self.onclick)

    def onclick(self):
        messagebox.showinfo("Test Press button", "button pressed. Thank you.")

    def on_resize(self, event):
        # This method can be used to handle window resizing if needed
        pass

if __name__ == "__main__":
    app = Form1()
    app.mainloop()

