# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 22:29:31 2021

@author: patry
"""

#Zad 2


import tkinter as tk
import random

window = tk.Tk()
button_identities = []

def delete():
    entry.delete(0,tk.END)

def start_game():
    imie = entry.get()
    entry.destroy()
    name.destroy()
    dele.destroy()
    start.destroy()
    tk.messagebox.showinfo("Start Game", "Powodzena " + imie + "!!!")
    lbl_value.grid(row=0, column=1)
    losuj()

    
def losuj():
    global spr
    global los
    loss = random.randint(0, 8)
    los = tk.Label(master = frame1, fg ="white",font=("Courier", 44), text = button_colors.get(loss), bg=button_colors.get(loss))
    los.pack(pady=30)
    spr = button_colors.get(loss)

def increase():
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value + 1}"
    lbl_value["fg"] = "#003300"

def decrease():
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value - 1}"
    lbl_value["fg"] = "#990033"

def sprawdz(zmienna):
    if(zmienna == spr):
        increase()
    else:
        decrease()
    los.destroy()
    losuj()
    print(spr)
    print(zmienna)
    
button_colors = {
    0: "green",
    1: "red",
    2: "blue",
    3: "yellow",
    4: "pink",
    5: "brown",
    6: "purple",
    7: "gray",
    8: "orange",  
}
licznik = 0
frame1 = tk.Frame(master=window, width=100, height=50, bg="#212121")
frame1.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

frame2 = tk.Frame(master=window, width=100, height=50, bg="#616161")
frame2.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

frame3 = tk.Frame(master=window, width=100, height=50, bg="#616161")
frame3.pack(fill=tk.BOTH, side=tk.TOP, expand=True)


frame3.columnconfigure(0, weight=1, minsize=75)
frame3.rowconfigure(0, weight=1, minsize=50)


frame = tk.Frame(master=frame3, relief=tk.RAISED, borderwidth=1, background="black")
frame.grid(row=0, column=0, padx=5, pady=5)
button1 = tk.Button(master=frame, text=button_colors.get(0), bg = button_colors.get(0),width=25, height=5, command=lambda:sprawdz(button_colors.get(0)))
button1.pack(padx=5, pady=5)
frame = tk.Frame(master=frame3, relief=tk.RAISED, borderwidth=1, background="black")
frame.grid(row=0, column=1, padx=5, pady=5)
button2 = tk.Button(master=frame, text=button_colors.get(1), bg = button_colors.get(1),width=25, height=5, command=lambda:sprawdz(button_colors.get(1)))
button2.pack(padx=5, pady=5)
frame = tk.Frame(master=frame3, relief=tk.RAISED, borderwidth=1, background="black")
frame.grid(row=0, column=2, padx=5, pady=5)
button2 = tk.Button(master=frame, text=button_colors.get(2), bg = button_colors.get(2),width=25, height=5, command=lambda:sprawdz(button_colors.get(2)))
button2.pack(padx=5, pady=5)

frame3.columnconfigure(1, weight=1, minsize=75)
frame3.rowconfigure(1, weight=1, minsize=50)
frame = tk.Frame(master=frame3, relief=tk.RAISED, borderwidth=1, background="black")
frame.grid(row=1, column=0, padx=5, pady=5)
button1 = tk.Button(master=frame, text=button_colors.get(3), bg = button_colors.get(3),width=25, height=5, command=lambda:sprawdz(button_colors.get(3)))
button1.pack(padx=5, pady=5)
frame = tk.Frame(master=frame3, relief=tk.RAISED, borderwidth=1, background="black")
frame.grid(row=1, column=1, padx=5, pady=5)
button2 = tk.Button(master=frame, text=button_colors.get(4), bg = button_colors.get(4),width=25, height=5, command=lambda:sprawdz(button_colors.get(4)))
button2.pack(padx=5, pady=5)
frame = tk.Frame(master=frame3, relief=tk.RAISED, borderwidth=1, background="black")
frame.grid(row=1, column=2, padx=5, pady=5)
button2 = tk.Button(master=frame, text=button_colors.get(5), bg = button_colors.get(5),width=25, height=5, command=lambda:sprawdz(button_colors.get(5)))
button2.pack(padx=5, pady=5)

frame3.columnconfigure(2, weight=1, minsize=75)
frame3.rowconfigure(2, weight=1, minsize=50)
frame = tk.Frame(master=frame3, relief=tk.RAISED, borderwidth=1, background="black")
frame.grid(row=2, column=0, padx=5, pady=5)
button1 = tk.Button(master=frame, text=button_colors.get(6), bg = button_colors.get(6),width=25, height=5, command=lambda:sprawdz(button_colors.get(6)))
button1.pack(padx=5, pady=5)
frame = tk.Frame(master=frame3, relief=tk.RAISED, borderwidth=1, background="black")
frame.grid(row=2, column=1, padx=5, pady=5)
button2 = tk.Button(master=frame, text=button_colors.get(7), bg = button_colors.get(7),width=25, height=5, command=lambda:sprawdz(button_colors.get(7)))
button2.pack(padx=5, pady=5)
frame = tk.Frame(master=frame3, relief=tk.RAISED, borderwidth=1, background="black")
frame.grid(row=2, column=2, padx=5, pady=5)
button2 = tk.Button(master=frame, text=button_colors.get(8), bg = button_colors.get(8),width=25, height=5, command=lambda:sprawdz(button_colors.get(8)))
button2.pack(padx=5, pady=5)

        
name = tk.Label(master = frame1, fg ="white",font=("Courier", 44), text ="Name", bg="#212121")
entry = tk.Entry(master = frame1)
name.grid(row=0, column=0, sticky="ne")
entry.grid(row=1, column=0, sticky="ne", ipadx=10)
start = tk.Button(frame1, text = "start", command = start_game)
start.grid(row=2, column=0, sticky="ne", ipadx =55)
dele = tk.Button(frame1, text = "clear", command = delete)
dele.grid(row=3, column=0, sticky="ne", ipadx=54)

frame2.rowconfigure(0, minsize=50, weight=1)
frame2.columnconfigure([0, 1, 2], minsize=50, weight=1)


lbl_value = tk.Label(master=frame2, text="0",font=("Courier", 48), bg = "#616161")



window.mainloop()







