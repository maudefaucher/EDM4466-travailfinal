# Bonjour ! :-) Voici mon script pour mon projet final qui porte sur le lobbying climatique 👇

# coding: utf-8

import csv

# Je crée déjà tous mes fichiers qui me seront utiles pour mon moissonnage. Les fichiers primaire, sujets et titulaires sont les 3 fichiers CSV dans lesquels je moissonnerai. Le fichier climat sera mes résultats et la boucle vide lobbying climatique me permettra de .append des éléments des trois premiers fichiers à ma boucle. 
prim = "Primaire.csv"
sujets = "Sujets.csv"
titu = "Titulaires.csv"
clim = "lobbyingclimatique.csv"

# J'ai fait un premier test, je suis capable d'imprimer les lignes entières ainsi que seulement les COMLOG_ID de toutes les lignes. C'est un bon début ! :-)
# for primaire in primaires :
#     print(primaire)
#     print(primaire[0]) 

# Bon, je rencontre mon premier problème. J'essaie d'imprimer les COMLOG_ID du fichier sujets des lignes qui comprennent le mot "limat". Ça ne fonctionne pas. Lorsque je fais rouler mon script, ça n'imprime rien. Ça ne m'indique pas qu'il y a une erreur non plus. C'est comme si le script n'arrivait pas à aller chercher les informations que je demande. 
# for ligne in lignes2 :
#     if ligne[1] == "limat" or ligne[2] == "limat":
#         print(ligne[0])

# Je l'ai essayé avec deux formules et j'arrive toujours au même résultat : rien.
# for ligne in lignes2:
#     if ligne["SUBJ_MATTER_OBJET"] or ligne["OTHER_SUBJ_MATTER_AUTRE_OBJET"] == "limat":
#         print(ligne["COMLOG_ID"])

f2 = open(sujets, encoding="utf-8")
sujets = csv.reader(f2)

n=0
for sujet in sujets :
    if "limat" in sujet[1] or "limat" in sujet[2] : 
        # print(sujet[0])
        # Ça fonctionne ! Merci de l'aide !:-)
        
        # J'essaie d'extraire les COMLOG_ID du fichier Primaire qui sont identiques à ceux extraits du fichier Sujets juste en haut pour avoir les COMLOG_ID de climat dans le premier fichier. 
        # for primaire in primaires :
        #     if primaire[0] == sujet[0] : 
        #         n+=1
        #         print(n, primaire[0], primaire[1], primaire[2], primaire[3], primaire[7], sujet[1])
        # Ça ne fonctionne pas. Ça n'imprime qu'un seul résultat. Il est bon mais je suis censé en avoir plus de 9000 et je n'en ai qu'un. 

        # Après un appel qui m'a beaucoup aidé, j'ai compris qu'il fallait que je mette mon open(fichier) à l'intérieur de ma boucle afin que toutes les lignes soient lues par le script.
        f1 = open(prim, encoding="utf-8")
        primaires = csv.reader(f1)
        next(primaires)

        lobbyingclimatique = []
        for primaire in primaires : 
            if primaire[0] == sujet[0] :
                n+=1
                # print(n, primaire[0], "-", primaire[1], "-", primaire[2], "-", primaire[3], "-", primaire[7])
                
                # Je fais maintenant une liste qui regroupera toutes les infos dans le fichier csv.
                # Je .append tous les éléments que j'ai imprimé du fichier Primaires. C'est la première moitié de ma liste.
                # Mais avant tout, j'ouvre mon fichier f4 dans ma boucle. 
                f4 = open(clim, encoding="utf-8")
                climat = csv.writer(f4, delimiter=",")
                # Note à moi-même : les catégories à mettre dans le fichier csv lorsque je vais le manipuler sur Excel : "num id rapports", "num id clientsorganisationsentreprises", "nom ang", "nom fr", "date comm", "num id rapports", "poste TCPD comm", "autre inst", "inst"
                # J'imagine qu'il y une manière de le faire directement dans le script, mais je l'ignore. 

                lobbyingclimatique.append(primaire[0])
                lobbyingclimatique.append(primaire[1])
                lobbyingclimatique.append(primaire[2])
                lobbyingclimatique.append(primaire[3])
                lobbyingclimatique.append(primaire[7])

        # J'extrais maintenant les informations que je cherche du fichier Titulaires. Je m'y prends de la même façon que pour le fichier Primaires.
        f3 = open(titu, encoding="utf-8")
        titulaires = csv.reader(f3)

        for titulaire in titulaires :
            if titulaire[0] == sujet[0] :
                # n+=1
                # print(n, titulaire[0], "-", titulaire[3], "-", titulaire[5], "-", titulaire[6])
                
                # J'ajoute maintenant la deuxième partie de ma liste qui formera mon fichier cvs final.
                lobbyingclimatique.append(titulaire[0])
                lobbyingclimatique.append(titulaire[3])
                lobbyingclimatique.append(titulaire[5])
                lobbyingclimatique.append(titulaire[6])
                print(lobbyingclimatique)
                # Ça fonctionne ! :-)  

                justin = open(clim, "a")
                trudeau = csv.writer(justin)
                trudeau.writerow(lobbyingclimatique)