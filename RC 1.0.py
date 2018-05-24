import random # Importation de la bibliothèque random
import os # Importation de la bibliothèque os
MAJ = [i for i in range(65,91)] # Création d'une liste où se trouve les majuscules avec leurs nombres en ascii
NOMBRES = [i for i in range(48,58)] # Création d'une liste où se trouve les nombres avec leurs nombres en ascii
MINUSCULES = [i for i in range(97,123)] # Création d'une liste où se trouve les minuscules avec leurs nombres en ascii

add_maj = bool # Variable qui définies si l'utilisateur veut des majuscules
add_min = bool # Variable qui définies si l'utilisateur veut des minuscules
add_nb = bool  # Variable qui définies si l'utilisateur veut des nombres

CARACTERES = [] # Liste qui stocke tout les caractères qui vont être potentiellement utilisé dans le mot de passe
mot_de_passe = [] # liste dans laquelle se trouve le mot de passe
global nombre_caracteres # variable globale stockant le nombre de caractère voulus

#*****************************************
#*NOM : main c'est la fonction principale*
#***********ENTREES : aucune**************
#************SORTIE : aucune**************
#*****************************************
def main():
    restart = 'y' #Initialisation de la variable de remise en route du programme
    while restart == 'y': #Boucle tant que permettant de faire tourener le programme autant de fois que désiré
        nombre_caracteres = int(input('\nNombre de caractères : ')) #Commande demandant à l'utilisateur le nombre de caractères voulus
        print() #Permet un saut à la ligne pour un visuel plus confortable
        presence_nombres = PRESENCE_NOMBRE() #Variable faisant appel à la fonction PRESENCE_NOMBRE
        presence_maj = PRESENCE_MAJUSCULE() #Variable faisant appel à la fonction PRESENCE_MAJUSCULE
        presence_min = PRESENCE_MINUSCULE() #Variable faisant appel à la fonction PRESENCE_MINUSCULE
        GENERATEUR(nombre_caracteres) #Appel de la fonction qui va générer le mot de passe
        if presence_min == True: #Instruction vérifiant que l'utilisateur ait bien demandé la présence de minuscules
            FORCAGE_MINUSCULE(presence_min, add_min) #Appel de la fonction de forçage des minuscules
        if presence_maj == True: #Instruction vérifiant que l'utilisateur ait bien demandé la présence de majuscules
            FORCAGE_MAJUSCULE(presence_maj, add_maj) #Appel de la fonction de forçage des majuscules
        if presence_nombres == True: #Instruction vérifiant que l'utilisateur ait bien demandé la présence de nombres
            FORCAGE_NOMBRE(presence_nombres, add_nb) #Appel de la fonction de forçage des nombres
        print() #Permet un saut à la ligne pour un visuel plus confortable
        AFFICHER_MDP() #Appel de la fonction AFFICHER_MDP
        print() #Permet un saut à la ligne pour un visuel plus confortable
        ENREGISTRER() #Appel de la fonction d'enregistrement
        print() #Permet un saut à la ligne pour un visuel plus confortable
        REINITIALISATION() #Appel de la fonction de réinitialisation
        restart = input('Voulez vous regénérer un mot de passe : yes:y | no:n\n') #Instruction demandant à l'utilisateur si il veut recréer un mot de passe

#****************************************************************************************************************************************
#*NOM : PRESENCE_NOMBRE c'est la fonction qui permet de voir s'il faut des nombres et les ajoutes dans la liste de caractères a utilisés*
#*************************************ENTREES : aucune***********************************************************************************
#*****************************SORTIE : la varible presence_nombres qui dit s'il faut des nombres ****************************************
#****************************************************************************************************************************************
def PRESENCE_NOMBRE():
    if input("NOMBRES: yes: y | no: n\n")== "y": #Commande demandant à l'utilisateur si il a besoin de nombre dans son code
        presence_nombres = True #Variable stockant le choix de l'utilisateur positif
        for l in range(len(NOMBRES)): #Boucle permettant d'ajouter les nombres au caractères utilisable
            CARACTERES.append(NOMBRES[l])
    else : presence_nombres = False #Variable stockant le choix de l'utilisateur négatif
    return (presence_nombres) #retour de la vairable de choix

