import tkinter
from tkinter import scrolledtext

class Appliation(tkinter.Frame):
    def __init__(self, root):
        super(Appliation, self).__init__(root)
        self.pack()
        self.helloButton = tkinter.Button(self,
                                        text="hello",
                                        command=self.sayHello    )   
        self.worldButton = tkinter.Button(self , text="world", command=self.sayWorld)
        self.output = scrolledtext.ScrolledText(master=self)
        self.helloButton.pack(side="top")
        self.worldButton.pack(side="top")
        self.output.pack(side="top")
    def outputLine(self,text):
        self.output.insert(tkinter.INSERT, text+'\n')
    def sayHello(self):
        self.outputLine("hello")
    def sayWorld(self):
        self.outputLine("world")
Appliation(tkinter.Tk()).mainloop()
