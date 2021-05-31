from tkinter import *
import datetime

 
root = Tk()
root.geometry("1440x900+0+0")
 
frame = Frame(root)
frame.pack()
 
now = datetime.datetime.now()
time = now.strftime("%H:%M:%S")

label = Label(frame, text=time)
label.pack()

 
# root.mainloop()

while True:
    now = datetime.datetime.now()
    time = now.strftime("%H:%M:%S.%f")
    label.config(text=time)
    label.update()
    print(now, "updating")