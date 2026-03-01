from funzione_filtra_stanze import filtra_stanze
import random

def genera_stanze_library (partenza, arrivo, grado, chiave, stanze_library, stanze_usate):
    stanze_valide=filtra_stanze(partenza, arrivo, grado, chiave, stanze_library, stanze_usate)
    opzioni=[]
    for i in range(1, 4):
        pesi = [d["peso"] for d in stanze_valide]
        s=random.choices(stanze_valide, weights=pesi, k=1)[0]
        opzioni.append(s)
        stanze_valide.remove(s)
    return opzioni