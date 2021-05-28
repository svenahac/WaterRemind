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

def start_timer():
    ''' Starts timer '''
    t = int(time_entry.get())
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins,secs)
        time2 = Label(frame2, text=timer, font=("Helvetica", 18))
        time2.grid(row=0, column=1)
        frame.after(1000)
        t -= 1
    


# Text and entry for time
time = Label(frame, text="Set time (min): ", font=("Helvetica", 18))
time.grid(row=0, column=0)
time_entry = Entry(frame, width=15)
time_entry.insert(0, 30)
time_entry.grid(row=0, column=1, columnspan=2)
old_time = int(time_entry.get())

startTimer = Button(frame, text="Start Timer", command=start_timer, font=("Helvetica", 18), padx=2, pady=2)
startTimer.grid(row=1, column=0, columnspan=3)

# Black line
my_canvas = Canvas(root, width=300, height=2, bg="black")
my_canvas.pack()

def start_timer():
    while hours != 0 and minutes != 0 and seconds != 0:
        seconds -= 1
        time.after(1000,start_timer)

# Frame 2
frame2 = Frame(root)
frame2.pack()

timer = Label(frame2, text="Timer:", font=("Helvetica", 18))
timer.grid(row=0, column=0)

# Black line
my_canvas2 = Canvas(root, width=300, height=2, bg="black")
my_canvas2.pack()

root.mainloop()