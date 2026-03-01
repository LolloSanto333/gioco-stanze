from dati_stanze import stanze
from dati_stanze import stanze_l
from dati_stanze import stanze_specchi_destro
from dati_stanze import stanze_specchi_sinistro
from dati_stanze import aggiunte_specchi
from dati_stanze import modifiche_cons
from dati_stanze import stanze_esterne
from funzione_key import key
from funzione_terna import terna
from funzione_genera_stanze_esterne import genera_stanze_esterne_e_scegli
from funzione_scegliere import scegliere
from funzione_converti import converti
from funzione_reset import reset
import random
import copy

def algoritmo_gioco():
    stanze_run=stanze[:]
    stanze_library=stanze_l[:]
    stanze_specchi_dx=stanze_specchi_destro[:]
    stanze_specchi_sx=stanze_specchi_sinistro[:]
    doppioni=aggiunte_specchi[:]
    mod_cons=modifiche_cons[:]
    stanze_est=stanze_esterne[:]
    stanze_usate=[{"nome":"Entrata"}, {"nome": "Anticamera"}]
    stanze_trovate=[]
    camb=[]
    obiettivo="no"
    benedizione="nessuna"
    col="blu"
    d=1
    st=0
    b=0
    h=0
    p=0
    o=0
    pa=0
    cl=0
    n=0
    g=0
    db=0
    while True:
        add=[]
        duplicati=[]
        stanze_run_cloi_agg=[]
        passi="si"
        q="no"
        a=0
        dx=0
        sx=0
        u=0
        pacco="no"
        while passi=="si":
            if stanze_run_cloi_agg!=[]:
                stanze_run=stanze_run_cloi_agg
                stanze_run_cloi_agg=[]
                if scelta in stanze_run:
                    stanze_run.remove(scelta)
            disegni=input("Devi aggiungere dal DS?") # Le risposte ammissibili sono "si" o "no"
            duplica=input("Devi duplicare dalla CM?") # Le risposte ammissibili sono "si" o "no"
            if disegni=="si":
                if a==0:
                    lista=[]
                    for stanza in stanze_run:
                        if stanza["pos_in"]==["STUDIO"]:
                            lista.append(stanza)
                    for i in range(1, 4):
                        pesi=[d["peso"] for d in lista]
                        s=random.choices(lista, weights=pesi, k=1)[0]
                        add.append(s)
                        lista.remove(s)
                        print(s["nome"])
                    a=1
                else:
                    for i in add:
                        print(i["nome"])
                q=input("Vuoi aggiungere?") # Le risposte ammissibili sono "si" o "no"
                if q=="si":
                    agg=input("Quale stanza vuoi aggiungere?") # Le risposte ammissibili sono i nomi che stanno in add
                    for stanza in stanze_run:
                        if stanza["nome"]==agg:
                            if agg=="Dovecote":
                                stanza["pos_in"]=["interno"]
                            else:
                                stanza["pos_in"]=["ovunque"]
                    for stanza in stanze_library:
                        if stanza["nome"]==agg:
                            if agg=="Dovecote":
                                stanza["pos_in"]=["interno"]
                                break
                            else:
                                stanza["pos_in"]=["ovunque"]
                                break
                    add=[s for s in add if s["nome"]==agg]
                continue
            if duplica=="si":
                angolo=input("Angolo destro o sinistro?") # Le risposte ammissibili sono "dx" o "sx"
                if angolo=="dx":
                    if dx==0:
                        lista=[]
                        for nome in stanze_specchi_dx:
                            originale=next((s for s in stanze_run if s["nome"]==nome), None)
                            if originale is None:
                                originale=next((s for s in stanze_usate if s["nome"]==nome), None)
                            if originale:
                                lista.append(copy.deepcopy(originale))
                        pesi=[s["peso"] for s in lista]
                        estratto_dx=random.choices(lista, weights=pesi, k=1)[0]
                        print(estratto_dx["nome"])
                        acc=input("Accetti il doppione?") # Le risposte ammissibili sono "si" o "no"
                        if acc=="si":
                            duplicati.append(estratto_dx)
                            stanze_run.append(estratto_dx)
                            stanze_specchi_dx.remove(estratto_dx["nome"])
                            if any(d["nome"]==estratto_dx["nome"] for d in stanze_library):
                                stanze_library.append(d)
                        dx=1
                    else:
                        print(estratto_dx["nome"])
                        acc=input("Accetti il doppione?") # Le risposte ammissibili sono "si" o "no"
                        if acc=="si":
                            duplicati.append(estratto_dx)
                            stanze_run.append(estratto_dx)
                            stanze_specchi_dx.remove(estratto_dx["nome"])
                            if any(d["nome"]==estratto_dx["nome"] for d in stanze_library):
                                stanze_library.append(d)
                if angolo=="sx": 
                    if sx==0:
                        lista=[]
                        for nome in stanze_specchi_sx:
                            originale=next((s for s in stanze_run if s["nome"]==nome), None)
                            if originale is None:
                                originale=next((s for s in stanze_usate if s["nome"]==nome), None)
                            if originale:
                                lista.append(copy.deepcopy(originale))
                        pesi=[s["peso"] for s in lista]
                        estratto_sx=random.choices(lista, weights=pesi, k=1)[0]
                        print(estratto_sx["nome"])
                        acc=input("Accetti il doppione?") # Le risposte ammissibili sono "si" o "no"
                        if acc=="si":
                            duplicati.append(estratto_sx)
                            stanze_run.append(estratto_sx)
                            stanze_specchi_sx.remove(estratto_sx["nome"])
                            if any(d["nome"]==estratto_sx["nome"] for d in stanze_library):
                                stanze_library.append(d)
                        sx=1
                    else:
                        print(estratto_sx["nome"])
                        acc=input("Accetti il doppione?") # Le risposte ammissibili sono "si" o "no"
                        if acc=="si":
                            duplicati.append(estratto_sx)
                            stanze_run.append(estratto_sx)
                            stanze_specchi_sx.remove(estratto_sx["nome"])
                            if any(d["nome"]==estratto_sx["nome"] for d in stanze_library):
                                stanze_library.append(d)
                continue
            B_U=input("Hai mangiato bacon e uova?") # Le risposte ammissibili sono "si" o "no"
            if B_U=="si":
                if b==0:
                    for stanza in stanze_run:
                        if stanza["nome"]=="Morning Room":
                            stanza["pos_in"]=["interno"]
                    for stanza in stanze_library:
                        if stanza["nome"]=="Morning Room":
                            stanza["pos_in"]=["interno"]
                    b=1
                else:
                    originale=next((s for s in stanze_run if s["nome"]=="Morning Room"), None)
                    originale_l=next(s for s in stanze_library if s["nome"]=="Morning Room")
                    if originale is None:
                        originale=next((s for s in stanze_usate if s["nome"]=="Morning Room"), None)
                    if originale:
                        duplicato=copy.deepcopy(originale)
                        stanze_run.append(duplicato)
                    if originale_l:
                        duplicato_l=copy.deepcopy(originale_l)
                        stanze_library.append(duplicato_l)
                continue
            aggi=input("Hai aggiornato?") # Le risposte ammissibili sono "si" o "no"
            if aggi=="si":
                aggiornamento=input("Quale stanza?") # Le risposte ammissibili sono "Spare Room", "Parlor", "Billiard Room", "Corridor", "Closet", "Nursery"
                if aggiornamento=="Spare Room":
                    nomi_mappa = {"rosa": "Spare Bedroom", "verde": "Spare Greenroom", "arancione": "Spare Hall"}
                    o=1
                    col=input("Che colore?") # Le risposte ammissibili sono "rosa", "verde", "arancione"
                    nuovo_nome=nomi_mappa.get(col)
                    originale=next((s for s in stanze_run if s["nome"]=="Spare Room"), None)
                    if originale: originale["colore"]=[col]
                    if col=="rosa": originale["nome"]="Spare Bedroom"
                    elif col=="verde": originale["nome"]="Spare Greenroom"
                    elif col=="arancione": originale["nome"]="Spare Hall"
                    if nuovo_nome:
                        if "Spare Room" in stanze_specchi_sx:
                            idx=stanze_specchi_sx.index("Spare Room")
                            stanze_specchi_sx[idx]=nuovo_nome
                        if "Spare Room" in doppioni:
                            idx=doppioni.index("Spare Room")
                            doppioni[idx]=nuovo_nome
                elif aggiornamento=="Parlor":
                    pa=1
                    originale=next((s for s in stanze_run if s["nome"]=="Parlor"), None)
                    if originale:
                        originale["colore"]=["rosso"]
                        originale["nome"]="Funeral Parlor"
                    if "Parlor" in stanze_specchi_dx:
                        index=stanze_specchi_dx.index("Parlor")
                        stanze_specchi_dx[index]="Funeral Parlor"
                    if "Parlor" in doppioni:
                        index=doppioni.index("Parlor")
                        doppioni[index]="Funeral Parlor"
                elif aggiornamento=="Billiard Room":
                    p=1
                    target=["Foyer", "Great Hall", "Secret Passage"]
                    for nome in target:
                        originale=next((s for s in stanze_run if s["nome"]==nome), None)
                        if originale is None:
                            originale=next((s for s in stanze_usate if s["nome"]==nome), None)
                        if originale:
                            duplicato=copy.deepcopy(originale)
                            stanze_run.append(duplicato)
                    originale=next((s for s in stanze_run if s["nome"]=="Billiard Room"), None)
                    if originale:
                        originale["colore"]=["arancione"]
                        originale["nome"]="Pool Hall"
                    if "Billiard Room" in stanze_specchi_dx:
                        index=stanze_specchi_dx.index("Billiard Room")
                        stanze_specchi_dx[index]="Pool Hall"
                    if "Billiard Room" in doppioni:
                        index=doppioni.index("Billiard Room")
                        doppioni[index]="Pool Hall"
                elif aggiornamento=="Corridor":
                    h=1
                    originale=next((s for s in stanze_run if s["nome"]=="Hallway"), None)
                    if originale is None:
                        originale=next((s for s in stanze_usate if s["nome"]=="Hallway"), None)
                        if originale:
                            duplicato=copy.deepcopy(originale)
                            stanze_run.append(duplicato)
                elif aggiornamento=="Closet":
                    cl=1
                    originale=next((s for s in stanze_run if s["nome"]=="Closet"), None)
                    if originale:
                        originale["colore"]=["rosso"]
                        originale["nome"]="Empty Closet"
                    if "Closet" in stanze_specchi_dx:
                        index=stanze_specchi_dx.index("Closet")
                        stanze_specchi_dx[index]="Empty Closet"
                    if "Closet" in doppioni:
                        index=doppioni.index("Closet")
                        doppioni[index]="Empty Closet"
                elif aggiornamento=="Nursery":
                    n=1
                    originale=next((s for s in stanze_run if s["nome"]=="Nursery"), None)
                    if originale:
                        originale["colore"]=["verde"]
                        originale["nome"]="Indoor Nursery"
                    if "Nursery" in doppioni:
                        index=doppioni.index("Closet")
                        doppioni[index]="Indoor Nursery"
                continue
            trov=input("Hai trovato una planimetria?") # Le risposte ammissibili sono "si" o "no"
            if trov=="si":
                name=input("Quale planimetria aggiungi?") # Le risposte ammissibili sono "Planetarium", "Mechanarium", "Throne Room", "Treasure Trove", "Tunnel", "Conservatory", "Lost & Found", "Closed Exhibit" 
                target=next((s for s in stanze_run if s["nome"]==name), None)
                target_l=next((sl for sl in stanze_library if sl["nome"]==name), None)
                if target: target["pos_in"]=["ovunque"]
                if target_l: target_l["pos_in"]=["ovunque"]
                stanze_trovate.append(target["nome"])
                continue
            partenza=input("Dove ti trovi?")  # Le parole ammissibili sono: "lato sinistro", "interno", "lato destro", "HLC", "RN", "Library", "CloAgg", "Tunnel", "esterno"
            arrivo=input("Dove vuoi andare?") # Le parole ammissibili sono: "lato sinistro", "interno", "lato destro", "esterno"
            if partenza=="esterno" and arrivo=="esterno":
                scelta, benedizione, g, db=genera_stanze_esterne_e_scegli(stanze_est, stanze_run, stanze_usate, benedizione, d, g, db)
            else:
                if partenza=="CloAgg":
                    stanze_run_cloi_agg=stanze_run[:]
                    partenza=="interno"
                    agg_clo=input("Quale?") # Le risposte ammissibili sono "Rynna" o "Draxus"
                    if agg_clo=="Rynna":
                        [stanza.update({"peso": 1.15}) for stanza in stanze_run if "verde" in stanza["colore"]]
                    elif agg_clo=="Draxus":
                        stanze_run=[s for s in stanze_run if s["porte"] in (1, 2)]
                grado=int(input("In quale grado vuoi andare?")) # Le parole ammissibili sono 1, 2, 3, 4, 5, 6, 7, 8, 9
                chiave=key(grado, arrivo)
                if chiave=="esci":
                    continue
                opzioni, st=terna(d, st, partenza, arrivo, grado, chiave, stanze_run, stanze_library, stanze_usate)
                scelta, pacco=scegliere(opzioni, stanze_run, stanze_library, stanze_usate, doppioni, mod_cons, camb, pacco)
            passi=input("Hai dei passi disponibili?") # Le risposte ammissibili sono "si" o "no"
            if passi=="no":
                d+=1
                obiettivo=input("Hai sbloccato la Room 46?") # Le risposte ammissibili sono "si" o "no"
        reset(stanze_run, stanze_library, stanze_usate, stanze_trovate, h, p, d, g, db, u, q, o, pa, cl, n, col, add, dx, sx, duplicati, obiettivo, camb, stanze_specchi_sx, stanze_specchi_dx, doppioni, pacco, benedizione, stanze_est)
algoritmo_gioco ()