from tkinter import *
import time

root = Tk()
root.title("WaterRemind")
root.geometry("300x300")
root.resizable(False, False)
root.iconbitmap("icon.ico")

# Frame 1
frame = Frame(root)
frame.pack()

def calculate_BMI(a, b):
    ''' Calculates BMI '''
    conversed_to_meters = int(a) / 100
    bmi = int(b) / conversed_to_meters**2
    return round(bmi, 1)

def showBMI():
    ''' Removes other widgets and shows your BMI '''
    if height_entry.get() == "" or weight_entry.get() == "":
        return
    elif (int(height_entry.get()) == False) or (int(weight_entry.get()) == False):
        return
    else:
        weight.grid_forget()
        weight_entry.grid_forget()
        height.grid_forget()
        height_entry.grid_forget()
        calculate.grid_forget()
        bmi = calculate_BMI(height_entry.get(), weight_entry.get())
        myBMI = Label(frame, text="Your BMI is " + str(bmi), font=("Helvetica", 18))
        myBMI.grid(row=0, column=0, rowspan=3, columnspan=3, padx=10, pady=10) 

# Text and entry for height
height = Label(frame, text="Height (cm): ", font=("Helvetica", 18))
height.grid(row=0, column=0, sticky=W)
height_entry = Entry(frame, width=20)
height_entry.grid(row=0, column=1)

# Text and entry for weight
weight = Label(frame, text="Weight (kg): ", font=("Helvetica", 18))
weight.grid(row=1, column=0)
weight_entry = Entry(frame, width=20)
weight_entry.grid(row=1, column=1)

# Calculate button
calculate = Button(frame, text="Calculate BMI", command=showBMI, font=("Helvetica", 18), padx=2, pady=2)
calculate.grid(row=2, column=0, columnspan=3)

# Black line
my_canvas = Canvas(root, width=300, height=2, bg="black")
my_canvas.pack()

# Frame 2
frame2 = Frame(root)
frame2.pack()

timer = Label(frame2, text="Timer:", font=("Helvetica", 18))
timer.grid(row=0, column=0)

time = Label(frame2, text="00:30:00", font=("Helvetica", 18))
time.grid(row=0, column=1)

# Black line
my_canvas2 = Canvas(root, width=300, height=2, bg="black")
my_canvas2.pack()

frame.mainloop()