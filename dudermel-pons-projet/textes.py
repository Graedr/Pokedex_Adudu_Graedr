#! /usr/bin/python3
# -*- coding:utf-8 -*-

"""Le script du programme : contient tous les textes des menus"""

def commencer():
    print(""" Inconnu : Bonjour ! Mon nom est Chen, mais tout le monde
m'appelle le Prof. Pokemon""")
    nom = input("Prof. Chen : Et toi, quel est ton nom ?\n")
    print("Ravi de te rencontrer, " + nom + " !")
    return None

presentation = """Ceci est le pokédex que j'ai passé ma vie à créer.
Il recense les  pokémons que tu pourras rencontrer à Kanto.
Tu es prêt ? Grâce à ce pokédex, tu vas pouvoir parcourir
la région sans difficultés !
Allez ! lance-toi dans le monde des pokémons !
Interface : Bienvenue dans ce moteur de recherche de pokédex.
"""

inter = "Interface : quelle action voulez-vous effectuer ?"

accueil = ["Rechercher un pokémon",
 "Rechercher une capacité",
 "Utiliser le logiciel stratégique"]

cherche_pokemon = ["Par nom ou début de nom en français",
 "Par nom ou début de nom en anglais","Par type"]
 
nomfr = "Interface : Entrez le nom ou début de nom du pokémon que \
vous cherchez.\n"
 
nomang = "Interface : Entrez le nom anglais ou début de nom \
anglais du pokémon que vous cherchez.\n"

nomty = "Interface : Entrez le type du pokémon recherché \n"

cherche_att = ["Par nom ou début de nom de capacité","Par type"]

nomatt = "Interface : Entrez le nom ou début de nom de la capacité \
que vous cherchez.\n"

nomtyatt = "Interface : Entrez le type de la capacité recherchée \n"

niv = "Interface : Entrez le niveau, entre 1 et 100, du pokémon.\n"

infopok1t = "{0} : de type {2}, en anglais {1}"
infopok2t = "{0} : de type {2} et {3}, en anglais {1}"

infocap = """{} : de type {}
PP : {} Puissance : {} Précision : {}
{}
"""

infocapch = """{0} : de type {1}
PP : {2} Précision : {4}
{5}
"""

strategie = ["Calculateur de dégâts","Failles stratégiques"]
