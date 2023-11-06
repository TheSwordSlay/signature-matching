import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, EpsImagePlugin
EpsImagePlugin.gs_windows_binary =  r'C:\Program Files\gs\gs10.02.0\bin\gswin64c'

def save_as_png(canvas,fileName):
    # save postscipt image 
    canvas.postscript(file = fileName + '.eps') 
    # use PIL to convert to PNG 
    img = Image.open(fileName + '.eps') 
    img.save(fileName + '.png', 'png') 
   
def paint(event, selected_colour):
    '''Draws a line following the user mouse cursor'''
    x1, y1 = event.x-1, event.y-1
    x2, y2 = (event.x+1), (event.y+1)
    canvas.create_line(x1, y1, x2, y2, fill=selected_colour, width=5)

def clear(canvas):
    '''Clear all drawn objects from the screen'''
    canvas.delete('all')

foreground_colour = 'white'
current_colour = 'black'

root = tk.Tk()
root.title("Whiteboard")
root.config(background='white')

canvas = tk.Canvas(root, width=300, height=300, borderwidth=0, highlightthickness=0, background='#e3e5e8')
canvas.grid(column=0, row=1, columnspan=5)
canvas.bind("<B1-Motion>", lambda event: paint(event, current_colour))

save_button = tk.Button(text='save',
                       foreground='white',
                       background='green',
                       relief='flat',
                       command=lambda: save_as_png(canvas,"new_signature")
                       )

clear_button = tk.Button(text='Clear',
                         fg='black',
                         bg='#c4c4c4',
                         relief='flat',
                         command=lambda: clear(canvas)
                         )

save_button.grid(column=0, row=0)

clear_button.grid(column=4, row=0)

root.mainloop()
