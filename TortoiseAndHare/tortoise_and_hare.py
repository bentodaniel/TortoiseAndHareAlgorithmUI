import tkinter as tk
from tkinter import messagebox
from tkinter import *
import random
import math

#
# Author: Daniel Bento
# 30/04/2020
#

#Creative commons - https://discuss.interviewbit.com/t/python-solution-floyds-tortoise-and-hare-algorithm-o-n-o-1-space/30895
def find_repeated_occurrence(array):
    tortoise = hare = array[0]

    # Keep advancing 'tortoise' by one step and 'hare' by two steps until they meet inside the loop.
    while True:
        tortoise = array[tortoise]
        hare = array[array[hare]]

        # Detected Cycle => (hare meets tortoise)
        if tortoise == hare:
                break

    # Send hare back to the start of array to evaluate the point of entrance to the cycle
    # Current tortoise position in the circle is the point of overlap when hare met the tortoise indicating presence of cycle.
    # Advance both of them at the same speed until they meet again.
    hare = array[0]
    while hare != tortoise:
        hare = array[hare]
        tortoise = array[tortoise]
    # The duplicate number must be the entry point of the circle when visiting the array again
    # Tortoise and hare meet again; the intersection index has the duplicate element.

    messagebox.showinfo("Operation Result","The operation finished successfully.\n\nThe repeated number is : " + str(hare))
    draw_main_window()


def find_repeated_occurrence_by_steps(array, canvas):
    global step
    global tortoise_rectangle
    global hare_rectangle
    global both_rectangle
    global t
    global h
    global t_h_meet

    canvas.delete(tortoise_rectangle)
    canvas.delete(hare_rectangle)
    canvas.delete(both_rectangle)

    if not t_h_meet:
        if step == 0:
            t = h = array[0]
            both_rectangle = draw_rectangle(canvas, 0, "blue")

        else:
            t_index = t
            h_index = array[h]

            t = array[t_index]
            h = array[h_index]

            # Detected Cycle => (hare meets tortoise)
            if t == h:
                t_h_meet = True
                both_rectangle = draw_rectangle(canvas,t_index,"blue")
                step = -1

            else:
                tortoise_rectangle = draw_rectangle(canvas,t_index,"green")
                hare_rectangle = draw_rectangle(canvas,h_index,"red")

        step += 1

    else:
        if step == 0:
            h = array[0]
            tortoise_rectangle = draw_rectangle(canvas,t,"green")
            hare_rectangle = draw_rectangle(canvas,0,"red")

        else:
            t_index = t
            h_index = h

            t = array[t_index]
            h = array[h_index]

            if t == h:
                both_rectangle = draw_rectangle(canvas,t_index,"blue")

                messagebox.showinfo("Operation Result","The operation finished successfully.\n\nThe repeated number is : " + str(h))
                draw_main_window()

            else:
                tortoise_rectangle = draw_rectangle(canvas,t_index,"green")
                hare_rectangle = draw_rectangle(canvas,h_index,"red")

        step += 1



def draw_rectangle(canvas, index, color):
    row = math.floor(index / 15)
    column = index % 15

    return canvas.create_rectangle((column*75) + 5, (row*75) + 5, (column*75) + 70, (row*75) + 70,outline=color,width=3)


def create_array_with_one_repeated(n_elements):
    repeated_index = random.randint(0, n_elements-1)

    array = list(range(1, n_elements))

    return array[:repeated_index] + [random.randint(1, n_elements-1)] + array[repeated_index:]

