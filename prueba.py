from tkinter import *

class Window:
    def __init__(self):
        window=Tk()

        window.title('hola')
        window.geometry("300x200+10+20")
        window.mainloop()

window = Window()