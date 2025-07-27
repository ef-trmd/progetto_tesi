#Calcolo della cohesive energy

##alpha.scf.in
- i parametri hanno i valori ottenuti dai test di convergenza

##isolated_B.scf.in
- Il codice è sttao eseguito con celldm(1)=20 bohr e celldm(1)= 30 bohr ottenendo lo stesso risultato: ciò significa che 20 bohr (10.6 Angstroms) sono una separazione sufficiente tra le copie di atomi di boro per calcolare le energie degli atmi isolati.
- Il boro ha tre elettroni di valenza, quindi può avere polarizzazione di spin non nulla: nspin=2, starting_magnetization = 1.0

- Per entrambi i calcoli SCF, pseudopotenziali e energie di cutoff sono gli stessi

##Risultati
alpha.scf.out:!    total energy              =     -49.98806847 Ry
isolated_B.scf.out:!    total energy              =      -5.80165049 Ry

Ecohesive = Eatom-Ebulk/8 = 6.072 eV/atomo, in buon accordo con quella indicata nel paper per la struttura alpha pari a 6.11 eV/atomo
