#! /usr/local/bin/python3
# -*- coding:utf-8 -*-

def charge_effets(nom):
    """charge la table des effets stockee dans nom
    nom : nom du fichier, doit etre en csv
    sortie : tableau a double entree
    sortie[i][j] retourne le coef multiplicateur de l'attaque de type
    i sur un type j"""
    with open(nom,encoding="utf8") as fichier:
        entree = fichier.readlines()
    sortie = []
    for ligne in entree:
        sortie.append([float(x) for x in ligne.split(",")])
    return sortie

table_effets = charge_effets("effets.csv")

def charge_spe(nom):
    """charge la table des specialisations (physique ou special)
    des types stockee dans nom
    nom : nom du fichier, doit etre en csv
    sortie : tableau a double entree"""
    with open(nom,encoding="utf8") as fichier:
        entree = fichier.readlines()
    sortie = []
    for ligne in entree:
        sortie.append([str(x) for x in ligne.split(",")])
    return sortie

table_spe = charge_spe("spe_phys_capa.csv")

test = ["antonin", "antigone", "antoine", "nicolas"]

def singulier(n):
    if n > 1:
        return "s"
    return ""

def similitudes(ch1,ch2):
    lim = min(len(ch1),len(ch2))
    i = 0
    while True:
        if not(i < lim and ch1[i]==ch2[i]):
            return i
        i += 1

def autocompletion(champ,nom=""):
    """autocompletion(champ,nom) retourne nom s'il se trouve dans champ, et
    sinon sélectionne les éléments commencant par nom, s'il n'y en a pas
    soulève une erreur de valeur, les affiche et propose a l'utilisateur de
    compléter nom, et rappelle autocomplétion avec nom complété et le champ
    des éléments commencant par nom
    précondition : champ liste de chaines, nom chaine (par défaut "") """
    if nom in champ:
        return nom
    
    ch = sorted([comp for comp in champ if (nom in comp) and
                 not(comp.index(nom))])
    nb_ent = len(ch)
    s = singulier(nb_ent)

    if nb_ent == 0:
        raise ValueError
    
    i = similitudes(ch[0],ch[-1])
    
    print("{0} entrée{1} correspondante{1} :".format(nb_ent,s))
    print(*ch,sep="\n")
    print("#"*10)

    nom = ch[0][:i]
    return autocompletion(ch,nom+input(nom))

