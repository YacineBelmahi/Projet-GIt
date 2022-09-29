#-------------------------------------------------------------------------------
# Name:        Gestion des utilisateurs Belemkasser Youness & Belmahi Yacine
# Purpose:
#
# Author:      Youness Belemkasser
#
# Created:     22/09/2021
# Copyright:   (c) Youness Belemkasser 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#Importation du module CSV
import csv
#Importation du module getpass
import random
import string
import hashlib ### hashage, MD5, SHA ect...

#Création d'un utilisateur pour le rajouter dans le fichier csv
continuer="oui"
while (continuer=="oui"):
    u=input("Saisiser le Nom de l'utilisateur :")
    p=input("Saisiser le Prénom de l'utilisateur :")
    a=u[0]
    l=a + p
    n1=input("Saisisez un mot de passe:")
    n2=input("Re saisisez le mot de passe pour verification:")

    #déclaration des variables dans une liste
    if n1!=n2:
            print("Les mots de passe ne correpondent pas, reesayer:");

            #vérifiacation de la similarité des mots de passes
            n1=input("Saisisez un mot de passe:")
            n2=input("Re saisisez le mot de passe pour verification:")
            while n1!=n2:
                print("Les mots de passe ne correspondent pas, reesayer:")
                n1=input("Saisisez un mot de passe:")
                n2=input("Re saisisez le mot de passe pour verification:")
            else:
                    print("Les mots de passe correspondent bien:")

    #hachage de Mots de passe
    salt="ESGI" #POUR MD5
    passwd_hashé=hashlib.md5(n1.encode()+salt.encode()).hexdigest()

    #Création d'un Fichier CSV
    with open('data2.csv','a',newline='', encoding='utf-8-sig') as fichiercsv:
        writer = csv.writer(fichiercsv)
        dict = {'Nom': u, 'Prénom': p, 'Login': l, 'Mots de passe hashé': passwd_hashé}
        writer.writerow([dict])

    continuer=input("Voulez vous ajouter un autre utilisateur ? Répondre oui ou non")


print("Les utilisateurs ont été ajoutés dans le fichier CSV qui a été crée a la racine du script")