#**********************************************************************************************************************************************
#*NOM : PRESENCE_MAJUSCULE c'est la fonction qui permet de voir s'il faut des majuscules et les ajoutes dans la liste de caractères a utilisés*
#*************************************ENTREES : aucune*****************************************************************************************
#*****************************SORTIE : la varible presence_maj qui dit s'il faut des majuscules ***********************************************
#**********************************************************************************************************************************************
def PRESENCE_MAJUSCULE():
    if input("MAJUSCULES: yes: y | no: n\n")== "y": #Commande demandant à l'utilisateur si il a besoin de majuscules dans son code
        presence_maj = True #Variable stockant le choix de l'utilisateur positif
        for l in range(len(MAJ)): #Boucle permettant d'ajouter les majuscules au caractères utilisable
            CARACTERES.append(MAJ[l])
    else : presence_maj = False #Variable stockant le choix de l'utilisateur négatif
    return(presence_maj) #retour de la vairable de choix

#**********************************************************************************************************************************************
#*NOM : PRESENCE_MINUSCULE c'est la fonction qui permet de voir s'il faut des minuscules et les ajoutes dans la liste de caractères a utilisés*
#*************************************ENTREES : aucune*****************************************************************************************
#*****************************SORTIE : la varible presence_min qui dit s'il faut des minuscules ***********************************************
#**********************************************************************************************************************************************
def PRESENCE_MINUSCULE():
    if input("MINUSCULES: yes: y | no: n\n")== "y": #Commande demandant à l'utilisateur si il a besoin de minuscules dans son code
        presence_min = True #Variable stockant le choix de l'utilisateur positif
        for l in range(len(MINUSCULES)):#Boucle permettant d'ajouter les minuscules au caractères utilisable
            CARACTERES.append(MINUSCULES[l])
    else : presence_min = False #Variable stockant le choix de l'utilisateur négatif
    return (presence_min) #retour de la vairable de choix

#**************************************************************************************************************************
#******NOM : generateur c'est la fonction qui permet de nettoyer le message de l'utilisateur en enlevant les accents*******
#***************ENTREES : la variblable nombre_caracteres stockant le nombre de caractères dans le mot de passe************
#***********************************************SORTIE : aucune************************************************************
#**************************************************************************************************************************
def GENERATEUR(nombre_caracteres):
    for i in range(nombre_caracteres): #Boucle qui va caractère par caractère générer le mot de passe
        x = random.randint(0, len(CARACTERES)-1)#Commande associant à x de manière aléatoire un nombre (rang) compris dans la liste CARACTERES
        mot_de_passe.append(CARACTERES[x])#Commande associant le nombre de x au carctères qu'il représente et le stockant dans mot de mot_de_passe

#***************************************************************************************************************************
#*NOM : FORCAGE_NOMBRE c'est la fonction qui va obliger a mettre un nombre si c'est nécessaire******************************
#***********ENTREES : presence_nombres pour vérifier s'il faut des nombres et add_nb pour dire qu'il faut ajouter un nombre*
#****************************************************SORTIE : aucune********************************************************
#***************************************************************************************************************************
def FORCAGE_NOMBRE(presence_nombres, add_nb):
    if presence_nombres==True: #Vérification du choix de l'utilisateur quand à la présence de nombres
        for char in mot_de_passe: #char prend tour à tour chaque caractères de mot de passe
            if char in NOMBRES==False: #Vérification que la valeur de char se trouve dnas la liste nombres
                add_nb = True #Si il n'y en a pas add_nb devient vrai
        if add_nb==True: #Si add_nb est vrai
            x = random.randint(0,len(mot_de_passe)) # x prend un rang aléatoire dans mot de passe
            y = random.randint(0,len(NOMBRES)) # y prend une velaur aléatoire dans la liste des nombres
            mot_de_passe[x].replace(NOMBRES[y]) # au rang x le caractère prend la valeur de y

