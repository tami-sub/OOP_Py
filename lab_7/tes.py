from tkinter import *

clicks = 0


def click_button():
    global clicks
    clicks += 1
    btn.config(text="Clicks {}".format(clicks))
    lbl.config(text="LOL")


root = Tk()
root.title("GUI на Python")
root.geometry("300x250")

lbl = Label(text="meme", background="#555")
lbl.pack(side=BOTTOM)

btn = Button(text="Clicks 0", background="#555", foreground="#ccc",
             padx="20", pady="8", font="16", command=click_button)
btn.pack()

root.mainloop()