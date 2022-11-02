import tkinter

win = tkinter.Tk()
win.geometry("300x300+500+140")

btn1 = tkinter.Button(win,text="btn1")
btn1.config(width=50)
btn1.pack()

btn2 = tkinter.Button(win,text="btn2")
btn2.config(width=50)
btn2.pack()

btn3 = tkinter.Button(win,text="btn3")
btn3.config(width=50)
btn3.pack()

win.mainloop()