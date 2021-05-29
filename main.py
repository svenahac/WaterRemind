from tkinter import *
import time as mytime
import  pygame

root = Tk()
root.title("WaterRemind")
root.geometry("300x300")
root.resizable(False, False)
root.iconbitmap("icon.ico")

# Initializes pygame mixer 
pygame.mixer.init()

# Dictionary of all available sounds
sounds = {
    "Default" : "audio/default.mp3",
    "Amelia" : "audio/amelia.mp3",
    "Bruh" : "audio/bruh.mp3"
}

# Frame 1
frame = Frame(root)
frame.pack()

def timer():
    ''' First removes elements then starts timer, when it ends it adds elements back'''
    time.grid_remove()
    time_entry.grid_remove()
    repeats.grid_remove()
    repeats_entry.grid_remove()
    startTimer.grid_remove()
    timer_running.grid(row=0, column=0)

    # Selects the sound notification
    sound_file = sounds[clicked.get()]

    n = 0
    our_repeats = int(repeats_entry.get())
    while our_repeats > n:
        time_now = int(time_entry.get())
        root.update()
        mytime.sleep(time_now)
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play(loops=0)
        mytime.sleep(2)
        n += 1
    if n == our_repeats:
        timer_running.grid_remove()
        time.grid()
        time_entry.grid()
        repeats.grid()
        repeats_entry.grid()
        startTimer.grid()

# Text that shows when timer is running
timer_running = Label(frame, text="Timer is running", font=("Helvetica", 20))

# Text and entry for time
time = Label(frame, text="Set time (seconds): ", font=("Helvetica", 14))
time.grid(row=0, column=0)
time_entry = Entry(frame, width=15)
time_entry.insert(0, 1800)
time_entry.grid(row=0, column=1, columnspan=2)

# Text and entry for number of repeats
repeats = Label(frame, text="Repeats: ", font=("Helvetica", 14))
repeats.grid(row=1, column=0)
repeats_entry = Entry(frame, width=15)
repeats_entry.insert(0, 1)
repeats_entry.grid(row=1, column=1, columnspan=2)

# Button that starts the timer
startTimer = Button(frame, text="Start Timer", command=timer, font=("Helvetica", 14), padx=2, pady=2)
startTimer.grid(row=2, column=0, columnspan=3)

# Black line
my_canvas = Canvas(root, width=300, height=2, bg="black")
my_canvas.pack()

# Frame 2
frame2 = Frame(root)
frame2.pack()

sound = Label(frame2, text="Select sound", font=("Helvetica", 14))
sound.grid(row=0, column=0)

clicked = StringVar()
clicked.set("Default")

options = {"Default" : "hello", "Amelia" : "Juhu"}

dropdown = OptionMenu(frame2, clicked, "Default", "Amelia", "Bruh")
dropdown.grid(row=0, column=1, columnspan=2)


# Black line
my_canvas2 = Canvas(root, width=300, height=2, bg="black")
my_canvas2.pack()

root.mainloop()