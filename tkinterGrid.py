from tkinter import ttk
from tkinter import *

root = Tk()
content = ttk.Frame(root)
frame = ttk.Frame(content,borderwidth=5,relief="sunken",width=200,height=100)
namelabel = ttk.Label(content,text="name")
name= ttk.Entry(content)

onevariable = BooleanVar()
twovariable = BooleanVar()
threevariable = BooleanVar()
onevariable.set(True)
twovariable.set(False)
threevariable.set(True)
one = ttk.Checkbutton(content,text="One",variable=onevariable,onvalue=True)
two = ttk.Checkbutton(content,text="Two",variable=twovariable,onvalue=True)
three = ttk.Checkbutton(content,text="Three",variable=threevariable,onvalue=True)
ok = ttk.Button(content,text="okay")
cancel = ttk.Button(content, text="cancel")


content.grid(column=0,row=0)
frame.grid(column=0, row=0,columnspan=3, rowspan=2)
namelabel.grid(column=3, row=0,columnspan=2)
name.grid(column=3, row=1,columnspan=2)
one.grid(column=0,row=3)
two.grid(column=1,row=3)
three.grid(column=2,row=3)
ok.grid(column=3,row=3)
cancel.grid(column=4,row=3)
root.mainloop()