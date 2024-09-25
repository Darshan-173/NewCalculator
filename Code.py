import tkinter as tk
from tkinter import messagebox
import math

# Initialize variables to track input
check_step = 0
input_sequence = []
current_expression = ""

def click_button(value):
    global current_expression
    current_expression += value
    entry.delete(0, tk.END)
    entry.insert(0, current_expression)
    input_sequence.append(value)  # Track every button press

def clear_entry():
    global check_step, input_sequence, current_expression
    entry.delete(0, tk.END)
    check_step = 0  # Reset check step when clearing
    input_sequence = []  # Reset input sequence
    current_expression = ""

def calculate_result():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
        input_sequence.append(str(result))  # Track result as part of input
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input! {e}")

def square_root():
    try:
        current = float(entry.get())
        result = math.sqrt(current)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
        input_sequence.append(f"√({current}) = {result}")  # Track square root operation
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input for square root! {e}")

def check_expression():
    global check_step
    if not input_sequence:
        messagebox.showinfo("Check", "No input entered yet!")
        return

    # Step through input sequence
    if check_step < len(input_sequence):
        value = input_sequence[check_step]
        if check_step == 0:
            messagebox.showinfo("Check", f"First number entered: {value}")
        elif check_step == 1:
            messagebox.showinfo("Check", f"Operator: {value}")
        elif check_step == 2:
            messagebox.showinfo("Check", f"Second number entered: {value}")
        elif check_step == 3:
            messagebox.showinfo("Check", f"Result: {value}")
        check_step += 1
    else:
        check_step = 0  # Reset step after completing the sequence

# Create main window
root = tk.Tk()
root.title("Calculator")
root.configure(bg="#dcdcdc")  # Light gray background

# Entry widget
entry = tk.Entry(root, width=15, font=('Arial', 24), borderwidth=5, relief="ridge", bg="#fff", fg="#000")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button definitions
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0, 2), ('√', 5, 2, 2),
    ('Check', 6, 0, 4)  # Add Check button
]

# Create buttons with a realistic design
for (text, row, col, *args) in buttons:
    if text == 'C':
        button = tk.Button(root, text=text, padx=40, pady=20, command=clear_entry, bg="#ff7f7f", fg="#fff", font=('Arial', 18), borderwidth=3, relief="raised")
        button.grid(row=row, column=col, columnspan=2, sticky="nsew")
    elif text == '√':  # Square root button
        button = tk.Button(root, text=text, padx=40, pady=20, command=square_root, bg="#4caf50", fg="#fff", font=('Arial', 18), borderwidth=3, relief="raised")
        button.grid(row=row, column=col, columnspan=2, sticky="nsew")
    elif text == 'Check':  # Check button
        button = tk.Button(root, text=text, padx=40, pady=20, command=check_expression, bg="#2196f3", fg="#fff", font=('Arial', 18), borderwidth=3, relief="raised")
        button.grid(row=row, column=col, columnspan=4, sticky="nsew")
    elif text == '=':
        button = tk.Button(root, text=text, padx=40, pady=20, command=calculate_result, bg="#4caf50", fg="#fff", font=('Arial', 18), borderwidth=3, relief="raised")
        button.grid(row=row, column=col)
    else:
        button = tk.Button(root, text=text, padx=40, pady=20, command=lambda t=text: click_button(t), bg="#f0f0f0", fg="#000", font=('Arial', 18), borderwidth=3, relief="raised")
        button.grid(row=row, column=col)

# Adjust column and row weights
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(7):  # Adjust for additional row
    root.grid_rowconfigure(i, weight=1)

# Run the application
root.mainloop()