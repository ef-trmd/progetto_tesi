#Calcolo delle bande
- kpath.pwscf: contiene il percorso nella zona di Brillouin Brillouin generato usando xcrysden selezionando i punti gamma - M (punto medio della cella primitiva esagonale del reticolo reciproco) - K (vertice della cella primitiva esagonale del reticolo reciproco) - gamma, campionato con 50 punti.

- alphabands.dat.gnu: contiene tutte le bande. Se non specificato, QE calcola 16 bande, anche oltre l'energia di Fermi che è pari a Ef = -0.6136 ev. Il grafico con le bande ottenute è all_bands.png

- around_Ef.dat.gnu: contiene solo le ultime 7 bande che si trovano in alphabands.dat.gnu, per evidenziare il comportamento attorno all'energia di Fermi (vedi around\_Ef.png)

##Risultati
- Solo una banda interseca il livello di Fermi contribuendo alla possibile conduzione. Da verificare che a questa banda contribuiscano stati elettronici che derivano dall'orbitale pz del boro come affermato nel paper: gli elettroni di conduzione non sono quelli che formano i legami in-plane tra gli atomi di boro.

- La banda immediatamente superiore non interseca il livello di Fermi per qualche decimo di eV e (a parte per la degenerazione in Gamma?) rimane nettamente separata dalla banda di conduzione (separazione massima tra i 5 e 6 eV)
