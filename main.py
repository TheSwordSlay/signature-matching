import os
import tkinter as tk
from tkinter import messagebox
from signature_check import orb_sim
from PIL import Image, EpsImagePlugin
EpsImagePlugin.gs_windows_binary =  r'C:\Program Files\gs\gs10.02.0\bin\gswin64c'

def save_as_png(canvas,fileName):
    canvas.postscript(file = fileName + '.eps') 

    img = Image.open(fileName + '.eps') 
    img.save(fileName + '.png', 'png') 
    path = 'assets'
    checkSig = os.listdir(path)
    sigOwner = "none"
    best = 0
    for x in checkSig:
        path1s = 'assets\\'+x
        path2s = 'check.png'
        result = orb_sim(path1s, path2s)*100
        print(x+' '+str(result)+'%')
        if(result >= 60):
            if(result > best):
                sigOwner = x
                best = result
    if(sigOwner != 'none'):
        messagebox.showinfo("Tanda tangan terdeteksi",
                            "Ini adalah tanda tangan "+sigOwner[:-4])
    else:
        messagebox.showerror("Tanda tangan tidak terdeteksi",
                             "Tanda tangan tidak cocok dengan data apapun")

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

# Create the window
root = tk.Tk()
root.title("Signature Check")
root.config(background='white')

# Create a canvas object and place it at the bottom of the window
canvas = tk.Canvas(root, width=300, height=300, borderwidth=0, highlightthickness=0, background='#e3e5e8')
canvas.grid(column=0, row=1, columnspan=5)
canvas.bind("<B1-Motion>", lambda event: paint(event, current_colour))

# Create and style buttons
save_button = tk.Button(text='check',
                       foreground='white',
                       background='green',
                       relief='flat',
                       command=lambda: save_as_png(canvas,"check")
                       )

# blue_button = tk.Button(text='blue',
#                         foreground='white',
#                         background='blue',
#                         relief='flat',
#                         command=lambda: change_colour('blue')
#                         )

# green_button = tk.Button(text='green',
#                          foreground='white',
#                          background='green',
#                          relief='flat',
#                          command=lambda: change_colour('green')
#                          )

# black_button = tk.Button(text='black',
#                          foreground='white',
#                          background='black',
#                          relief='flat',
#                          command=lambda: change_colour('black')
#                          )

clear_button = tk.Button(text='Clear',
                         fg='black',
                         bg='#c4c4c4',
                         relief='flat',
                         command=lambda: clear(canvas)
                         )
# Place buttons horizontally above drawing area
save_button.grid(column=0, row=0)
# blue_button.grid(column=1, row=0)
# green_button.grid(column=2, row=0)
# black_button.grid(column=3, row=0)
clear_button.grid(column=4, row=0)

root.mainloop()
