import tkinter as tk
from tkinter import messagebox

def on_entry_click(event):
    if entry_task.get() == 'Enter your task...':
        entry_task.delete(0, tk.END)
        entry_task.config(fg='black')  # Set text color to black

def on_focus_out(event):
    if entry_task.get() == '':
        entry_task.insert(0, 'Enter your task...')
        entry_task.config(fg='grey')  # Set text color to grey

def add_task():
    task = entry_task.get()
    if task and task != 'Enter your task...':
        to_do_list.append(task)
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        selected_index = listbox_tasks.curselection()[0]
        deleted_task = to_do_list.pop(selected_index)
        listbox_tasks.delete(selected_index)
        messagebox.showinfo("Success", f"Task '{deleted_task}' deleted successfully!")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def update_task():
    try:
        selected_index = listbox_tasks.curselection()[0]
        updated_task = entry_task.get()
        to_do_list[selected_index] = updated_task
        listbox_tasks.delete(selected_index)
        listbox_tasks.insert(tk.END, updated_task)
        entry_task.delete(0, tk.END)
        messagebox.showinfo("Success", "Task updated successfully!")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to update.")

def view_tasks():
    if not to_do_list:
        messagebox.showinfo("Info", "No tasks to display.")
    else:
        messagebox.showinfo("To-Do List", "\n".join(to_do_list))

def exit_program():
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("To-Do List")
root.configure(bg='#ECECEC')

# Create and set up widgets
entry_task = tk.Entry(root, width=50, font=('Arial', 12), fg='grey')
entry_task.insert(0, 'Enter your task...')
entry_task.bind('<FocusIn>', on_entry_click)
entry_task.bind('<FocusOut>', on_focus_out)

listbox_tasks = tk.Listbox(root, selectmode=tk.SINGLE, height=10, width=50, bg='#F0F0F0', font=('Arial', 12))
button_add = tk.Button(root, text="Add Task", command=add_task, bg='#A3FFA3', font=('Arial', 12, 'bold'))
button_delete = tk.Button(root, text="Delete Task", command=delete_task, bg='#FF7F7F', font=('Arial', 12, 'bold'))
button_update = tk.Button(root, text="Update Task", command=update_task, bg='#7FBFFF', font=('Arial', 12, 'bold'))
button_view = tk.Button(root, text="View Tasks", command=view_tasks, bg='#FFD97F', font=('Arial', 12, 'bold'))
button_exit = tk.Button(root, text="Exit", command=exit_program, bg='#FF7F7F', font=('Arial', 12, 'bold'))

# Place widgets in the window
entry_task.pack(pady=10)
listbox_tasks.pack()
button_add.pack(pady=5)
button_delete.pack(pady=5)
button_update.pack(pady=5)
button_view.pack(pady=5)
button_exit.pack(pady=10)

# Initialize the to-do list
to_do_list = []

# Run the main loop
root.mainloop()
