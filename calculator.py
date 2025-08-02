import tkinter as tk

def click(btn_text):
    current = entry.get()
    if btn_text == "AC":
        entry.delete(0, tk.END)
    elif btn_text == "=":
        try:
            expression = current.replace('×', '*').replace('÷', '/')
            result = str(eval(expression))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif btn_text == "+/-":
        if current and current[0] == "-":
            entry.delete(0)
        else:
            entry.insert(0, "-")
    elif btn_text == "%":
        try:
            result = str(float(current) / 100)
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    else:
        entry.insert(tk.END, btn_text)

root = tk.Tk()
root.title("Calculator")
root.configure(bg="black")
root.geometry("330x450")
root.resizable(False, False)

entry = tk.Entry(root, font=("Arial", 24), bd=10, relief=tk.FLAT, bg="black", fg="white", justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="nsew")

buttons = [
    ["AC", "+/-", "%", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["00", "0", ".", "="]
]

def create_button(text, row, col):
    bg_color = "#FF9500" if text in ["÷", "×", "-", "+", "="] else "#505050" if text in ["AC", "+/-", "%"] else "#1C1C1C"
    fg_color = "white" if text != "00" else "#FFCC00"

    btn = tk.Button(root, text=text, font=("Arial", 20), fg=fg_color, bg=bg_color,
                    width=5, height=2, relief=tk.FLAT,
                    command=lambda t=text: click(t))
    btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

for i, row in enumerate(buttons):
    for j, char in enumerate(row):
        create_button(char, i+1, j)

for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

root.mainloop()
