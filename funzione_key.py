import random

def key(grado, arrivo):
    if (grado==4 or grado==5 and random.random()<=1/3) or (grado==6 or grado==7 and random.random()<=2/3) or (grado==8 or grado==9):
        chiave=input("La porta è bloccata!") # Le risposte ammissibili sono: "chiave", "chiave speciale", "esci".
        if chiave=="chiave speciale":
            if grado==8:
                chiave=input("Quale chiave speciale stai usando?") # Le risposte ammissibili sono: "Chiave d'argento", "Chiave 8", "Chiave prismatica".
            elif (grado==4 or grado==5 or grado==6 or grado==7) and (arrivo=="lato sinistro" or arrivo=="lato destro"):
                chiave=input("Quale chiave speciale stai usando?") # Le risposte ammissibili sono: "Chiave del giardino segreto", "Chiave d'argento", "Chiave prismatica".
            else:
                chiave=input("Quale chiave speciale stai usando?") # Le risposte ammissibili sono: "Chiave d'argento", "Chiave prismatica".
    else: chiave="nessuna"
    return chiave