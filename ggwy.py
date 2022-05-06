from tkinter import *
choices = ['yes','no']
player = input(choices)

def func():
    def wish():
        print("Hey how are u?")
    def destroy():
        window.destroy()
    window = Tk()
    if (player == 'yes'):
        button = Button(window,text="hi",bg="green",command=wish).pack()
        window.mainloop()
    else:
        button1 = Button(window,text="bye",bg="red",command=destroy).pack()
        window.mainloop()

func()