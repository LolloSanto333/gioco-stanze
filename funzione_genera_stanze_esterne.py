import random

def genera_stanze_esterne_e_scegli(stanze_est, stanze_run, stanze_usate, benedizione, d, g, db):
    speciale=next((s for s in stanze_est if s["peso"] != 1), None)
    if speciale:
        speciale["peso"]=1
    opzioni=random.sample(stanze_est, 3)
    if speciale and speciale not in opzioni:
        opzioni[2]=speciale
    for s in opzioni: print(s["nome"])
    dadi=input("Vuoi utilizzare i dadi?") # Le risposte ammissibili sono "si" o "no"
    while dadi=="si":
        lista=[]
        for s in opzioni:
            stanze_est.remove(s)
            lista.append(s)
        opzioni=random.sample(stanze_est, 3)
        for s in lista: stanze_est.append(s)
        for s in opzioni: print(s["nome"])
        dadi=input("Vuoi utilizzare nuovamente i dadi?") # Le risposte sono "si" o "no"
    scelta=input("Quale stanza scegli?") # Le risposte ammissibili sono i nomi delle stanze in opzioni
    if scelta=="Schoolhouse":
        aula=next((s for s in stanze_run if s["nome"]=="Classroom"), None)
        if aula==None: aula=next((s for s in stanze_usate if s["nome"]=="Classroom"), None)
        for _ in range(8):
            stanze_run.append(aula)
    if scelta=="Shrine":
        benedizione=input("Quale benedizione?") # Le risposte ammissibili sono "Ballerino", "High Roller", "Giardiniere", "Generale", "Chef", "Monaco", "Raccoglitore di bacche", "nessuna"
        if benedizione!="nessuna":
            g=int(input("Per quanti giorni?")) # Le risposte ammissibili sono 3, 4, 5, 6, 7
            db=d+g-1
            if benedizione=="Giardiniere":
                giardino=next((s for s in stanze_run if s["nome"]=="Courtyard"), None)
                if giardino==None: giardino=next((s for s in stanze_usate if s["nome"]=="Courtyard"), None)
                for _ in range(8):
                    stanze_run.append(giardino)
    stanza_scelta=next(s for s in opzioni if s["nome"]==scelta)
    stanze_usate.append(stanza_scelta)
    return stanza_scelta, benedizione, g, db