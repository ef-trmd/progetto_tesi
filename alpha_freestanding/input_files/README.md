#Organizzazione delle cartelle in input_files

- run_py: contiene gli script per testare la convergenza dei parametri. I file di output vengono salvati nelle rispettive cartelle denominate come il parametro da testare.
- read_py: contiene gli script che estraggono le energie totali dai file di output e le salvano in un file con estensione .dat in funzione del valore del parametro testato. I file con estensione .dat sono salvati nelle cartelle dei rispettivi parametri.
- crystal_images: contiene le immagini della struttura alpha generate con xcrysden

##Nell'ordine in cui è stata testata la convergenza (<1 meV/atomo):

- vacuum: distanza tra i piani di borofene (quanto vuoto serve affinché i piani siano isolati in buona approssimazione?)
- ecut: energia di cutoff
- k: densità della griglia di k-points che campiona la prima BZ
- degauss: parametro di smearing
- latticeparam: qui si trovano energie totali al variare di celldm(1), al variare di celldm(1) a diversi valori di ecut e al variare di celldm(1) con diverse griglie di k-points

##Calcolo cohesive energy
- cohesive-energy: contiene un input file alpha.scf.in con i valori dei parametri stabiliti dopo convergenza per calcolare l'energia della struttura cristallina e un input file isolated_B.scf.in per calcolare l'energia dell'atomo di boro isolato. compute_cohesive_energy.py calcola l'energia di coesione.

##Post-processing
- bands: calcolo delle bande
- dos: calcolo della DOS e della pDOS

#Unit cell
Si usa ibrav = 4, ossia una struttura esagonale, con cui si costruisce la unit cell indicata nella figura 1 del paper per la struttura alpha: 8 atomi di boro nelle coordinate indicate in ATOMIC_POSITIONS crystal, relative ai vettori primitivi definiti attraverso ibrav + celldm(1). Da notare che la cella unitaria così ottenuta è speculare orizzontalmente ripetto alla figura del paper (utile per capire la numerazione degli atomi nel calcolo della pdos).

