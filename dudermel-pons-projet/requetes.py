#! /usr/bin/python3
# -*- coding:utf-8 -*-

import principal as pr
import sqlite3 as s
from os import listdir

LIMSECU = 12


class DangerError(ValueError):
	pass
	
def securite(chaine):
	"""estime si la chaine en entrée peut être une tentative d'injection
	de code, soulève l'erreur DangerError si c'est le cas"""
	if ";" in chaine or len(chaine) > LIMSECU:
		print("danger : tentative d'attaque détectée")
		raise DangerError
	return None


        
conn = s.connect("dudermel-pons-projet.db")
c = conn.cursor()

table_effets = pr.charge_effets("effets.csv")

def id_est(i,table):
    """va chercher le nom de l'élément d'id i de la table table
    i est un int
    !Version non sécurisée"""
    c.execute("""select nom from {} where id = ?;""".format(table),(i,))
    return c.fetchone()[0]

def evolution(i):
        """retourne la liste des noms des évolutions du pokémon d'id i"""

        request = """select evol.nom, condition from pokemon as bebe, \
        pokemon as evol, evolution where id_bebe = bebe.id and \
        evol.id = id_evolution and bebe.id = ?"""

        request = """select nom, condition from pokemon,evolution where \
        id_bebe = ? and id = id_evolution"""
        c.execute(request,(i,))
        res = c.fetchall()
        return res
    
def info_pokemon(i):
	"""retourne les infos de type d'un pokemon a partir de son id"""
	request = "select pokemon.nom, nom_ang, t1.nom, t2.nom from \
	pokemon, type as t1, type as t2 where \
	t1.id = type1 and t2.id = type2 and pokemon.id = ?;"
	c.execute(request,(i,))
	res = c.fetchone()
	return res

def info_capacite(i):
        """retourne les informations de la capacité d'id i
        à savoir le nom, le type, le nombre de PP, la puissance, la précision
        et une courte description de la capacité"""
        request = "select capacite.nom, type.nom, PP, Puissance, \
	Precision, Description from capacite, type where \
	type. id = capacite.type and capacite.id = ?"
        c.execute(request, (i,))
        res = c.fetchone()
        return res
	
def strat_pokemon_att(i):
	"""retourne les infos utiles à la stratégie pour les pokemons
	qui attaquent"""
	request = "select base_stat_att, base_stat_spe, type1, type2 \
	from pokemon where id = ?"
	c.execute(request, (i,))
	res = c.fetchone()
	return res	
	
def strat_pokemon_def(i):
	"""retourne les infos utiles à la stratégie pour les pokemons
	qui encaissent les dégâts"""
	request = "select base_stat_def, base_stat_spe, type1, type2 \
	from pokemon where id = ?"
	c.execute(request, (i,))
	res = c.fetchone()
	return res


def strat_equipe_vit(table_id):
        """retourne la vitesse du plus rapide des pokémons d'un équipe
        (d'id les éléments de table_id)
        Précondition : table_id est un tableau d'entiers de longueur
        6 au maximum"""

        request = """select max(base_stat_vts) from pokemon where id in {};"""
        c.execute(request.format(tuple(table_id)))
        res = c.fetchone()
        return res[0]


def strat_rapide(v):
        """retourne les noms de tous les pokémons plus rapides que la vitesse v"""
        request = """select nom from pokemon where base_stat_vts >= ?
        order by nom asc;"""
        c.execute(request,(v,))
        res = c.fetchall()
        res = [x[0] for x in res]
        #retourne des noms !!!
        return res
	
def strat_capacite(i):
	"""retourne les infos utiles a la sratégie pour la capacité
	frappante"""
	request = """select Puissance, type from capacite where id = ?"""
	c.execute(request, (i,))
	res = c.fetchone()
	return res

def effet_special(i):
	"""retourne les infos pour d'une capacité ayant un comportement
	spécial"""
	request = """select effet from atqspe where atqspe.id = ?"""
	c.execute(request, (i,))
	res = c.fetchone()
	return res[0]
    
def charge_table(table,champ):
    """charge toutes les valeurs de champ de la table
    Version non sécurisée"""
    securite(table);securite(champ)
    c.execute("""select {} from {} 
    order by id asc;""".format(champ,table))
    t = c.fetchall()
    t = [x[0] for x in t]
    return t

def req_simple(table,champ,valeur):
	"""Retourne l'id des éléments de table vérifiant champ = valeur
	prec:table doit etre un nom de table dans la base de données"""
	securite(table);securite(champ)
	req = "select id from {} where {} = ?""".format(table,champ)
	c.execute(req,(valeur,))
	t = c.fetchall()
	t = [x[0] for x in t]
	return t
	
def filtre_poke(nom,t):
    """crée une table provisoire filtretype contenant tous les pokemons
    dont l'id du type est t"""
    c.execute("""create view {} as select * from pokemon,type where
            (pokemon.type1 = type.id or pokemon.type2 = type.id )
            and type.id = {};""".format(nom,t))
    return nom

def filtre_cap(nom,t):
        c.execute("""create view {} as select * from capacite,type where
        capacite.type = type.id and type.id = {}""".format(nom,t))
        return nom

def detruire_filtre(nom):
        "supprime la vue nom"
        c.execute("""drop view {};""".format(nom))
        return None



def failles_strategiques(team):
    """regarde face a quel type l'equipe va morfler
    team : liste de 6 noms de pokemons"""
    c.execute("""select count(*) from type;""")
    n = c.fetchall()
    n = int(n[0][0])
    eff = [0 for i in range(n-1)]
    for pokemon in team:
        c.execute("""select type1,type2 from pokemon where \
        nom = ?""",(pokemon,))
        t1,t2 = c.fetchone()
        for i in range(n-1):
            eff[i] += table_effets[i][t1] * table_effets[i][t2]
    eff = [i/len(team) for i in eff]
    sortie = []
    for i,v in enumerate(eff,1):
        sortie.append((id_est(i,"type"), v))
    sortie.sort(key=lambda x:x[1],reverse = True)
    return sortie

try:
        detruire_filtre("filtre")
except s.OperationalError:
        pass

if __name__== "__main__":
    print(failles_strategiques(["Électhor","Sulfura","Artikodin"]))
    print(strat_rapide(strat_equipe_vit([1,42,3,143,101])))
    print("pour le programme en entier, lancer main")    
