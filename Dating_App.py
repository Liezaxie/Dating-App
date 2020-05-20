import tkinter as tk
from tkinter import *
from tkinter import filedialog, Text
import os
import pyodbc
import os.path

#Start tkinter en maakt connectie met de SQL Server.
root = tk.Tk()
root.title("DatingAAP")
root.geometry("600x400")
conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=DATINGAPP;'
                          'Database=datingapp;'
                          'UID=computerland;''PWD=P@ssw0rd')
cursor = conn.cursor()
cursor.execute("SELECT COUNT (*) FROM persgegevens")
vraagcounter = 1
nogeencounter = 0
lidnummercounter = cursor.fetchone()[0] + 1
lidnummercounter = str(lidnummercounter)
vraag =open('vragen.txt')
leesvraag =vraag.readlines()
canvas = Canvas(root, width = 290, height = 290)
canvas.pack()
img = PhotoImage(file="Tork.gif")
canvas.create_image(30,30, anchor=NW, image=img)


#print(lidnummercounter)


def getTextInput():
    result=textExample.get(1.0, tk.END+"-1c")
    textExample.delete("1.0", "end")
    #cursor.execute("INSERT INTO persgegevens (voornaam, lidnummer) VALUES('{}','{}')".format(result, lidnummercounter))
    #conn.commit()



def buttonA():
    global vraagcounter
    global nogeencounter
    #cursor.execute("INSERT INTO vragen (lidnummer, vraag, antwoord) VALUES('{}','{}','{}')".format(lidnummercounter,vraagcounter,"A"))
    #conn.commit()
    vraagcounter += 1

    print(vraagcounter)
    textExample.delete("1.0","end")
    textExample.insert(tk.END, leesvraag[nogeencounter+1])
    textExample.insert(tk.END, leesvraag[nogeencounter+ 2])
    textExample.insert(tk.END, leesvraag[nogeencounter+ 3])
    nogeencounter += 3


def buttonB():
    global vraagcounter
    global nogeencounter
    #cursor.execute("INSERT INTO vragen (lidnummer, vraag, antwoord) VALUES('{}','{}','{}')".format(lidnummercounter, vraagcounter,"B"))
    #conn.commit()
    vraagcounter += 1
    print(vraagcounter)
    textExample.delete("1.0", "end")
    textExample.insert(tk.END, leesvraag[nogeencounter+1])
    textExample.insert(tk.END, leesvraag[nogeencounter +2])
    textExample.insert(tk.END, leesvraag[nogeencounter +3])
    nogeencounter += 3

#def vragen():




textExample=tk.Text(root, height= 3)
textExample.insert(tk.END,leesvraag[nogeencounter])
textExample.pack()
btnRead=tk.Button(root, height=1, width=10, text="Bevestig", command=getTextInput)
btnRead.pack()
AntwoordA=tk.Button(root, height=2, width=20, text="A", command=buttonA).place(x=10, y=350)
AntwoordB=tk.Button(root, height=2, width=20, text="B", command=buttonB).place(x=440, y=350)


root.mainloop()




