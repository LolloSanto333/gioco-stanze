import random

def estraz_stanze(stanze_valide, grado, chiave):
    if chiave=="Chiave 8":
        risultato=[{"nome":"Room 8","pos_in":["ovunque"],"pos_fin":["ovunque"],"peso":0.23,"porte":2,"colore":["blu"]}]
    elif chiave=="Chiave del giardino segreto":
        risultato=[{"nome":"Secret Garden","pos_in":["ovunque"],"pos_fin":["lato destro", "lato sinistro"],"peso":0.23,"porte":3,"colore":["verde"]}]
    else:
        weights_temp=[]
        for stanza in stanze_valide:
            peso=stanza["peso"]
            if grado in [1, 2, 3] and peso==4:
                peso *= 10
            elif grado in [4, 5] and peso==3:
                peso *= 10
            elif grado in [6, 7] and peso==2:
                peso *= 10
            elif grado in [8, 9] and peso==1:
                peso *= 10
            weights_temp.append(peso)
        stanze_temp=stanze_valide.copy()
        risultato=[]
        for _ in range(min(3, len(stanze_temp))):
            scelta=random.choices(stanze_temp, weights=weights_temp, k=1)[0]
            index=stanze_temp.index(scelta)
            risultato.append(scelta)
            stanze_temp.pop(index)
            weights_temp.pop(index)
    return risultato