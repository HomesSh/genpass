from tkinter import*

main = Tk()
main.title("Projet")
#main['bg'] = "#3c3c3c"
main.geometry("300x300")

maj_var = IntVar()
min_var = IntVar()
nb_var = IntVar()
mot_de_passe = StringVar()
nb_caracteres = StringVar()


def printmsg():
    print(nb_caracteres.get())
    
titre = Label(main, text="Générateur de mots de passe", font='Helvetica 12 bold underline').pack(side=TOP)
#wr = Entry(main,textvariable=entree).pack()
bt = Button(main, text="Générer", command=printmsg,).pack(side=BOTTOM)
maj_check = Checkbutton(main, text="Majuscules", variable=maj_var).pack(side=TOP)
min_check = Checkbutton(main, text="Minuscules",variable=min_var).pack(side=TOP)
nb_check = Checkbutton(main, text="Nombres", variable=nb_var).pack(side=TOP)
mdp = Label(main, textvariable=mot_de_passe).pack(side=BOTTOM)
slide_caracteres = Scale(main, from_=1, to=25, orient=HORIZONTAL, variable=nb_caracteres).pack()









main.mainloop()
