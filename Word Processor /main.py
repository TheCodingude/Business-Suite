import docx
from tkinter import *
from tkinter.scrolledtext import ScrolledText

document = docx.Document()



window = Tk()

bar = Scrollbar(window)
bar.grid(row=0, column=1)

text = Text(window)
text.grid(row = 0,column= 0)

window.mainloop()


