
from tkinter import *
from tkinter import messagebox, simpledialog



class Board:
    def __init__(self, master):
        
        self.master = master
        self.master.title("Kanban Board by Saurabh Saindhane")
        self.master.geometry("600x400")

        
        self.todo_frame = Frame(self.master, bg="lightblue")
        self.inprogress_frame = Frame(self.master, bg="lightgreen")
        self.testing_frame = Frame(self.master, bg="yellow")
        self.done_frame = Frame(self.master, bg="lightpink")

       
        self.todo_label = Label(self.todo_frame, text="To Do", font=("Arial", 16), bg="lightblue")
        self.inprogress_label = Label(self.inprogress_frame, text="In Progress", font=("Arial", 16), bg="lightgreen")
        self.testing_label = Label(self.testing_frame, text="Testing", font=("Arial", 16), bg="yellow")
        self.done_label = Label(self.done_frame, text="Done", font=("Arial", 16), bg="lightpink")

        
        self.todo_listbox = Listbox(self.todo_frame, width=20, height=10)
        self.inprogress_listbox = Listbox(self.inprogress_frame, width=20, height=10)
        self.testing_listbox = Listbox(self.testing_frame, width=20, height=10)
        self.done_listbox = Listbox(self.done_frame, width=20, height=10)

      
        self.add_button = Button(self.master, text="Add a task", command=self.add_task)
        self.move_button = Button(self.master, text="Move a task", command=self.move_task)

      
        self.todo_frame.pack(side=LEFT, fill=BOTH, expand=True)
        self.inprogress_frame.pack(side=LEFT, fill=BOTH, expand=True)
        self.testing_frame.pack(side=LEFT, fill=BOTH, expand=True)
        self.done_frame.pack(side=LEFT, fill=BOTH, expand=True)

        self.todo_label.pack()
        self.inprogress_label.pack()
        self.testing_label.pack()
        self.done_label.pack()

        self.todo_listbox.pack(fill=BOTH, expand=True)
        self.inprogress_listbox.pack(fill=BOTH, expand=True)
        self.testing_listbox.pack(fill=BOTH, expand=True)
        self.done_listbox.pack(fill=BOTH, expand=True)

        self.add_button.pack(side=LEFT)
        self.move_button.pack(side=RIGHT)

    def add_task(self):
       
        task = simpledialog.askstring("Add a task", "Enter the task:")

      
        if task:
           
            self.todo_listbox.insert(END, task)

    def move_task(self):
     
        todo_selection = self.todo_listbox.curselection()
        inprogress_selection = self.inprogress_listbox.curselection()
        testing_selection = self.testing_listbox.curselection()

        
        if len(todo_selection) + len(inprogress_selection) + len(testing_selection) == 1:
         
            if todo_selection:
                index = todo_selection[0]
                task = self.todo_listbox.get(index)
                self.todo_listbox.delete(index)
                self.inprogress_listbox.insert(END, task)
            elif inprogress_selection:
                index = inprogress_selection[0]
                task = self.inprogress_listbox.get(index)
                self.inprogress_listbox.delete(index)
                self.testing_listbox.insert(END, task)
            elif testing_selection:
                index = testing_selection[0]
                task = self.testing_listbox.get(index)
                self.testing_listbox.delete(index)
                self.done_listbox.insert(END, task)
            else:
                messagebox.showinfo("Task completed", "Task is already completed")


root = Tk()
board = Board(root)
root.mainloop()
