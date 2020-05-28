import tkinter as tk
from tkinter import *
from tkinter import filedialog, Text
import pyodbc
import numpy as np
from connection import *

#Start tkinter en maakt connectie met de SQL Server.
root = tk.Tk()
root.title("DatingAAP")
root.geometry("600x400")
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
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
    global nogeencounter
    result=textExample.get(1.0, tk.END+"-1c")
    textExample.delete("1.0", "end")
    cursor.execute("INSERT INTO persgegevens (voornaam, lidnummer) VALUES('{}','{}')".format(result, lidnummercounter))
    conn.commit()
    textExample.delete("1.0","end")
    textExample.insert(tk.END, leesvraag[nogeencounter+1])
    textExample.insert(tk.END, leesvraag[nogeencounter+ 2])
    textExample.insert(tk.END, leesvraag[nogeencounter+ 3])
    nogeencounter += 3

def buttonA():
    global vraagcounter
    global nogeencounter
    cursor.execute("INSERT INTO vragen (lidnummer, vraag, antwoord) VALUES('{}','{}','{}')".format(lidnummercounter,vraagcounter,"A"))
    conn.commit()
    vraagcounter += 1
    if vraagcounter > 22:
        antwoorden()
    print(vraagcounter)
    textExample.delete("1.0","end")
    if nogeencounter <= 64:
        textExample.insert(tk.END, leesvraag[nogeencounter+1])
        textExample.insert(tk.END, leesvraag[nogeencounter +2])
        textExample.insert(tk.END, leesvraag[nogeencounter +3])
        nogeencounter += 3

def buttonB():
    global vraagcounter
    global nogeencounter
    cursor.execute("INSERT INTO vragen (lidnummer, vraag, antwoord) VALUES('{}','{}','{}')".format(lidnummercounter, vraagcounter,"B"))
    conn.commit()
    vraagcounter += 1
    print(vraagcounter)
    if vraagcounter > 22:
        antwoorden()
    textExample.delete("1.0", "end")
    if nogeencounter <= 64:
        textExample.insert(tk.END, leesvraag[nogeencounter+1])
        textExample.insert(tk.END, leesvraag[nogeencounter +2])
        textExample.insert(tk.END, leesvraag[nogeencounter +3])
        nogeencounter += 3

def antwoorden():
    global lidnummercounter
    matchArray = np.array([1])
    counterteller = 1
    lidnummercounter = int(lidnummercounter)
    cursor.execute("SELECT COUNT (*) FROM vragen where lidnummer = '{}' and antwoord = '{}' ".format(lidnummercounter, "A"))
    antwoordenAJezelf = cursor.fetchone()[0]
    print("Dit ben ik zelf" + str(antwoordenAJezelf))
    textExample.delete("1.0", "end")

    for lid in range(lidnummercounter):
        cursor.execute("SELECT COUNT (*) FROM vragen where lidnummer = '{}' and antwoord = '{}' ".format(counterteller, "A"))
        antwoordenA = cursor.fetchone()[0]
        counterteller += 1
        matchArray = np.append(matchArray,antwoordenA)


    print("Dit is de matcharray "+ str(matchArray))
    searchval = antwoordenAJezelf
    matches = np.where(matchArray == searchval )[0]
    textMatch = tk.Text(canvas, height=15)
    textMatch.pack()
    print("Dit zijn de lidnummers" + str(matches))
    for i in range(len(matches)):
        cursor.execute("SELECT distinct persgegevens.voornaam FROM persgegevens INNER JOIN vragen ON persgegevens.lidnummer = vragen.lidnummer where persgegevens.lidnummer='{}'".format(matches[i]))
        Jegroteliefde= cursor.fetchone()[0]
        textMatch.insert(tk.END, "Je hebt een match met: " + Jegroteliefde + "\n")
        print(str(Jegroteliefde))
        i += 1
    textMatch.insert(tk.END, "\n" + "Je hebt een BONUS match met: Tjerk!!!!")

textExample=tk.Text(root, height= 3)
textExample.insert(tk.END,leesvraag[nogeencounter])
textExample.pack()
btnRead=tk.Button(root, height=1, width=10, text="Bevestig", command=getTextInput)
btnRead.pack()
AntwoordA=tk.Button(root, height=2, width=20, text="A", command=buttonA).place(x=10, y=350)
AntwoordB=tk.Button(root, height=2, width=20, text="B", command=buttonB).place(x=440, y=350)


root.mainloop()