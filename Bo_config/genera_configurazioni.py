import os
import numpy as np
from itertools import combinations

L = 6  # dimensione della griglia: 6x6 triangoli
primi_vicini = [(-1, -1), (0, -1), (1, 0), (-1, 0), (0, 1), (1, 1)]
#lista che contiene le posizioni dei primi vicini relative al sito di riferimento


def modulo(i):
    """
    Funzione modulo: usata nel calcolo dei primi vicini per tenere conto delle PBC
    Input:
        i (intero): indice di posizione, assume valori nell'intervallo [-1,6]
    Parametri:
        L (intero): dimensione della griglia
    Returns:
        intero: sostituisce i valori di input i=-1 e i=6 con 6 -> 0 e -1 -> 5
    """
    return i % L

def ha_vicini(combinazione):
    """
    Verifica se nella combinazione in input ci sono buchi vicini (inclusi vicini con PBC)
    Input:
        combinazione (tupla): contiene le coordinate (i,j) dei buchi
    Returns:
        bool: restituisce True se trova due buchi vicini, False se non li trova
    """

    #per ciascun buco, controllo se uno o più dei suoi primi vicini si trova nella combinazione
    for i, j in combinazione:
        for di, dj in primi_vicini:
            ni = modulo(i + di)
            nj = modulo(j + dj)
            if (ni, nj) in combinazione:
                return True
    return False
    
def genera_configurazioni(n_buchi, cartella_output):
    """
    Generare configurazioni valide per un dato n_buchi
    Input:
        N-buchi (intero): numero di vacanze (da 1 a 9)
        output_dir (stringa): percorso della cartella dove salvare le configurazioni
    Returns:
        tot_config (intero): numero totale di configurazioni permesse con N_buchi
    """
    #genero percorso cartella se non esiste già
    os.makedirs(cartella_output, exist_ok=True)
    #costruisco matrice 6x6 di 1 che rappresentano tutti i siti occupati della griglia 6x6
    griglia = [(i, j) for i in range(L) for j in range(L)]
    tot_config = 0

    #genero tutte le combinazioni di n_buchi e controllo quali di queste sono valide
    for combinazione in combinations(griglia, n_buchi):
        if ha_vicini(combinazione):
            continue
        #se la configurazione è valida, le entrate che corrispondono alle posizioni dei buchi vengono trasformate in 0, ossia siti vuoti della griglia
        matrice = np.ones((L, L), dtype=int)

        for (i, j) in combinazione:

            matrice[i, j] = 0

        #nella cartella {n}_vacancies creo un file per ciascuna configurazione ("B coord_x coord_y coord_z")
        #se n_buchi=2 e il file contiene la configurazione con buchi in (1,1) e (3,4), il file viene denominato "(1,1)_(3,4).dat"
        nomefile = "_".join(f"({i},{j})" for (i, j) in combinazione)
        filepath = os.path.join(cartella_output, f"{nomefile}.dat")
        with open(filepath, 'w') as f:
            for x in range(L):
                for y in range(L):
                    #se le entrate (x,y) della matrice sono 1 (sito pieno): (coord_x, coord_y, coord_z) = (1/6*x, 1/6*y, 0.400000)
                    #se le entrate (x,y) della matrice sono 0 (sito vuoto): non scrivo niente
                    if matrice[x, y] == 1:
                        f.write(f"B  {x / L:.6f}  {y / L:.6f}  0.400000\n")
        #conteggio le configurazioni
        tot_config += 1

    print(f"{tot_config} configurazioni permesse trovate con n_buchi = {n_buchi} in '{cartella_output}'.")
    return tot_config

#Genero una cartella contenente le configurazioni per ciascun numero di buchi (da 1 a 9)
for n_buchi in range(1, 10):
    cartella = f"./allowed_config/{n_buchi}_vacancies"
    genera_configurazioni(n_buchi, cartella)
