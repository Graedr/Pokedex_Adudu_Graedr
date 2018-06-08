#! /usr/bin/python3
# -*- coding:utf-8 -*-

import principal as pr

from math import sqrt

faiblesses = pr.table_effets
specificationsTypes = pr.table_spe
EVmin = 0
EVmax = 65535
IVmin = 0
IVmax = 15

def stat(IV,BS,EV,Niv):
	"""Calcule la statistique d'un pokémon de niveau Niv avec IV en valeur d'iv, EV points d'ev,
	BS en base stat
	Préconditions : IV est dans [[0,15]], EV dans [[0,65535]], BS est un entier, Niv est dans [[1,100]]"""

	return int((2*BS + IV + int(sqrt(EV+3)/4))*Niv/100) + 5

def degats(Niv,stat_off,pui,stat_def,STAB,type_capa,type1_cible,type2_cible):
	"""Calcule les dégâts faits par un pokémon de niveau Niv et de stat offensive stat_off, avec une
	capacité de puissance pui, de type type_capa et un stab STAB, sur un pokémon de stat défensive
	stat_def et de type type_cible"""

	multip_off = (Niv*0.4 + 2)*stat_off*pui
	multip_def = stat_def*50
	effic = faiblesses[type_capa][type1_cible]*faiblesses[type_capa][type2_cible]

	return int(((multip_off/multip_def)+2)*STAB*effic)


def calcul_degats(Attq,Niv_att,capa,Def,Niv_def):
	"""calcule les dégâts min et max
	Niv_att, Niv_def entiers entre 1 & 100
	Attq liste des valeurs d'attaque, de spe et de type de l'attaquant
	Def liste des valeurs de défense, de spé et de type du défenseur
	capa, liste des valeurs de puissance et de type de la capacité"""
	if Attq[2] == capa[1] or Attq[3] == capa[1] :
		STAB = 1.5
	else :
		STAB = 1

	if capa[0] < 0 :
		return capa[0]
		request = """select effet from capacite, atqspe where atqspe.id = Puissance and nom = ?"""
		c.execute(request, (repCapa,))
		res = c.fetchall()
		print("le jeu")
		print(res[0][0])
		return None

	elif capa[0] == 0 :
		degatsMin = 0
		degatsMax = 0

	else :
		if capa[1] in specificationsTypes[0]:
			spePkmnMin = stat(IVmin,Attq[1],EVmin,Niv_att)
			spePkmnMax = stat(IVmax,Attq[1],EVmax,Niv_att)
			spePkmn2Min = stat(IVmin,Def[1],EVmin,Niv_def)
			spePkmn2Max = stat(IVmax,Def[1],EVmax,Niv_def)
			degatsMin = int(degats(Niv_att,spePkmnMin,capa[0],spePkmn2Max,STAB,capa[1],Def[2],Def[3])*0.85)
			degatsMax = degats(Niv_att,spePkmnMax,capa[0],spePkmn2Min,STAB,capa[1],Def[2],Def[3])
				

		else :
			attPkmnMin = stat(IVmin,Attq[0],EVmin,Niv_att)
			attPkmnMax = stat(IVmax,Attq[0],EVmax,Niv_att)
			defPkmn2Min = stat(IVmin,Def[0],EVmin,Niv_def)
			defPkmn2Max = stat(IVmax,Def[0],EVmax,Niv_def)
			degatsMin = int(degats(Niv_att,attPkmnMin,capa[0],defPkmn2Max,STAB,capa[1],Def[2],Def[3])*0.85)
			degatsMax = degats(Niv_att,attPkmnMax,capa[0],defPkmn2Min,STAB,capa[1],Def[2],Def[3])
	return degatsMin,degatsMax
	
if __name__ == "__main__":
	print("lancez plutôt main")
