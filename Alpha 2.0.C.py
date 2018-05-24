from random import*
from tkinter import*

app = Tk()
app.title("Projet")
#app['bg'] = "#3c3c3c"
app.geometry("300x300")

maj_var = IntVar()
min_var = IntVar()
nb_var = IntVar()
#mot_de_passe = StringVar() Affichage label
nb_caracteres = StringVar()

MAJ = [i for i in range(65,91)]
NOMBRES = [i for i in range(48,58)]
MINUSCULES = [i for i in range(97,123)]

add_maj = bool
add_min = bool
add_nb = bool

CARACTERES = [0,0]
mot_de_passe = []

global nombre_caracteres

def main():
    nombre_caracteres = int(nb_caracteres.get())
    presence_nombres = PRESENCE_NOMBRE()
    presence_min = PRESENCE_MAJUSCULE()
    presence_maj = PRESENCE_MINUSCULE()
    GENERATEUR(nombre_caracteres)
    if presence_nombres == True:
        FORCAGE_NOMBRE(presence_nombres, add_nb)
    if presence_maj == True:
        FORCAGE_MAJUSCULE(presence_maj, add_maj)
    if presence_min == True:
        FORCAGE_MINUSCULE(presence_min, add_min)
    AFFICHER_MDP()

titre = Label(app, text="Générateur de mots de passe", font='Helvetica 12 bold underline').pack(side=TOP)
bt = Button(app, text="Générer", command=main,).pack(side=BOTTOM)
maj_check = Checkbutton(app, text="Majuscules", variable=maj_var).pack(side=TOP)
min_check = Checkbutton(app, text="Minuscules",variable=min_var).pack(side=TOP)
nb_check = Checkbutton(app, text="Nombres", variable=nb_var).pack(side=TOP)
#mdp = Label(app, textvariable=mot_de_passe).pack(side=BOTTOM)
slide_caracteres = Scale(app, from_=4, to=25, orient=HORIZONTAL, variable=nb_caracteres).pack()

def GENERATEUR(nombre_caracteres):
    for i in range(nombre_caracteres):
        x = randrange(0, len(CARACTERES)-1)
        mot_de_passe.append(CARACTERES[x])

def PRESENCE_MAJUSCULE():
    if maj_var.get() == 1:
        presence_maj = True
        for l in range(len(MAJ)):
            CARACTERES.append(MAJ[l])
    else : presence_maj = False
    return presence_maj

def PRESENCE_NOMBRE():
    if nb_var.get() == 1:
        presence_nombres = True
        for l in range(len(NOMBRES)):
            CARACTERES.append(NOMBRES[l])
    else : presence_nombres = False
    return presence_nombres

def PRESENCE_MINUSCULE():
    if min_var.get() == 1:
        presence_min = True
        for l in range(len(MINUSCULES)):
            CARACTERES.append(MINUSCULES[l])
    else : presence_min = False
    return presence_min

def FORCAGE_NOMBRE(presence_nombres, add_nb):
    if presence_nombres==True:
        for char in mot_de_passe:
            if char in NOMBRES==False:
                add_nb = True
        if add_nb==True:
            x = randrange(0,len(mot_de_passe))
            y = randrange(0,len(NOMBRES))
            mot_de_passe[x].replace(NOMBRES[y])

def FORCAGE_MAJUSCULE(presence_maj, add_maj):
    if presence_maj==True:
        for char in mot_de_passe:
            if char in MAJ==False:
                add_maj = True
        if add_maj==True:
            x = randrange(0,len(mot_de_passe))
            y = randrange(0,len(MAJ))
            mot_de_passe[x].replace(MAJ[y])

def FORCAGE_MINUSCULE(presence_min, add_min):
    if presence_min==True:
        for char in mot_de_passe:
            if char in MINUSCULES==False:
                add_min = True
        if add_min==True:
            x = randrange(0,len(mot_de_passe))
            y = randrange(0,len(MINUSCULES))
            mot_de_passe[x].replace(MINUSCULES[y])

#faire la fonction de vérification

def AFFICHER_MDP():
    for i in range(len(mot_de_passe)):
        print(chr(mot_de_passe[i]),end="")
    print("")

        

if __name__ == '__main__':
    main()

app.mainloop()
