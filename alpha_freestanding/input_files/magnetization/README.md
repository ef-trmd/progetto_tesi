#simulazione struttura alpha lasciando libertà di polarizzazione di spin: il Boro ha 3 elettroni di valenza, quindi un elettrone rimane spaiato
in alpha.scf.in:
nspin = 2
starting_magnetization = 1

#Risultati
Nella sezione dell'ottava e ultima iterazione, in alpha.scf.out della cartella magnetization:

total magnetization       =     0.00 Bohr mag/cell
absolute magnetization    =     0.00 Bohr mag/cell

!    total energy              =     -49.98807193 Ry

differisce dall'energia totale calcolata senza iniziale polarizzazione di spin (in alpha.scf.out della cartella cohesive_energy):

!    total energy              =     -49.98806847 Ry

per meno di 1 meV/atomo: la differenza in energia totale del calcolo spin-polarizzato e non spin-polarizzato è trascurabile e pertanto la struttra alpha del borofene è non spin-polarizzata (in media il numero di elettroni spaiati con spin up è uguale a quello degli elettroni con spin down).
