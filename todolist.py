import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        deleted_task = listbox.get(selected_task_index)
        listbox.delete(selected_task_index)
        save_tasks()
        messagebox.showinfo("Task Deleted", f'Task "{deleted_task}" deleted successfully!')
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")

def save_tasks():
    tasks = listbox.get(0, tk.END)
    with open("tasks.txt", "w") as file:
        file.write("\n".join(tasks))

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            listbox.insert(tk.END, *file.read().splitlines())
    except FileNotFoundError:
        pass

root = tk.Tk()
root.title('Todo List - Sarfaraz CodSoft')
root.configure(bg='#1E1E1E')

# Header
tk.Label(root, text="Welcome to ToDo List", bg='#1E1E1E', fg='white', font=("Arial", 15)).pack(fill="x", padx=10, pady=10)

# Task Input
entry = tk.Entry(root, width=30, bg="#333333", fg="white", font=("Arial", 12))
entry.pack(pady=10, padx=10, fill="x")

# Buttons
tk.Button(root, text="Add Task", bg="white", fg="black", font=("Arial", 12), padx=10, command=add_task).pack(pady=5)
tk.Button(root, text="Delete Task", bg="white", fg="black", font=("Arial", 12), padx=10, command=delete_task).pack(pady=5)

# Listbox
listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=40)
listbox.pack(pady=10)

load_tasks()
root.mainloop()
