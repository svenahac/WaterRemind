from tkinter import *

root = Tk()
root.title("Test Program")

myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="My name Jeff")

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)

e = Entry(root, width = 50)
e.grid(row=1, column=1)
e.insert(0, "Vpisi nekaj")

def  myClick():
    myLabel = Label(root, text="Buton goes brr")
    myLabel.grid(row=3, column=4)

myButton = Button(root, text="Click me", padx=50, pady=50, command=myClick, fg="red", bg="black")
myButton.grid(row=2, column=3)
root.mainloop()