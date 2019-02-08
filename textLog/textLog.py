import os
from tkinter import *
import diaryFile.diaryMaster as diary
from tkinter import scrolledtext
from tkinter import filedialog

def submitClicked():
    dir_path = txt_path.get().strip()
    file_name = txt_file.get().strip()
    if file_name == '':
        lbl2.configure(fg='red')
        return 
    message = txt_box.get("1.0", 'end-1c')
    diaryobj = diary.diaryMaster(dir_path, file_name)
    diaryobj.diaryWrite(message)


def getDirectory():
    #dir_path_asked = filedialog.askdirectory()
    dir_path_asked = ''
    file_name_asked = filedialog.askopenfilename()
    if os.path.isfile(file_name_asked):
        dir_path_asked = os.path.dirname(file_name_asked)
        file_name_asked = os.path.basename(file_name_asked)
    
    txt_path.insert(0,dir_path_asked)
    txt_file.insert(0,file_name_asked)

def main():
    global txt_path, txt_file, txt_box
    window = Tk()
    window.geometry('820x480')

    lbl1 = Label(window, text="Target Folder Path [{0}\Desktop]: ".format(os.path.join(os.environ['HOMEDRIVE'], os.environ['HOMEPATH'])),font=("Arial Bold", 10))
    lbl1.grid(column=1,row=10)
    txt_path = Entry(window,width=30)
    txt_path.grid(column=1,row=20)

    lbl2 = Label(window, text="File name* : ",font=("Arial Bold", 10))
    lbl2.grid(column=1,row=30)
    txt_file = Entry(window,width=30)
    txt_file.grid(column=1,row=40)

    browse_button = Button(window, text="Browse", width=20, command=getDirectory)
    browse_button.grid(column=1, row=50)

    lbl3 = Label(window, text="Log Message : ",font=("Arial Bold", 10))
    lbl3.grid(column=1, row=100)
    txt_box = scrolledtext.ScrolledText(window,width=100,height=20)
    txt_box.grid(column=1,row=110)

    submit_button = Button(window, text="Save Message", width=20, command=submitClicked)
    submit_button.grid(column=1, row=210)

    window.mainloop()

if __name__=="__main__":
    main()