def display_array(array):
    n_rows = math.ceil(len(array) / 15)

    window_height = n_rows*75+30
    window_width = 15*75

    canvas = tk.Canvas(window,width=window_width,height=window_height)

    for i in range(n_rows+1):
        y = i * 75
        canvas.create_line(0, y, window_width, y,fill="#476042")

    for i in range(15):
        x = i * 75
        canvas.create_line(x, 0, x, window_height-30,fill="#476042")

    count = 0
    for i in range(n_rows):
        for j in range(15):
            grid_label = tk.Label(window,text=array[count])
            grid_label.config(font=('helvetica',11))

            x = (j+1) * 75 / 2 + (j * 75 / 2)
            y = (i+1) * 75 / 2 + (i * 75 / 2)
            canvas.create_window(x, y, window=grid_label)

            count += 1

            if count == len(array):
                break

    canvas.pack()

    restart_btn = tk.Button(text='Restart',command=draw_main_window,bg='brown',fg='white',font=('helvetica',9,'bold'))
    restart_btn.config(height=1,width=10)
    canvas.create_window(50,window_height-14,window=restart_btn)

    #Tortoise legend
    canvas.create_rectangle(145, window_height - 20, 155, window_height - 10, outline="green", width=3)
    label_tortoise = tk.Label(window,text='Tortoise')
    label_tortoise.config(font=('helvetica',10))
    canvas.create_window(190,window_height - 15,window=label_tortoise)

    #Hare legend
    canvas.create_rectangle(245,window_height - 20,255,window_height - 10,outline="red",width=3)
    label_hare = tk.Label(window,text='Hare')
    label_hare.config(font=('helvetica',10))
    canvas.create_window(280,window_height - 15,window=label_hare)

    #Both legend
    canvas.create_rectangle(345,window_height - 20,355,window_height - 10,outline="blue",width=3)
    label_hare = tk.Label(window,text='Both')
    label_hare.config(font=('helvetica',10))
    canvas.create_window(380,window_height - 15,window=label_hare)

    step_btn = tk.Button(text='>',command=lambda: find_repeated_occurrence_by_steps(array, canvas),bg='green',fg='white',font=('helvetica',9,'bold'))
    step_btn.config(height=1,width=5)
    canvas.create_window(window_width - 150,window_height - 14,window=step_btn)

    start_btn = tk.Button(text='Run',command=lambda: find_repeated_occurrence(array),bg='green',fg='white',font=('helvetica',9,'bold'))
    start_btn.config(height=1,width=10)
    canvas.create_window(window_width-50,window_height - 14,window=start_btn)


def start_tortoise_hare(value):
    try:
        array_n_elements = int(value)
        array = create_array_with_one_repeated(array_n_elements)

        for widget in window.winfo_children():
            widget.destroy()

        display_array(array)
    except Exception:
        messagebox.showerror("Error","Invalid value. Please use only numbers bigger or equal to 2.")


def draw_main_window():
    reset_globals()

    for widget in window.winfo_children():
        widget.destroy()

    canvas1 = tk.Canvas(window,width=500,height=300)
    canvas1.pack()

    label1 = tk.Label(window,text='Tortoise and Hare Algorithm Viewer')
    label1.config(font=('helvetica',14))
    canvas1.create_window(250,50,window=label1)

    label2 = tk.Label(window,text='Number of elements in the array:')
    label2.config(font=('helvetica',11))
    canvas1.create_window(250,150,window=label2)

    spinbox1 = Spinbox(window,from_=2,to=1000)
    canvas1.create_window(250,180,window=spinbox1)

    button1 = tk.Button(text='Quit',command=window.quit,bg='brown',fg='white',font=('helvetica',9,'bold'))
    button1.config(height=2,width=15)
    canvas1.create_window(150,260,window=button1)

    button2 = tk.Button(text='Start Algorithm',command=lambda: start_tortoise_hare(spinbox1.get()),bg='green',fg='white',
                        font=('helvetica',9,'bold'))
    button2.config(height=2,width=15)
    canvas1.create_window(350,260,window=button2)


def reset_globals():
    global step
    global tortoise_rectangle
    global hare_rectangle
    global both_rectangle
    global t
    global h
    global t_h_meet

    step = 0
    tortoise_rectangle = None
    hare_rectangle = None
    both_rectangle = None
    t = 0
    h = 0
    t_h_meet = False


window = tk.Tk()
window.title("Tortoise and Hare")
window.resizable(width=False,height=False)

step = 0
tortoise_rectangle = None
hare_rectangle = None
both_rectangle = None
t = 0
h = 0
t_h_meet = False

draw_main_window()

window.mainloop()
