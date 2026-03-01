def filtra_stanze (i_pos, f_pos, grado, chiave, stanze_run, stanze_usate):
    if i_pos=="Library":
        i_pos=input("Dove ti trovi?") # Le parole ammissibili sono: "lato sinistro", "interno", "lato destro"
    stanze_valide=[s for s in stanze_run if (s["pos_in"] == ["ovunque"] or i_pos in s["pos_in"]) and (s["pos_fin"] == ["ovunque"] or f_pos in s["pos_fin"])]
    target=["The Foundation", "Garage", "Boiler Room", "Sauna", "West Wing Hall", "East Wing Hall", "Secret Passage", "Greenhouse", "Morning Room", "Dormitory", "Throne Room"]
    if grado==1 or grado==9: stanze_valide=[s for s in stanze_valide if s.get("nome") not in target]
    else:
        stanze_valide=[s for s in stanze_valide if s.get("nome")!="Conservatory"]
        if grado==2 or grado==3: stanze_valide=[s for s in stanze_valide if (s.get("nome")!="The Foundation" and s.get("nome")!="Garage")]
    if chiave=="Chiave d'argento":
        stanze_valide=[s for s in stanze_valide if s.get("porte") in [3, 4] and s.get("nome") != "The Foundation"]
    if chiave=="Chiave prismatica":
        colore=input("La stanza dove ti trovi che colore è?") # Le risposte sono "verde", "arancione", "rosa", "rosso", "giallo", "altro"
        if colore!="altro":
            da_escludere=["Secret Passage", "Tunnel"] if colore=="arancione" else []
            stanze_valide=[s for s in stanze_valide if colore in s.get("colore", []) and s.get("nome") not in da_escludere]
    return(stanze_valide)