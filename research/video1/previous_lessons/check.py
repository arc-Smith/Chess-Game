from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Codemy.com Image Viewer')
root.geometry("400x400")

def show():
	myLabel = Label(root, text=var.get()).pack()

var = StringVar()
c = Checkbutton(root, text="Would you like to SuperSize your order? Check Here!", variable=var, onvalue="SuperSize", offvalue="RegularSize")
c.deselect()
c.pack()
myButton = Button(root, text="Show Selection", command=show).pack()

root.mainloop()
