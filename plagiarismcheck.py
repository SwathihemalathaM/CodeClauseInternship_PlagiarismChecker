from difflib import SequenceMatcher
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox


root = Tk()
root.title('Plagiarism Detector')
root.geometry('500x300')


def file1():
    global file1Data
    file1 = filedialog.askopenfilename(initialdir="C:\\Users\\smuna\\OneDrive\\Documents\\python swathi\\codeclausepythonprojects", title='file1',filetypes=(('text files','*.txt'),('all files','*.*')))
    file1text = open(file1,'r')
    file1Data = file1text.read()
    file1_text.insert(END,file1Data)
    file1text.close()

def file2():
    global file2Data
    file2 = filedialog.askopenfilename(initialdir="C:\\Users\\smuna\\OneDrive\\Documents\\python swathi\\codeclausepythonprojects", title='file1',filetypes=(('text files','*.txt'),('all files','*.*')))
    file2text = open(file2,'r')
    file2Data = file2text.read()
    file2_text.insert(END,file2Data)
    file2text.close()

def plagiarismcheck():
    match = SequenceMatcher(None,file1Data,file2Data).ratio()
    messagebox.showinfo('Output',f'The content are {match*100}% common.')



myframe = Frame(root)
myframe.pack(pady=5)
file1_button = Button(myframe,text='file1',command=file1).pack()

file1_text = Text(myframe,width=40,height=5)
file1_text.pack(pady=5)

file2_button = Button(myframe,text='file2',command=file2).pack()
file2_text = Text(myframe,width=40,height=5)
file2_text.pack(pady=5)

check_button = Button(myframe,text='Plagiariism Check',command=plagiarismcheck).pack()



root.mainloop()