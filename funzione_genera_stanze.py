from funzione_filtra_stanze import filtra_stanze
from funzione_estraz_stanze import estraz_stanze

def genera_stanze(i_pos, f_pos, grado, chiave, stanze_run, stanze_usate):
    stanze_valide=filtra_stanze(i_pos, f_pos, grado, chiave, stanze_run, stanze_usate)
    opzioni=estraz_stanze(stanze_valide, grado, chiave)
    return opzioni