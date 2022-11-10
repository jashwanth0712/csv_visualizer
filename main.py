from tkinter import *
from tkinter import filedialog
import pandas as pd
from PIL import Image, ImageTk

import numpy as np
import sys
import os 

def openFile():
    filepath = filedialog.askopenfilename(title="Select the CSV file",
                                          filetypes= (("text files","*.csv"),
                                          ("all files","*.*")))
    file = open(filepath,'r')
    df = pd.read_csv(filepath)
    df.info()
    print("-------------------------------------")
    print(file.read())
    print("---------lets shift to another file------------")
    os.system('python analyse.py')
    file.close()


window = Tk()
k=PhotoImage(file='./assets/images/open_csv_button.png')
window.config(bg='#000000')
window.title("CSV Visualizer")
window.geometry('300x300')
button = Button(window,command=openFile, image =k,bd=0,bg='#000000',activebackground="#000000")
button.pack(pady=20)
window.mainloop()