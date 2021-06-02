from tkinter import *
import math
from tkinter import font
from tkinter.font import Font as f

def evaluer(event):
     chaine.configure(text="bravo tu sais faire des math dani : reponse: "+str(eval(entree.get())))
     


#programme de math principal

fen = Tk()
fen.title("la calatrice de dani v1.0")
fen.geometry("480x550")
fen.config(background="grey")
fen.minsize(380, 450)
fen.maxsize(480, 550)
entree = Entry(fen,width=100)
entree.bind("<Return>", evaluer)
entree.config(font =f (size=15))
chaine = Label(fen, fg='green')
chaine.config(font= f(size=15))
entree.pack()
chaine.pack()
fen.mainloop()


