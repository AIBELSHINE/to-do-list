import tkinter as tk

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def delete_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_listbox.delete(selected_task)

# GUI setup
root = tk.Tk()
root.title("To-Do List")

task_entry = tk.Entry(root, width=30)
task_entry.pack()

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack()

task_listbox = tk.Listbox(root, width=50, height=15)
task_listbox.pack()

root.mainloop()
