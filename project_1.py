from tkinter import *

def Submit():
    inputText = text.get('1.0', END)
    print(inputText)


window = Tk()

text = Text(window, bg="light yellow", font=('Ink Free', 25), fg='red', height=8, width=20)
text.pack()

button = Button(window, text='Submit', command=Submit, width=47, height=2, font=('Arial', 10))
button.pack()
window.mainloop()