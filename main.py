from tkinter import *
from tkinter import filedialog
import pandas as pd
import numpy as np
def openFile():
    filepath = filedialog.askopenfilename(title="Select the CSV file",
                                          filetypes= (("text files","*.csv"),
                                          ("all files","*.*")))
    file = open(filepath,'r')
    df = pd.read_csv(filepath)
    df.info()
    print("-------------------------------------")
    print(file.read())
    file.close()

window = Tk()
window.title("CSV Visualizer")
window.geometry('300x300')
button = Button(text="Open CSV file",command=openFile)
button.pack(pady=20)
window.mainloop()