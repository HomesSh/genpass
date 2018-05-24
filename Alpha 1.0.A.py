import random

MAJ = [i for i in range(65,91)]
NOMBRES = [i for i in range(48,58)]
MINUSCULES = [i for i in range(97,123)]

add_maj = bool
add_min = bool
add_nb = bool

CARACTERES = []

nombre_caracteres = int(input('Nombre de caractères : '))
mot_de_passe = []

if input("MAJUSCULES: yes: y | no: n\n")== "y":
    presence_maj = True
    for l in range(len(MAJ)):
        CARACTERES.append(MAJ[l])
else : presence_maj = False

if input("NOMBRES: yes: y | no: n\n")== "y":
    presence_nombres = True
    for l in range(len(NOMBRES)):
        CARACTERES.append(NOMBRES[l])
else : presence_nombres = False


if input("MINUSCULES: yes: y | no: n\n")== "y":
    presence_min = True
    for l in range(len(MINUSCULES)):
        CARACTERES.append(MINUSCULES[l])
else : presence_min = False

for i in range(nombre_caracteres):
    x = random.randint(0, len(CARACTERES))
    mot_de_passe.append(CARACTERES[x])


if presence_nombres==True:
    for char in mot_de_passe:
        if char in NOMBRES==False:
            add_nb = True
 
    if add_nb==True:
        x = random.randint(0,len(mot_de_passe))
        y = random.randint(0,len(NOMBRES))
        mot_de_passe[x].replace(NOMBRES[y])

if presence_maj==True:
    for char in mot_de_passe:
        if char in MAJ==False:
            add_maj = True
 
    if add_maj==True:
        x = random.randint(0,len(mot_de_passe))
        y = random.randint(0,len(MAJ))
        mot_de_passe[x].replace(MAJ[y])

if presence_min==True:
    for char in mot_de_passe:
        if char in MINUSCULES==False:
            add_min = True
 
    if add_min==True:
        x = random.randint(0,len(mot_de_passe))
        y = random.randint(0,len(MINUSCULES))
        mot_de_passe[x].replace(MINUSCULES[y])


for i in range(len(mot_de_passe)):
    print(chr(mot_de_passe[i]),end="")

