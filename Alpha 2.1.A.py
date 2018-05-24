import random # Importation de la bibliothèque random

MAJ = [i for i in range(65,91)] # Création d'une liste où se trouve les majuscules avec leurs nombres en ascii
NOMBRES = [i for i in range(48,58)] # Création d'une liste où se trouve les nombres avec leurs nombres en ascii
MINUSCULES = [i for i in range(97,123)] # Création d'une liste où se trouve les minuscules avec leurs nombres en ascii

add_maj = bool # Variable qui définies si l'utilisateur veut des majuscules
add_min = bool # Variable qui définies si l'utilisateur veut des minuscules
add_nb = bool  # Variable qui définies si l'utilisateur veut des nombres

CARACTERES = []
mot_de_passe = [] # liste dans laquelle se trouve le mot de passe
global nombre_caracteres # variable globale stockant le nombre de caractère voulus 

def main():
    nombre_caracteres = int(input('Nombre de caractères : '))
    presence_nombres = PRESENCE_NOMBRE()
    presence_maj = PRESENCE_MAJUSCULE()
    presence_min = PRESENCE_MINUSCULE()
    GENERATEUR(nombre_caracteres)
    if presence_min == True:
        FORCAGE_MINUSCULE(presence_min, add_min)
    if presence_maj == True:
        FORCAGE_MAJUSCULE(presence_maj, add_maj)
    if presence_nombres == True:
        FORCAGE_NOMBRE(presence_nombres, add_nb)
    AFFICHER_MDP()

def GENERATEUR(nombre_caracteres):
    for i in range(nombre_caracteres):
        x = random.randint(0, len(CARACTERES)-1)
        mot_de_passe.append(CARACTERES[x])

def PRESENCE_MAJUSCULE():
    if input("MAJUSCULES: yes: y | no: n\n")== "y":
        presence_maj = True
        for l in range(len(MAJ)):
            CARACTERES.append(MAJ[l])
    else : presence_maj = False
    return(presence_maj)

def PRESENCE_NOMBRE():
    if input("NOMBRES: yes: y | no: n\n")== "y":
        presence_nombres = True
        for l in range(len(NOMBRES)):
            CARACTERES.append(NOMBRES[l])
    else : presence_nombres = False
    return(presence_nombres)

def PRESENCE_MINUSCULE():
    if input("MINUSCULES: yes: y | no: n\n")== "y":
        presence_min = True
        for l in range(len(MINUSCULES)):
            CARACTERES.append(MINUSCULES[l])
    else : presence_min = False
    return (presence_min)

def FORCAGE_NOMBRE(presence_nombres, add_nb):
    if presence_nombres==True:
        for char in mot_de_passe:
            if char in NOMBRES==False:
                add_nb = True
        if add_nb==True:
            x = random.randint(0,len(mot_de_passe))
            y = random.randint(0,len(NOMBRES))
            mot_de_passe[x].replace(NOMBRES[y])

def FORCAGE_MAJUSCULE(presence_maj, add_maj):
    if presence_maj==True:
        for char in mot_de_passe:
            if char in MAJ==False:
                add_maj = True
        if add_maj==True:
            x = random.randint(0,len(mot_de_passe))
            y = random.randint(0,len(MAJ))
            mot_de_passe[x].replace(MAJ[y])

def FORCAGE_MINUSCULE(presence_min, add_min):
    if presence_min==True:
        for char in mot_de_passe:
            if char in MINUSCULES==False:
                add_min = True
        if add_min==True:
            x = random.randint(0,len(mot_de_passe))
            y = random.randint(0,len(MINUSCULES))
            mot_de_passe[x].replace(MINUSCULES[y])

def AFFICHER_MDP():
    for i in range(len(mot_de_passe)):
        print(chr(mot_de_passe[i]),end="")
    print("")

if __name__ == '__main__':
    main()
