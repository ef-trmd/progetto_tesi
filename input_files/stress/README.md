#calcolo tensore di stress per unità di volume (Ry/bohr**3) per valori del lattice parameter compresi tra 9.52 e 9.64
in &control:
tstress = .true.

#Risultati
Il file stress.latticeparam.dat contiene nella prima colonna i valori del lattice parameter compresi tra 9.52 e 9.64 con i relativi valori diagonali del tensore di stress lungo x (\sigma-xx) e y(\sigma-yy) rispettivamente nella seconda e terza colonna. I valori sono espressi in energia per unità di volume e, come ci si aspetta dalla simmetria della struttura, i valori lungo x e lungo y coincidono.
Come atteso, lo stress si annulla in corrispondenza del valore del lattice parameter di poco superiore a 9.58 bohr, coerente con il valore del lattice parameter a cui corrisponde il minimo valore dell'energia totale (si veda immagine stress_latticeparam.png)
