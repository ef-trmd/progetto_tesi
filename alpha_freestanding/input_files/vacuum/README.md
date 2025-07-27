#Convergenza distanza interplanare (vacuum)

##Viene testata la convergenza dell'energia totale al variare della separazione tra i piani 2D di borofene: si cerca la minima distanza a cui i piani possono essere considerati isolati in buona approssimazione

##Parametro testato: celldm(3) con valori tra 1.5 e 4.5 con step = 0.5.
- Fissato a = celldim(1) = 9.5 bohr, celldm(3) = c/a, da cui i valori testati sono c = celldm(3) *a sono compresi tra 7.5 e 22.6 Angstroms (ho fatto riferimento al fatto che nel paper si afferma che una separazione di 7.4 A è sufficiente alla convergenza).

##Risultati
- L'energia totale converge a meno di 1 meV/atomo per celldm(3)=2.0, che corrisponde ad una separazione di circa una decina di Angstroms.

##File: run_vacuum.py
