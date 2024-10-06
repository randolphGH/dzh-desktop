import tkinter as tk
import database

def on_submit():
    name = entry.get()
    database.insert(name)

def update_listbox():
    rows = database.get_names()

    listbox.delete(0, tk.END)
    for row in rows:
        listbox.insert(tk.END, row[1])
    

database.create_database()
app = tk.Tk()
app.title("Python Desktop App")
app.geometry("400x300")

label = tk.Label(app, text="Enter your name:")
label.pack()

entry = tk.Entry(app)
entry.pack()

submit_button = tk.Button(app, text="Submit", command=on_submit)
submit_button.pack()

listbox = tk.Listbox(app)
listbox.pack()
update_listbox()

app.mainloop()

