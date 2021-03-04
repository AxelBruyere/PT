from tkinter import *

fen = Tk()
fen.title('Contrôle du robot')

lignes = []
for line in open("commandes.txt","r"):
    lignes.append(line)

lignes.pop(0)

for p in lignes:
    cmd = p.split(':')
    print(cmd)
    button = Button(fen,text = cmd[0]




fen.mainloop()
