from dati_stanze import stanze
from dati_stanze import stanze_l
from dati_stanze import stanze_specchi_destro
from dati_stanze import stanze_specchi_sinistro
from dati_stanze import aggiunte_specchi
from dati_stanze import modifiche_cons
from dati_stanze import stanze_esterne

def reset(stanze_run, stanze_library, stanze_usate, stanze_trovate, h, p, d, g, db, u, q, o, pa, cl, n, col, add, dx, sx, duplicati, obiettivo, camb, stanze_specchi_sx, stanze_specchi_dx, doppioni, pacco, benedizione, stanze_est):
    stanze_trovabili=["Planetarium", "Mechanarium", "Throne Room", "Treasure Trove", "Tunnel", "Conservatory", "Lost & Found", "Closed Exhibit"]
    for stanza in stanze_run:
        if stanza["nome"]=="Morning Room" and stanza["pos_in"]=="interno":
            u+=1
    stanze_run=stanze[:]
    stanze_library=stanze_l[:]
    stanze_usate_due=[]
    if any(stanza["nome"]=="Freezer" for stanza in stanze_usate):
        stanza_da_togliere=next(s for s in stanze_run if s["nome"]=="Freezer")
        stanze_run.remove(stanza_da_togliere)
    if any(stanza["nome"]=="The Foundation" for stanza in stanze_usate):
        stanza_da_togliere=next(s for s in stanze_run if s["nome"]=="The Foundation")
        stanze_run.remove(stanza_da_togliere)
        stanze_usate_due.append(stanza_da_togliere)
    if any(stanza["nome"]=="The Pool" for stanza in stanze_usate):
        for stanza in stanze_run:
            if stanza["pos_in"]=="POOL":
                stanza["pos_in"]="ovunque"
    if g!=0 and d<=db:
        if benedizione=="Giardiniere":
            giardino=next(s for s in stanze_run if s["nome"]=="Courtyard")
            for _ in range(8):
                stanze_run.append(giardino)
        if benedizione=="Monaco":
            morte=input("In quale stanza hai terminato i passi?") # Le risposte ammissibili sono tutte le stanze in stanze_usate
            stanza_da_togliere=next(s for s in stanze_run if s["nome"]==morte)
            stanze_run.remove(stanza_da_togliere)
            stanze_est.append(stanza_da_togliere)
            stanza_da_togliere=next((s for s in stanze_library if s["nome"]==morte), None)
            if stanza_da_togliere: stanze_library.remove(stanza_da_togliere)
    stanze_usate=stanze_usate_due
    if q=="si" and add:
        for stanza in stanze_run:
            if stanza["nome"]==add[0]["nome"]:
                if stanza["nome"]=="Dovecote": stanza["pos_in"]==["interno"]
                else: stanza["pos_in"]==["ovunque"]
        for stanza in stanze_library:
            if stanza["nome"]==add[0]["nome"]:
                if stanza["nome"]=="Dovecote": stanza["pos_in"]==["interno"]
                else: stanza["pos_in"]==["ovunque"]
    if dx==1 or sx==1:
        for i in duplicati:
            if any(d["nome"]==i["nome"] for d in stanze_run):
                stanze_run.append(d)
            if any(d["nome"]==i["nome"] for d in stanze_library):
                stanze_library.append(d)
    if u!=0:
        stanze_run.remove({"nome":"Morning Room","pos_in":["B&U"],"pos_fin":["lato destro","lato sinistro"],"peso":0.23,"porte":2,"colore":["verde"]})
        stanze_library.remove({"nome":"Morning Room","pos_in":["B&U"],"pos_fin":["lato destro","lato sinistro"],"peso":3.85,"porte":2,"colore":["verde"]})
        for _ in range (u):
            stanze_run.append({"nome":"Morning Room","pos_in":["interno"],"pos_fin":["lato destro","lato sinistro"],"peso":0.23,"porte":2,"colore":["verde"]})
            stanze_library.append({"nome":"Morning Room","pos_in":["interno"],"pos_fin":["lato destro","lato sinistro"],"peso":3.85,"porte":2,"colore":["verde"]})
        b=1
    else: b=0
    for stanza in stanze_trovabili:
        if stanza in stanze_trovate:
            if any(room["nome"]==stanza for room in stanze_run):
                room["pos_in"]=["ovunque"]
            if any(room_l["nome"]==stanza for room_l in stanze_library):
                room_l["pos_in"]=["ovunque"]
    if h==1:
        stanze_run.append({"nome":"Hallway","pos_in":["ovunque"],"pos_fin":["ovunque"],"peso":2.94,"porte":3,"colore":["arancione"]})
    if p==1:
        stanze_run.append({"nome":"Secret Passage","pos_in":["ovunque"],"pos_fin":["ovunque"],"peso":0.45,"porte":1,"colore":["arancione"]})
        stanze_run.append({"nome":"Foyer","pos_in":["ovunque"],"pos_fin":["ovunque"],"peso":0.45,"porte":2,"colore":["arancione"]})
        stanze_run.append({"nome":"Great Hall","pos_in":["ovunque"],"pos_fin":["ovunque"],"peso":0.45,"porte":4,"colore":["arancione"]})      
        originale=next(s for s in stanze_run if s["nome"]=="Billiard Room")
        originale["colore"]=["rosso"]
        originale["nome"]="Pool Hall"
        originale=next(s for s in stanze_specchi_dx if s["nome"]=="Billiard Room")
        originale["nome"]="Pool Hall"
        originale=next(s for s in doppioni if s["nome"]=="Billiard Room")
        originale["nome"]="Pool Hall"    
    if o==1:
        originale=next((s for s in stanze_run if s["nome"]=="Spare Room"), None)
        originale["colore"]=[col]
        if col=="rosa": originale["nome"]="Spare Bedroom"
        elif col=="verde": originale["nome"]="Spare Greenroom"
        elif col=="arancione": originale["nome"]="Spare Hall"
        originale=next((s for s in stanze_specchi_sx if s["nome"]=="Spare Room"), None)
        if originale:
            if col=="rosa": originale["nome"]="Spare Bedroom"
            elif col=="verde": originale["nome"]="Spare Greenroom"
            elif col=="arancione": originale["nome"]="Spare Hall"
        originale=next((s for s in doppioni if s["nome"]=="Spare Room"), None)
        if originale:
            if col=="rosa": originale["nome"]="Spare Bedroom"
            elif col=="verde": originale["nome"]="Spare Greenroom"
            elif col=="arancione": originale["nome"]="Spare Hall"
    if pa==1:
        originale=next(s for s in stanze_run if s["nome"]=="Parlor")
        originale["colore"]=["rosso"]
        originale["nome"]="Funeral Parlor"
        originale=next(s for s in stanze_specchi_dx if s["nome"]=="Parlor")
        originale["nome"]="Funeral Parlor"
        originale=next(s for s in doppioni if s["nome"]=="Parlor")
        originale["nome"]="Funeral Parlor"
    if cl==1:
        originale=next(s for s in stanze_run if s["nome"]=="Closet")
        originale["colore"]=["rosso"]
        originale["nome"]="Empty Closet"
        originale=next(s for s in stanze_specchi_dx if s["nome"]=="Closet")
        originale["nome"]="Empty Closet"
        originale=next(s for s in doppioni if s["nome"]=="Closet")
        originale["nome"]="Empty Closet"
    if n==1:
        originale=next(s for s in stanze_run if s["nome"]=="Nursery")
        originale["colore"]=["verde"]
        originale["nome"]="Indoor Nursery"
        originale=next(s for s in doppioni if s["nome"]=="Nursery")
        originale["nome"]="Indoor Nursery"
    if camb!=[]:
        mappa_cambiamenti = {s["nome"]: s["peso"] for s in camb}
        for stanza in stanze_run:
            nome=stanza["nome"]
            if nome in mappa_cambiamenti:
                stanza["peso"]=mappa_cambiamenti[nome]
    if obiettivo=="si":
        for stanza in stanze_run:
            if stanza["pos_in"]==["Room 46"]: stanza["pos_in"]=["ovunque"]
        for stanza in stanze_library:
            if stanza["pos_in"]==["Room 46"]: stanza["pos_in"]=["ovunque"]
    elif d>=46:
        for stanza in stanze_run:
            if stanza["nome"]=="Gallery": stanza["pos_in"]=["ovunque"]
        for stanza in stanze_library:
            if stanza["pos_in"]==["Room 46"]: stanza["pos_in"]=["ovunque"]
    if pacco=="si":
        stanza=next(s for s in stanze_run if s["nome"]=="Mail Room")
        stanza["peso"]=2.94
        stanza=next(s for s in stanze_library if s["nome"]=="Mail Room")
        stanza["peso"]=0.05