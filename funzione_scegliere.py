import random
from funzione_converti import converti

def scegliere (opzioni, stanze_run, stanze_library, stanze_usate, doppioni, mod_cons, camb, pacco):
    scelta=input("Quale stanza scegli?") # Le opzioni saranno i tre nomi delle stanze in opzioni
    stanza_scelta=next(s for s in opzioni if s["nome"]==scelta)
    dizionario_run_scelto=next((d for d in stanze_run if d["nome"]==stanza_scelta["nome"]), None)
    if dizionario_run_scelto==None: dizionario_run_scelto=next((d for d in stanze_usate if d["nome"]==stanza_scelta["nome"]), None)
    else:
        stanze_run.remove(dizionario_run_scelto)
        stanze_usate.append(dizionario_run_scelto)
    if scelta=="The Pool":
        for stanza in stanze_run + stanze_library:
            if stanza.get("pos_in")==["POOL"]: stanza["pos_in"]="ovunque"
    elif scelta=="Chamber of Mirrors":
        nuovi_doppioni=[]
        nuovi_doppioni_l=[]
        for stanza in stanze_run + stanze_usate:
            if stanza["nome"] in doppioni:
                duplicati=copy.deepcopy(stanza)
                nuovi_doppioni.append(duplicati)
        stanze_run.extend(nuovi_doppioni)
        for stanza in stanze_library:
            if stanza.get("nome") in doppioni:
                duplicati_l=copy.deepcopy(stanza)
                nuovi_doppioni_l.append(duplicato)
        stanze_library.extended(nuovi_doppioni_l)
    elif scelta=="Greenhouse":
        for s in stanze_run:
            if s["nome"]=="Secret Passage" or "verde" in s.get("colore", []): s["peso"]=1.15
    elif scelta=="Furnace":
        for s in stanze_run:
            if "rosso" in s.get("colore", []): s["peso"]=1.15
    elif scelta=="Solarium":
        for stanza in stanze_run:
            if stanza["peso"]==2.94: stanza["peso"]=0.23
            elif stanza["peso"]==1.15: stanza["peso"]=0.45
            elif stanza["peso"]==0.45: stanza["peso"]=1.15
            elif stanza["peso"]==0.23: stanza["peso"]=2.94
    elif scelta=="Conservatory":
        possibili=[]
        for stanza in stanze_run:
            if not stanza["nome"] in mod_cons:
                possibili.append(stanza)
        draft=random.sample(possibili, k=3)
        camb=[{"nome": s["nome"], "rarità": converti(s["peso"])} for s in draft]
        mod="si"
        while mod=="si":
            for elemento in camb:
                print(elemento["nome"], elemento["rarità"])
            sta=input("Quale stanza vuoi cambiare?") # Le risposte ammissibili sono i nomi degli elementi in nuova_lista
            pes=input("Quale rarità scegli?") # Le risposte ammissibili sono "comune", "standard", "insolito", "raro"
            for elemento in camb:
                if elemento["nome"]==sta:
                    elemento["rarità"]=pes
            nuovo_peso=converti(pes)
            for stanza in stanze_run:
                if stanza["nome"]==sta:
                    stanza["peso"]=nuovo_peso
            mod=input("Vuoi modificare altro?") # Le risposte ammissibili sono "si" o "no"
    elif scelta=="Mail Room":
        pacco=input("Hai spedito un pacco?")
    return dizionario_run_scelto, pacco