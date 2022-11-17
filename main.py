from tkinter import *
from tkinter import filedialog
import pandas as pd
from PIL import Image, ImageTk,ImageSequence
import webbrowser
import numpy as np
from subprocess import *
import time
import sys

  
def openFile():
    filepath = filedialog.askopenfilename(title="Select the CSV file",
                                          filetypes= (("text files","*.csv"),
                                          ("all files","*.*")))
    print("input file path is : ",filepath)
    if(filepath==''):
        return
    dialouge_lable['text']='Analysing  '+filepath.split("/")[-1]
    button['image']=img2
    s='python kmean.py '+filepath
    #Popen opens analyse.py by giving the file path as an input argument 
    Popen(s)
    loading_lable=Label(window,text='''LOADING ...''',background='#000000',foreground='#ffffff')
    loading_lable.pack(pady=5)
    window.update()
    # t=time.localtime()
    # start = time.strftime("%S", t)
    # start_m = time.strftime("%M", t)
    # start_h = time.strftime("%H", t)
    # start=int(start)+int(start_m)*60+int(start_h)*3600

    # while(1):
    #     current_s=time.strftime("%S", time.localtime())
    #     current_m=time.strftime("%M", time.localtime())
    #     current_h=time.strftime("%H", time.localtime())
    #     current=int(current_s)+int(current_m)*60+int(current_h)*3600
    #     delta=int(current)-int(start)
    #     loading_lable['text']=str(10-delta)+' sec remaining...'
    #     window.update()
    #     if(delta>=10):
    #         break
   
    # print("next ran")
    # # webbrowser.open_new_tab(url)
    # window.destroy()

print("main.py started")
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
print("home page opened")
window.mainloop()



'''
Assets used :
visualization icon : https://www.flaticon.com/search?type=icon&word=visualize

'''