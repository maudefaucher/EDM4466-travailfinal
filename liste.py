# Ici, je cherche simplement à avoir le nombre total de communications. 

# coding: utf-8

import csv
 
prim = "Primaire.csv"
sujets = "Sujets.csv"
titu = "Titulaires.csv"
clim = "lobbyingclimatique.csv"

f1 = open(prim, encoding="utf-8")
primaires = csv.reader(f1)

n=0
for primaire in primaires :
    n+=1
    print(n, primaire)

f2 = open(sujets, encoding="utf-8")
sujets = csv.reader(f2)

n=0
for sujet in sujets : 
    n+=1
    # print(n, sujet)

f3 = open(titu, encoding="utf-8")
titulaires = csv.reader(f3)

n=0
for titulaire in titulaires :
    n+=1
    # print(n, titulaire)