def converti(valore):
    TABELLA_RARITA = {2.94: "comune", 1.15: "standard", 0.45: "insolito", 0.23: "raro"}
    TABELLA_INVERSA = {valore: chiave for chiave, valore in TABELLA_RARITA.items()}
    if isinstance(valore, (int, float)):
        return TABELLA_RARITA.get(valore, "sconosciuto")
    elif isinstance(valore, str):
        return TABELLA_INVERSA.get(valore.lower(), None)