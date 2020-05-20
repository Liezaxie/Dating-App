import tkinter as tk
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
lidnummercounter = cursor.fetchone()[0] + 1
lidnummercounter = str(lidnummercounter)
vraag =open('vragen.txt')
leesvraag =vraag.readlines()

#print(lidnummercounter)


def getTextInput():
    result=textExample.get(1.0, tk.END+"-1c")
    #cursor.execute("INSERT INTO persgegevens (voornaam, lidnummer) VALUES('{}','{}')".format(result, lidnummercounter))
    #conn.commit()



def buttonA():
    global vraagcounter
    #cursor.execute("INSERT INTO vragen (lidnummer, vraag, antwoord) VALUES('{}','{}','{}')".format(lidnummercounter,vraagcounter,"A"))
    #conn.commit()
    vraagcounter += 1
    print(vraagcounter)
    textExample.delete("1.0","end")
    textExample.insert(tk.END, leesvraag[vraagcounter[1-2]])


def buttonB():
    global vraagcounter
    #cursor.execute("INSERT INTO vragen (lidnummer, vraag, antwoord) VALUES('{}','{}','{}')".format(lidnummercounter, vraagcounter,"B"))
    #conn.commit()
    vraagcounter += 1
    print(vraagcounter)
    textExample.delete("1.0", "end")
    textExample.insert(tk.END, leesvraag[vraagcounter - 1])

#def vragen():




textExample=tk.Text(root, height= 1)
textExample.insert(tk.END,leesvraag[vraagcounter-1])
textExample.pack()
btnRead=tk.Button(root, height=1, width=10, text="Bevestig", command=getTextInput)
btnRead.pack()
AntwoordA=tk.Button(root, height=2, width=20, text="A", command=buttonA).place(x=10, y=350)
AntwoordB=tk.Button(root, height=2, width=20, text="B", command=buttonB).place(x=440, y=350)


root.mainloop()




