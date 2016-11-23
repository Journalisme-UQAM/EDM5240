# coding: utf-8

import csv
import requests
from bs4 import BeautifulSoup

entetes = {
    "User-Agent":"Valérie Daraiche Pour un cours de journalisme",
    "From":"valerie.daraiche@gmail.com"
}

url = "http://www.csc-scc.gc.ca/divulgation-contrats/2015-2016/2015-2016_4-fra.shtml"

fichier = "contrats-services-correctionnels-JHR.csv"

contenu = requests.get(url,headers=entetes)
page = BeautifulSoup(contenu.text,"html.parser")
# print(page)

i = 0

for ligne in page.find_all("tr"):
    if i != 0:
        # print(ligne)
        
        lien = ligne.a.get("href")
        # print(lien)
        
        hyperlien = "http://www.csc-scc.gc.ca/divulgation-contrats/2015-2016/" + lien
        # print(hyperlien)

        contenu2 = requests.get(hyperlien, headers=entetes)
        page2 = BeautifulSoup(contenu2.text, "html.parser")
        # print(page2)

        contrat = []
        contrat.append(hyperlien)

        for item in page2.find_all("tr"):
            # print(item)

            if item.td is not None:
                contrat.append(item.td.text)
            else:
                contrat.append(None)
        
        print(contrat)
        
        dossier = open(fichier,"a")
        voila = csv.writer(dossier)
        voila.writerow(contrat)

    i = i + 1

# Ça marche!
# Bravo! Tu as appliqué la recette montrée en classe à un autre site.