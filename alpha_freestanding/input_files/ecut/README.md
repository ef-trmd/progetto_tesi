#Convergenza energia di cutoff (ecut)

##Viene testata la convergenza dell'energia totale al variare dell'energia di cutoff

##Parametro testato: ecut con valori tra 40 e 80 Ry con step = 10 Ry.
- Parto da 40 Ry perché nella descrizione del pseudopotenziale utilizzato si consiglia di usare un energia di cutoff non inferiore ai 43 Ry

##Risultati
- L'energia totale converge a meno di 1 meV/atomo per ecut = 70 Ry

##File: run_ecut.py
