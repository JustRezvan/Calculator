import tkinter as tk

def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + value)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Ошибка")

def clear():
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Калькулятор")
root.configure(bg="#0D0D0D")

entry = tk.Entry(root, width=20, borderwidth=5, font=('Arial', 18))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

button_style = {'bg': '#333333', 'fg': '#FFFFFF', 'font': ('Arial', 14), 'width': 5, 'height': 2}

buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', '=', '+'),
    ('C',)
]

for i, row in enumerate(buttons):
    for j, button_label in enumerate(row):
        if button_label != 'C':
            bg_color = "#FF5722" if button_label in {'=', 'C'} else "#333333"
            button = tk.Button(root, text=button_label, bg=bg_color, fg="#FFFFFF", font=('Arial', 14),
                                width=5, height=2, command=lambda value=button_label: button_click(value))
            button.grid(row=i+1, column=j, padx=5, pady=5)
            if button_label in {'=', 'C'}:
                button.configure(command=calculate if button_label == '=' else clear)
        else:
            button = tk.Button(root, text=button_label, bg="#FF5722", fg="#FFFFFF", font=('Arial', 14),
                                width=15, height=2, command=clear)
            button.grid(row=i+1, column=j, padx=5, pady=5, columnspan=3)

root.mainloop()
