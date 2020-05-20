import tkinter as tk
from tkinter import filedialog, Text
import os
import pyodbc
counter = 1

root = tk.Tk()
root.title("DatingAAP")
root.geometry("600x400")
conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=DATINGAPP;'
                          'Database=datingapp;'
                          'UID=computerland;''PWD=P@ssw0rd')
cursor = conn.cursor()

cursor.execute("SELECT COUNT (*) FROM persgegevens")
lidnummercounter = cursor.fetchone()[0] + 1
lidnummercounter = str(lidnummercounter)

print (lidnummercounter)

def getTextInput():
    result=textExample.get(1.0, tk.END+"-1c")
    #cursor.execute("INSERT INTO persgegevens VALUES ("result," "lidnummercounter)")
    cursor.execute("INSERT INTO persgegevens (voornaam, lidnummer) VALUES('{}','{}')".format(result, lidnummercounter))
    #INSERT INTO persgegevens(voornaam, lidnummer) VALUES('henkk', '20201')
    conn.commit()


def buttonA():
    cursor.execute("INSERT INTO quizvragen (geslacht) VALUES(A)")
    conn.commit()

def buttonB():
    cursor.execute("INSERT INTO persgegevens (voornaam, lidnummer) VALUES (" +result+ ")")
    conn.commit()

textExample=tk.Text(root, height= 1)
textExample.pack()
btnRead=tk.Button(root, height=1, width=10, text="Naam", command=getTextInput)
btnRead.pack()

AntwoordA=tk.Button(root, height=2, width=20, text="A").place(x=10, y=350)


AntwoordB=tk.Button(root, height=2, width=20, text="B").place(x=440, y=350)


root.mainloop()




