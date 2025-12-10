#!/usr/bin/env python3

import sys

## Creer un nouveau programme exo.exam

## Objectif de l'exercice
###Lire un fichier TSV sequences_species.tsv où chaque ligne associe un ID de séquence à une espèce
### Regrouper les IDs par espèce et écrire un fichier de sortie listant
# pour chaque espèce, son nom précédé d’un # puis ses IDs sur les lignes suivantes

## Définir nos variables
#sequence_species.tsv = sys.argv[1]
#sequence_species.txt = sys.argv[2]
##Définir le chemin du fichier d'entrée (path) et le nom du fichier de sortie
path = "PYTHON_CIBIG25/files/sequences_especes.tsv"
out = "sequence_species.txt"

## Créer un dictionnaire vide nommé species_dico dont la clé est le nom de l'espèce et la valeur les ID
species_dico= {}
print(species_dico)

## Lire le fichier sequences_species.tsv
# Ouvrir le fichier en lecture et le parcourir ligne par ligne
with open(path, "r") as fd:
    for line in fd:
        data = line.strip().split("\t")
        if data[0] in species_dico:
            species_dico[data[0]].append(data[1])
        elif data[0] not in species_dico:
            species_dico[data[0]] = []

###Récupèrer les clés du dictionnaire et les trier ; sorted_dico est une liste des clés triées.
sorted_dico = sorted(species_dico.keys())

### Ouvrir le fichier de sortie en écriture
#Parcourt les clés triées et ecrire chaque ligne en commençant par # puis suivie de la clé
### Parcourt la liste d’éléments associée à la clé et écrit chaque élément sur une nouvelle ligne
###Écrire une ligne de séparateurs
with open(out, "w") as seq_txt:
    for key in sorted_dico:
        seq_txt.write(f"# {key}\n")
        for count in species_dico[key]:
            seq_txt.write(f"{count}\n")
        seq_txt.write(f"............\n")

