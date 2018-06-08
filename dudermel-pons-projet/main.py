#! /usr/bin/python3
# -*- coding:utf-8 -*-

import textes as txt
import interface as it
import requetes as rq

def acc():
	it.menu([cherche_pokemon,
                 cherche_att,
                 strategie],
                txt.accueil)
			 
def cherche_pokemon():
	it.menu([chfr,chen,chty],txt.cherche_pokemon)
	return 1
	
def chfr():
	ident = it.recherche_simple("pokemon","nom",txt.nomfr)
	print(it.afficher_pokemon(ident))
	return 1

def chen():
	ident = it.recherche_simple("pokemon","nom_ang",txt.nomang)
	print(it.afficher_pokemon(ident))
	return 1
	
def chty():
        t = it.recherche_simple("type","nom",txt.nomty)
        ident = it.filtre_pokemon(t,txt.nomfr)
        print(it.afficher_pokemon(ident))
        return 1

def cherche_att():
        it.menu([chatt,chatty],txt.cherche_att)
        return 1

def chatt():
	ident =it.recherche_simple("capacite","nom",txt.nomatt)
	print(it.afficher_capacite(ident))
	return 1

def chatty():
        t = it.recherche_simple("type","nom",txt.nomtyatt)
        ident = it.filtre_capacite(t,txt.nomatt)
        print(it.afficher_capacite(ident))
        return 1

def strategie():
        it.menu([it.calc_degats,failles],
                txt.strategie)
        return 1

def failles():
        eq = it.equipe()
        print("Les pokémons suivants attaqueront avant vous :")
        print(*it.faille_vts(eq),sep = "\n")
        print()
        print("Votre équipe est faible contre :")
        print(it.faille_type(eq))
        return 1



def main():
	txt.commencer()
	print(txt.presentation)
	acc()
	print("merci d'avoir utilisé le pokedex du Pr.Chen")
	rq.conn.close()

if __name__ == "__main__":
        main()
