#Convergenza del lattice parameter fissata ecut = 70 Ry e con una griglia di k-points 9x9x1

##Si cerca il minimo dell'energia totale al variare di celldm(1)

##Parametro testato: celldm(1) con valori compresi tra 9.0 e 10.0 Bohr con step = 0.2
- Si fa riferimento al risultato indicato nel paper per la lunghezza di legame della struttura alpha: impegando la GGA stimano che sia nel range 1.66-1.69 Angstrom (faccio riferimento a questo risultato perché lo pseudopotenziale scelto è una variante dei pseudopotenziali PBE (GGA) ottimizzata per i solidi)
- Si fa variare celldm(1) nell'intervallo indicato in modo da testare strutture con lunghezze di legame comprese tra 1.59 e 1.76 Angstroms.

##Risultati
- L'energia totale ha un minimo in corrispondenza di celldm(1) = 9.6 Bohr, a cui corrisponde una distanza di legame celldm(1)/3 pari a circa 1.69 A

##File: run_latticeparam.py



#Convergenza del latticeparameter con una griglia di k-points 9x9x1 a diverse energie di cutoff

##Parametro testato: celldm(1) con valori compresi tra 9.52 e 9.64 Bohr con step = 0.2 per ecut pari a 50, 60, 70, 80 Ry
- Si restringe l'intervallo attorno al valore di 9.6 Bohr ottenuto nel calcolo precedente, ma mantenendo comunque un range sufficientemente ampio ad avere un buon fit parabolico per trovare il minimo.

##Risultati
- Dagli andamenti nella figura convergence_latticeparam_ecut.png si vede che i minimi di energia corrispondono a valori disallineati di celldm(1) confrontando le enrgie di cutoff 60 e 70 Ry; sono invece allineati i minimi degli andamenti che corrispondono a 70 e 80 Ry. Ciò conferma che un'energia di cutoff pari a 70 Ry è una buona scelta.
- L'energia totale ha un minimo in corrispondenza di celldm(1) = 9.58 Bohr che corrisponde ad una lunghezza di legame pari a 1.69 A, in accordo col risultato indicato nel paper

##File: run_ecut_latticeparam.py, plot.py per i grafici



#Convergenza del latticeparameter fissata ecut= 70 Ry con diverse griglie di k-points

##Parametro testato: celldm(1) con valori compresi tra 9.52 e 9.64 Bohr con step = 0.2 con griglie 7x7x1, 8x8x1, 9x9x1, 10x10x1
- Si restringe l'intervallo attorno al valore di 9.6 Bohr ottenuto nel calcolo precedente, ma mantenendo comunque un range sufficientemente ampio ad avere un buon fit parabolico per trovare il minimo.

##Risultati
- Dagli andamenti nella figura convergence_latticeparam_k.png si vede che i minimi di energia corrispondono a valori disallineati di celldm(1) confrontando le griglie 7x7x1 e 8x8x1; gli altri andamenti hanno invece minimi allineati. Ciò conferma la buona scelta di una griglia 9x9x1.
- L'energia totale ha un minimo in corrispondenza di celldm(1) = 9.58 Bohr che corrisponde ad una lunghezza di legame pari a 1.69 A, in accordo col risultato precedente e con quello indicato sul paper

##File: run_k_latticeparam.py, plot_k.py per i grafici



