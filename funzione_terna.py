from funzione_genera_stanze import genera_stanze
from funzione_genera_stanze_library import genera_stanze_library

def terna(d, st, partenza, arrivo, grado, chiave, stanze_run, stanze_library, stanze_usate):
    if d==1 and st==0:
        opzioni=[{"nome":"Bedroom"}, {"nome":"Closet"}, {"nome":"Hallway"}]
        for stanza in opzioni: print(stanza["nome"])
        return opzioni, 1
    else:
        if partenza=="HLC":
            targets={"Boudoir", "Walk-in Closet"}
            for s in stanze_run:
                if s["nome"] in targets: s["peso"]=2.94
            opzioni=genera_stanze("lato sinistro", arrivo, grado, chiave, stanze_run, stanze_usate)
            for stanza in opzioni: print(stanza["nome"])
            dadi=input("Vuoi utilizzare i dadi?") # Le risposte ammissibili sono "si" o "no"
            while dadi=="si":
                opzioni=genera_stanze("lato sinistro", arrivo, grado, chiave, stanze_run, stanze_usate)
                for stanza in opzioni: print(stanza["nome"])
                dadi=input("Vuoi utilizzare nuovamente i dadi?") # Le risposte sono "si" o "no"
            for stanza in stanze_run:
                if stanza["nome"]=="Boudoir" or stanza["nome"]=="Walk-in Closet": stanza["peso"]=1.15
        elif partenza=="RN":
            partenza=input("Dove ti trovi?")  # Le parole ammissibili sono: "lato sinistro", "interno", "lato destro"
            opzioni=genera_stanze(partenza, arrivo, grado, chiave, stanze_run, stanze_usate)
            if not any(d["nome"]=="Library" for d in opzioni):
                opzioni[2]={"nome":"Library"}
                if not any(d["nome"]=="Library" for d in stanze_usate): stanze_usate.append({"nome":"Library"})
            for stanza in opzioni: print(stanza["nome"])
            dadi=input("Vuoi utilizzare i dadi?") # Le risposte ammissibili sono "si" o "no"
            while dadi=="si":
                opzioni=genera_stanze(partenza, arrivo, grado, chiave, stanze_run, stanze_usate)
                if not any(d["nome"]=="Library" for d in opzioni):
                    opzioni[2]={"nome":"Library"}
                for stanza in opzioni: print(stanza["nome"])
                dadi=input("Vuoi utilizzare nuovamente i dadi?") # Le risposte sono "si" o "no"
        elif partenza=="Library" and (chiave=="chiave" or chiave=="nessuna"):
            partenza=input("Dove ti trovi?")  # Le parole ammissibili sono: "lato sinistro", "interno", "lato destro"
            opzioni=genera_stanze_library(partenza, arrivo, grado, chiave, stanze_library, stanze_usate)
            for stanza in opzioni: print(stanza["nome"])
            dadi=input("Vuoi utilizzare i dadi?") # Le risposte ammissibili sono "si" o "no"
            while dadi=="si":
                opzioni=genera_stanze_library(partenza, arrivo, grado, chiave, stanze_library, stanze_usate)
                for stanza in opzioni: print(stanza["nome"])
                dadi=input("Vuoi utilizzare nuovamente i dadi?") # Le risposte sono "si" o "no"
        elif partenza=="Tunnel":
            partenza=input("Dove ti trovi?")  # Le parole ammissibili sono: "lato sinistro", "interno", "lato destro"
            opzioni=genera_stanze(partenza, arrivo, grado, chiave, stanze_run, stanze_usate)
            opzioni[0]={"nome":"Tunnel"}
            for stanza in opzioni: print(stanza["nome"])
            dadi=input("Vuoi utilizzare i dadi?") # Le risposte ammissibili sono "si" o "no"
            while dadi=="si":
                opzioni=genera_stanze(partenza, arrivo, grado, chiave, stanze_run, stanze_usate)
                for stanza in opzioni: print(stanza["nome"])
                dadi=input("Vuoi utilizzare nuovamente i dadi?") # Le risposte sono "si" o "no"    
        else:
            opzioni=genera_stanze(partenza, arrivo, grado, chiave, stanze_run, stanze_usate)
            for stanza in opzioni: print(stanza["nome"])
            dadi=input("Vuoi utilizzare i dadi?") # Le risposte ammissibili sono "si" o "no"
            while dadi=="si":
                opzioni=genera_stanze(partenza, arrivo, grado, chiave, stanze_run, stanze_usate)
                for stanza in opzioni: print(stanza["nome"])
                dadi=input("Vuoi utilizzare nuovamente i dadi?") # Le risposte sono "si" o "no"
        return opzioni, 1