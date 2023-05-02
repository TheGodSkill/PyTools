import tkinter as tk
import random
import time

def set_random_color():

    color = f"#{random.randint(0, 0xFFFFFF):06x}"
    root.configure(background=color)

def close():

    root.destroy()


msg = tk.Tk()
msg.withdraw()
tk.messagebox.showinfo("DeadPixel Tester", "25 Seconds of DeadPixel Testing now, program will exit automatically")
msg.destroy()


root = tk.Tk()
root.attributes("-fullscreen", True)
root.configure(background="black")

root.after(25000, close)

while True:
    set_random_color()
    root.update()
    time.sleep(5)
