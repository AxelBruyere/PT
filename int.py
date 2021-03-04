from tkinter import *

def test_bouton():
    print("J'ai appuyé sur le bouton")



root = Tk()
root.title('Contrôle du robot')

button_debut = Button(root, text="Début de l'épreuve", command = test_bouton, bg = '#C4C4C4',activebackground = '#AFAFAF',cursor = 'hand2')
button_debut.place(x = 5,y = 5, width = 140, height = 30) 

button_fin = Button(root, text="Fin de l'épreuve", command = test_bouton, bg = '#C4C4C4',activebackground = '#AFAFAF',cursor = 'hand2')
button_fin.place(x = 145, y = 5, width = 140, height = 30)

button_vitesse = Button(root, text="Vitesse", command = test_bouton, bg = '#C4C4C4',activebackground = '#AFAFAF',cursor = 'hand2')
button_vitesse.place(x = 285, y = 5, height = 30)

button_arret_urgence = Button(root, text="Arrêt d'urgence", command = test_bouton, bg = '#ff0000',activebackground = '#AFAFAF',cursor = 'hand2')











root.mainloop()

