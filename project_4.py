from tkinter import *

def moveUp(event):
    lable.place(x = lable.winfo_x(),y = lable.winfo_y() - 10)

def moveDown(event):
    lable.place(x = lable.winfo_x(),y = lable.winfo_y() + 10)

def moveLeft(event):
    lable.place(x = lable.winfo_x() - 10,y = lable.winfo_y())

def moveRight(event):
    lable.place(x = lable.winfo_x() + 10,y = lable.winfo_y())


window = Tk()
window.geometry("500x500")

window.bind("u", moveUp)
window.bind("d", moveDown)
window.bind("l", moveLeft)
window.bind("r", moveRight)

lable = Label(window, bg="red", width='10', height='5')
lable.place(x=0, y=0)


window.mainloop()