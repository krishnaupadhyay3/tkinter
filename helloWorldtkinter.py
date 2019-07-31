import tkinter
from tkinter import scrolledtext , filedialog , ttk
import json
import requests
import fcntl , os
import time
import subprocess
class Appliation(tkinter.Tk):
    def __init__(self):
        super().__init__()

        # self.pack()
        self.checkdrive = tkinter.Button(self,
                                        text="check device..",
                                         command=self.CheckDevice    )   
        self.file_selector = tkinter.Button(self , text="select files...", command=self.sayWorld)
        self.start_process  = tkinter.Button(self,
                                 text="start archiving",
                                 command=self.WriteCore   )  
        self.listbox     = tkinter.Listbox(self,width=40, height=6, selectmode=tkinter.EXTENDED) 
        self.listbox.grid(row=0,column=0,rowspan=3)
        self.file_selector.grid(row=0,column=2)
        self.checkdrive.grid(row=0,column=3)
        self.start_process.grid(row=1,column=2)
        # self.Test2 = tkinter.Button(self , text="ytest2", command=self.sayWorld)
        # self.output = scrolledtext.ScrolledText(master=self)
        # self.helloButton.pack(side="top")
        # self.worldButton.pack(side="top")
        # self.Test1.pack(side="top")
        # self.Test2.pack(side="top")
        # self.output.pack(side="top")
    def outputLine(self,text):
        self.output.insert(tkinter.INSERT, text+'\n')
    def CheckDevice(self):
        CDROM_DRIVE ="/dev/sr0"
        data_dict =  {1 :'no disk in tray',
            2 :'tray open',
            3 : 'reading tray',
            4 :'disk in tray'}
        fd = os.open(CDROM_DRIVE, os.O_RDONLY | os.O_NONBLOCK)
        rv = fcntl.ioctl(fd, 0x5326)
        os.close(fd)
        print(rv)
        json_data = data_dict[rv]
        self.outputLine(json_data)
    def sayWorld(self):
        self.file_path = list(filedialog.askopenfilenames(filetypes=[("all files", "*")]) )
        # with tkinter.filedialog.askopenfile() as f:
        #     contents = f.read()
        #     print(contents)

        for x in self.file_path :
            self.listbox.insert(tkinter.END,x )
    def WriteCore():#self,device_id , path ,working_dir ,job_id):
        '''fuction to write file to the cd / Dvd '''
        pass
        #command_list = " xorriso -dev {}  -follow link -add {}".format(device_id ,path) 
        # cmd = ["/usr/bin/xorriso" ,"-dev" ,"{}".format(device_id),  "-follow", "link" , "-map_single", "{}".format(path) ]
        # p = subprocess.Popen(cmd,stdout=subprocess.PIPE , stderr = subprocess.STDOUT, universal_newlines =True, cwd=working_dir)
        # last_notify_time = time.time()
        # while p.poll() is None:
        #     line = p.stdout.readline().strip()
        #     line_list = line.split(" ")
        #     line_list = list(filter(None , line_list) )
        #     if "UPDATE" in line and "Writing" in line :
        #         progress ={}
        #         #line_list = line.split("%")[0].split(" ")
        #         line_list[6]
        #         if time.time() - last_notify_time >2:
        #             last_notify_time = time.time()
                    
        #     else:    #
        #         print (line_list)
if __name__ =="__main__":
    app = Appliation()
    app.mainloop()
