from tkinter import *
from tkinter import filedialog
import pandas as pd
from PIL import Image, ImageTk,ImageSequence
import webbrowser
import numpy as np
from subprocess import *
import time
import sys
import os 
   
def openFile():
    filepath = filedialog.askopenfilename(title="Select the CSV file",
                                          filetypes= (("text files","*.csv"),
                                          ("all files","*.*")))
    file = open(filepath,'r')
    
    button.config(image =img2,bd=0,bg='#000000',activebackground="#000000")
    df = pd.read_csv(filepath)
    # df.info()
    # print("-------------------------------------")
    # print(file.read())
    print("---------lets shift to another file------------")
    s='python analyse.py '+filepath
    Popen(s)
    time.sleep(10)
   
    print("next ran")
    url = "http://127.0.0.1:8888/"
    webbrowser.open_new_tab(url)
    file.close()


window = Tk()
img1=PhotoImage(file='./assets/images/open_csv_button.png')
img2=PhotoImage(file='./assets/images/opened.png')
window.config(bg='#000000')
window.title("CSV Visualizer")
window.geometry('300x300')
#heading  all the data about the application and its working
heading_lable=Label(window,text="CSV Visualizer",font='Helvetica 20 bold ',background='#000000',foreground='#ffffff')
heading_lable.pack(pady=5)
#description
description_lable=Label(window,text='''Simple GUI Tool to visualize & analyse CSV files ''',background='#000000',foreground='#ffffff')
description_lable.pack(pady=5)

#dialouge
dialouge_lable=Label(window,text="Select a CSV file ",background='#000000',foreground='#ffffff')
dialouge_lable.pack(pady=5)

button = Button(window,command=openFile, image =img1,bd=0,bg='#000000',activebackground="#000000")
button.pack(pady=20)
window.mainloop()



'''
Assets used :
visualization icon : https://www.flaticon.com/search?type=icon&word=visualize

'''