#**********************************************************************************************************************************
#*NOM : FORCAGE_MAJUSCULE c'est la fonction qui va obliger a mettre une majuscule si c'est nécessaire******************************
#***********ENTREES : presence_maj pour vérifier s'il faut des majuscules et add_maj pour dire qu'il faut ajouter une majuscule****
#****************************************************SORTIE : aucune***************************************************************
#**********************************************************************************************************************************
def FORCAGE_MAJUSCULE(presence_maj, add_maj):
    if presence_maj==True: #Vérification du choix de l'utilisateur quand à la présence de majuscules
        for char in mot_de_passe: #char prend tour à tour chaque caractères de mot de passe
            if char in MAJ==False: #Vérification que la valeur de char se trouve dnas la liste MAJ
                add_maj = True #Si il n'y en a pas add_maj devient vrai
        if add_maj==True: #Si add_maj est vrai
            x = random.randint(0,len(mot_de_passe)) # x prend un rang aléatoire dans mot de passe
            y = random.randint(0,len(MAJ)) # y prend une velaur aléatoire dans la liste des majuscules
            mot_de_passe[x].replace(MAJ[y]) # au rang x le caractère prend la valeur de y

#**********************************************************************************************************************************
#*NOM : FORCAGE_MINUSCULE c'est la fonction qui va obliger a mettre une minuscule si c'est nécessaire******************************
#***********ENTREES : presence_min pour vérifier s'il faut des minuscules et add_min pour dire qu'il faut ajouter une minuscule****
#****************************************************SORTIE : aucune***************************************************************
#**********************************************************************************************************************************
def FORCAGE_MINUSCULE(presence_min, add_min):
    if presence_min==True: #Vérification du choix de l'utilisateur quand à la présence de minuscules
        for char in mot_de_passe: #char prend tour à tour chaque caractères de mot de passe
            if char in MINUSCULES==False: #Vérification que la valeur de char se trouve dnas la liste MINUSCULES
                add_min = True #Si il n'y en a pas add_min devient vrai
        if add_min==True: #Si add_min est vrai
            x = random.randint(0,len(mot_de_passe)) # x prend un rang aléatoire dans mot de passe
            y = random.randint(0,len(MINUSCULES)) # y prend une velaur aléatoire dans la liste des minuscules
            mot_de_passe[x].replace(MINUSCULES[y]) # au rang x le caractère prend la valeur de y

#****************************************************************************
#*NOM : AFFICHER_MDP c'est la fonction qui permet d'afficher le mot de passe*
#******************************ENTREES : aucune******************************
#******************************SORTIE : aucune*******************************
#****************************************************************************
def AFFICHER_MDP():
    for i in range(len(mot_de_passe)): # i va prendre tour à tour chaque valeur du mot de passe
        print(chr(mot_de_passe[i]),end="") # affichage du mot de passe
    print("")#Permet un saut à la ligne pour un visuel plus confortable

#******************************************************************************************
#*NOM : ENREGISTRER c'est la fonction qui enregistre le mot de passe dans un fichier texte*
#******************************ENTREES : aucune********************************************
#******************************SORTIE : aucune*********************************************
#******************************************************************************************
def ENREGISTRER():
    if input("Voulez enregistrer le mot de passe ? yes: y | no: n\n")=="y": # Demande à l'utilisateur
        file = open("mot_de_passe.txt","w") # Création d'un fichier texte pour écrire à l'intérieur
        file.write("Votre mot de passe : ") # Inscription pour confort visuel
        for i in range(len(mot_de_passe)): # i va prendre tour à tour chaque valeur du mot de passe
            file.write(chr(mot_de_passe[i])) # Inscription du mot de passe dans le fichier texte

#**********************************************************************
#*NOM : REINITIALISATION c'est la fonction qui réinitialise les listes*
#**********************ENTREES : aucune********************************
#**************************SORTIE : aucune*****************************
#**********************************************************************
def REINITIALISATION():
    mot_de_passe[:] = [] #remise à zéro de la liste mot de passe
    CARACTERES[:] = [] #remise à zéro de la liste caractère

if __name__ == '__main__':
    main()
