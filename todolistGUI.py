import tkinter
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox
from tkinter import filedialog,simpledialog

task = ""
tasks = []

def load_tasks_from_file():
    try:
        file = open("../../Desktop/tasks.txt")

        for line in file.readlines():
            tasks.append(line.strip())
        file.close()
    except FileNotFoundError:
        return
load_tasks_from_file()

def show_tasks():
    tasks_pad.configure(state='normal')
    tasks_pad.event_generate("<<SelectAll>>")
    tasks_pad.event_generate("<<Clear>>")
    task_index = 0
    for task in tasks:
        print(task + " [" + str(task_index) + "]")
        tasks_pad.insert(0.0, task + " [" + str(task_index) + "]\n")
        task_index += 1
    tasks_pad.configure(state='disabled')
def add_task():
    task = entry.get()
    tasks.append(task)
    print(tasks)
    show_tasks()

def delete_task():
    task_index = entry2.get()
    tasks.pop(int(task_index))
    show_tasks()

def save_tasks():
    file = open("../../Desktop/tasks.txt", "w")
    for task in tasks:
        file.write(task + "\n")
    file.close()
    show_tasks()

root = tkinter.Tk()
root['background']='grey'
root.title("To Do! GUI")
root.geometry('350x500')
root.resizable(0, 0)

l = tkinter.Label(root, text='To Do!', bg='grey')
l.pack()
tasks_pad = ScrolledText(root, width = 44, height = 25, bg='black', fg='white')
tasks_pad.pack()
l = tkinter.Label(root, text='Add task: ', bg='grey')
l.place(x=0, y=430)
entry = tkinter.Entry(width=35)
entry.place(x=0,y=450)
l = tkinter.Label(root, text='Del task: ', bg='grey')
l.place(x=280, y=430)
entry2 = tkinter.Entry(width=3)
entry2.place(x=280, y=450)
m = tkinter.Button(root, text = 'Add task', command=add_task, bg='grey')
m.place(x=0,y=473)
m = tkinter.Button(root, text = 'Delete task', command=delete_task, bg='grey')
m.place(x=78,y=473)
m = tkinter.Button(root, text = 'Save tasks', command=save_tasks, bg='grey')
m.place(x=171,y=473)
m = tkinter.Button(root, text = 'Exit app', command=exit, bg='grey', width=9)
m.place(x=260,y=473)
show_tasks()
root.mainloop()