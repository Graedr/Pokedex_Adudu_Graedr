#! /usr/bin/python3
# -*- coding:utf-8 -*-

import requetes as rq
import principal as pr
import textes as txt
import calculs as cc

table_effets = pr.table_effets

def retour():
	"""retourne au menu précédent"""
	print("Interface : retour arrière")
	return 0

#en Entrée

def entree(valeurs,texte=""):
	"""interaction simple avec l'utilisateur :
	lui demande d'entrer un élément dans valeurs
	en sortie : la valeur sélectionée"""
	ans = input(texte).title()
	return pr.autocompletion(valeurs,ans)

def recherche_simple(table,champ,texte=""):
	"""en entrée : un champ d'une table
	en sortie : l'id de l'élément du champ"""
	nom = entree(rq.charge_table(table,champ),texte)
	return rq.req_simple(table,champ,nom)[0]

def recherche_filtree(t,fonc,table,champ,texte=""):
	"""en entree un champ d'une table, un id t a filtrer et une fonction
        de filtre
	en sortie : l'id de l'élément du champ"""
	flt = fonc("filtre",t)
	print(*rq.charge_table(flt,"nom"),sep="\n",end="\n"*2)
	sortie = recherche_simple(flt, champ, texte)
	rq.detruire_filtre(flt)
	return sortie


def filtre_pokemon(t,texte=""):
        """effectue une recherche sur les pokémons dont le type est d'id t
        en sortie : l'id du pokémon résultat de la recherche"""
        return recherche_filtree(t,rq.filtre_poke,"pokemon","nom",texte)

def filtre_capacite(t,texte=""):
        """effectue une recherche sur les capacités dont le type est d'id t
        en sortie : l'id de la capacité résultat de la recherche"""
        return recherche_filtree(t,rq.filtre_cap,"capacite","nom",texte)
	
def calc_degats():
	"""gère les entrées/sorties pour le calculateur de dégâts"""
	print("Interface : Quel pokémon attaque ?\n")
	repAttq = recherche_simple("pokemon","nom",txt.nomfr)
	Attq = rq.strat_pokemon_att(repAttq)
	
	Niv_att = int(input(txt.niv))
	
	print("Interface : Quelle capacité utilise-t-il ?\n")
	repCapa = recherche_simple("capacite","nom",txt.nomatt)	
	capa = rq.strat_capacite(repCapa)

	print("Interface : Quel est le pokémon cible ?\n")

	repDef = recherche_simple("pokemon","nom",txt.nomfr)
	Def = rq.strat_pokemon_def(repDef)
	
	Niv_def = int(input(txt.niv))
	
	res = cc.calcul_degats(Attq,Niv_att,capa,Def,Niv_def)
	
	if isinstance(res,tuple):#fait des dégats de manière classique
		degatsMin,degatsMax = res
		print("\nInterface : Les dégâts causés par {}, lancé par {} sur {} sont les suivants :".format(
		 rq.id_est(repCapa,"capacite"),
		 rq.id_est(repAttq,"pokemon"),
		 rq.id_est(repDef,"pokemon")))
		print("Dégâts minimum causés : " + str(degatsMin))
		print("Dégâts maximum causés : " + str(degatsMax) + "\n")
	else:#a un effet particulier
		print("effet spécial :",end = " ")
		print(rq.effet_special(res))
	return 1

def equipe():
        """construit une équipe de pokémons dont les noms sont entrés par
        l'utilisateur. En sortie : une liste d'id"""
        sortie = []
        nb = ""
        while not(nb.isdigit() and 1 <= int(nb) < 7):
                nb = input("combien de pokémons dans l'équipe ? ")
        nb = int(nb)
        for k in range(nb):
                print("pokémon n° " + str(k+1))
                try:
                        ident = recherche_simple("pokemon","nom",txt.nomfr)
                        sortie.append(ident)
                except ValueError:
                        print("erreur en cours")
                        pass
        return sortie


def faille_type(equipe):
        """retourne les effets moyens des types contre l'équipe"""
        n = len(table_effets)
        eff = [0 for i in range(n-1)]
        for pok in equipe:
                t1,t2 = rq.strat_pokemon_att(pok)[2:]
                for i in range(n-1):
                        eff[i] += table_effets[i+1][t1] * table_effets[i+1][t2]
        eff = [i/len(equipe) for i in eff]
        table = list()
        for i,v in enumerate(eff,1):
                table.append((rq.id_est(i,"type"),v))
        table.sort(key=lambda x:x[1],reverse = True)
        sortie = ""
        for val in table:
                sortie += val[0].ljust(10) + str(val[1])[:4] + "\n"
        return sortie
###En Sortie

def afficher_pokemon(i):
        """retourne les informations du pokemon a partir de son id"""
        sortie = ""
        info = rq.info_pokemon(i)
        if info[-1] == "Aucun":
                sortie += txt.infopok1t.format(*info[:-1])
        else:
                sortie += txt.infopok2t.format(*(info))
        sortie += "\n"
        evol = rq.evolution(i)
        if evol:
                sortie += "évolue en :\n"
                for e in evol:
                        sortie += "{} si {}\n".format(*e)
        else:
                sortie += "n'évolue pas"
        return sortie

def afficher_capacite(i):
	"""retourne les informations de la capacité à partir de son id"""
	res = rq.info_capacite(i)
	if res[3] >= 0:
		return txt.infocap.format(*res)
	sortie = txt.infocapch.format(*res)
	sortie += "effet spécial : " + rq.effet_special(res[3])
	return sortie
##Divers

def faille_vts(equipe):
        """retourne le nom des pokémons plus rapides que tous les pokémons de
        l'équipe (où equipe est une liste d'id de pokémons)"""
        return rq.strat_rapide(rq.strat_equipe_vit(equipe))

def menu(L,doc):
	"""L est une liste de fonctions : menu(L,doc) affiche les docs 
        propose a l'utilisateur d'entrer un entier et
        exécute la fonction correspondante"""
	s = 1
	L = [retour] + L
	while s:
		print(txt.inter)
		for i,texte in enumerate(doc,1):
			print(str(i) + " : " + texte)
		print("0 : quitter")
		ent = input("choix ? ")
		print()
		if ent.isdigit() and int(ent) < len(L):
			try:
				s = L[int(ent)]()
			except ValueError:
				print("Erreur : pas de valeur correspondante")
		else:
			print("mauvais choix")
		print()


if __name__=="__main__":
	print(faille_type(equipe()))
	print("pour le programme en entier, lancer main")
