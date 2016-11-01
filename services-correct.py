# coding: utf-8

# j'ai d'abord créé mon environnement virtuel
# et je l'ai installé
# ensuite je l'ai activé
# j'ai finalement installé requests et BeautifulSoup4

import csv
import requests
from bs4 import BeautifulSoup

# Les entetes ci-dessous, c'est pour qu'on ne panique pas
# en voyant plusieurs milliers d'entrées simultanément
# quand j'aurai réussi à faire un fichier à la fin.
# Les responsables du site du gouvernement sauront que je ne suis
# pas en train de "hacker" leur site, puisque je me nomme 
# et j'écris la raison pourquoi je fais ça.


entetes = {
    "User-Agent":"Valérie Daraiche Pour un cours de journalisme",
    "From":"valerie.daraiche@gmail.com"
}

# L'URL du site duquel je veux créer un fichier est celui ci-bas

url = "http://www.csc-scc.gc.ca/divulgation-contrats/2015-2016/2015-2016_4-fra.shtml"

# quand je réussirai à faire le script et avoir toutes les données du tableau dans un meme fichier
# celui s'appellera "contrats-services-correctionnels.csv"
# tous les résultats de mon moissonnage sera dans ce fichier

fichier = "contrats-services-correctionnels.csv"

# avec l'aide de requests, j'obtiens tout le contenu de mon url
# dans une meme variable que j'appelle "contenu"


contenu = requests.get(url,headers=entetes)

page = BeautifulSoup(contenu.text,"html.parser")

# beautifulsoup rassemble tout le contenu texte qu'il y a dans l'url
# beautifulsoup l'analyse et met le résultat via la variable "page"

# print(page)

# en demandant la fonction print(page), j'obtiens tout le texte qu'il y a dans la page

# par contre, ce qui m'intéresse, c'est ce qu'il y a dans le tableau
# mais je ne veux pas inclure la première ligne du tableau
# parce qu'elle contient les entetes
# la variable "i" compte les lignes du tableau
# donc avec cette variable, je peux demander de ne pas s'occuper
# de la premiere ligne du tableau
# i = 0 c'est la première ligne du tableau, soit les entetes et je ne la veux pas

i = 0

# avec la boucle qui suit, je demande de voir chaque ligne du tableau
# les lignes du tableau sont toutes des éléments html qui sont "tr"
# mais je ne veux pas voir la ligne 0 du tableau, car ce sont les entetes
# je demande donc d'imprimer toutes les lignes qui ne sont pas égales à 0
# avec cette commande, j'aurai chaque ligne du tableau, sauf les entetes

for ligne in page.find_all("tr"):
    if i != 0:
        # print(ligne)
        
# mais ce qui m'intéresse surtout dans ce tableau, 
# c'est chaque lien (numéro de référence) qui mène aux détails de chaque contrat
# je veux surtout ces détails, je veux les rassembler pour m'éviter
# de cliquer sur chaque hyperlien individuellement
# donc je demande de recueillir ce lien
# le "a" de chaque ligne est l'hyperlien de celle-ci
        
        lien = ligne.a.get("href")
        # print(lien)
        
# le lien qui m'apparait n'est pas complet,
# alors je le complète avec la variable hyperlien
# j'ajoute le début de l'URL à la variable lien pour obtenir
# le lien complet de chaque ligne du tableau
# ce sont les deux dernières lignes de la boucle ci-dessus

        hyperlien = "http://www.csc-scc.gc.ca/divulgation-contrats/2015-2016/" + lien
        # print(hyperlien)
        
# je répète les memes étapes qu'au départ pour obtenir
# le contenu de mon hyperlien (grace a requests)
# et l'analyser (grace a beautifulsoup)
# cette analyse est placée dans la variable page2
# ces deux étapes ci-bas sont pour aller chercher
# tout le contenu de chaque hyperlien
# donc de chaque contrat
   
        contenu2 = requests.get(hyperlien, headers=entetes)
        page2 = BeautifulSoup(contenu2.text, "html.parser")
        # print(page2)
        
# je crée une liste pour mettre tout le contenu des contrats
        
        contrat = []
        
# la premiere chose que je mets dans ma liste
# c'est l'hyperlien de chaque contrat

        contrat.append(hyperlien)

# avec la boucle qui suit,        
# je vais chercher tous les items de chaque contrat
# chaque page est comme un mini tableau,
# donc je veux obtenir tous les éléments de chaque mini tableau
# tous les éléments des contrats sont des éléments html qui sont "tr"
# puisque je veux tous ces éléments, j'utilise la fonction find_all

        for item in page2.find_all("tr"):
            # print(item)
            
# si des cases du tableau sont vides,
# je veux qu'on me le dise
# pour m'éviter de chercher et de penser que ça a bogué
# alors je demande à ce que si c'est vide, d'ajouter NONE
# si ce n'est pas vide, je veux insérer le contenu de la case du tableau
# dans la liste contrat
# c'est ce que veut dire la condition qui suit

            if item.td is not None:
                contrat.append(item.td.text)
            else:
                contrat.append(None)
        
        print(contrat)
        
        dossier = open(fichier,"a")
        voila = csv.writer(dossier)
        voila.writerow(contrat)

    i = i + 1


    # contenu2 = requests.get(hyperlien, headers=entetes)
    # page2 = BeautifulSoup(contenu2.text, "html.parser")
    # contrat = []
    # contrat.append(hyperlien)


    


        
 
