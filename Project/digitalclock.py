import tkinter as tk
from time import strftime


root = tk.Tk()
root.title("Digital Clock")

def time():
    string  = strftime('%H:%M%S %p \n %d')