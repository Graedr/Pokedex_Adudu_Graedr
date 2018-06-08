#! /usr/bin/python3
# -*- coding:utf-8 -*-

import main as mn
from os import listdir

necess = ["principal.py",
          "requetes.py",
          "main.py",
          "calculs.py",
          "interface.py",
          "textes.py",
          "dudermel-pons-projet.db",
          "effets.csv",
          "spe_phys_capa.csv"]


if __name__ == "__main__":
    dossier = listdir("./")
    for i in necess:
        assert i in dossier, "fichier manquant : " + i + "\nVoir rapport"
    mn.main()
