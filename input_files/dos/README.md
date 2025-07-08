#DOS
- Per il calcolo nscf raddoppio i k-points nella BZ, usando una griglia 18 x 18 x 1 e sommo gli stati su bin di energia deltaE = 0.1
- Con questa griglia si ottiene un energia di fermi pari a -0.483 eV (differisce di poco più di 0.1 eV dal valore di -0.6136 eV ottenuto con una griglia 9x9x1). Errore relativo del 20% suggerisce forse che una griglia 9x9x1 non è sufficientemente densa?
- PROBLEMA: la DOS presenta dei picchi che sembrano arificiale, dovuti ad una scelta sbagliata della griglia di k-points o della larghezza dei bin. Ho provato a renderla più uniforme con una griglia 36x36x1 e un bin deltaE=0.05 ma non ho ottenuto miglioramenti. Non risolvo nemmeno aumentando il parametro di smearing a degauss = 0.05

##file: alphados.dat i cui dati sono graficati nell'immagine dos.png per valori di energia compresi tra -20 e 5 ev

#PDOS

##Gli atomi 1,2,3,4,6,8 sono equivalenti
- Hanno 5 primi vicini, quindi le proiezioni in-plane della DOS sugli orbitali px e py hanno andamento diverso

##file: pdos_atoms123468.png

##Gli atomi 5 e 7 sono equivalenti
- Hanno 6 primi vicini, quindi le proiezioni in-plane della DOS sugli orbitali px e py coincidono

##file: pdos_atoms57.png

##Risultati
- Solo l'orbitale pz contribuisce alla densità degli stati in corrispondenza dell'energia di Fermi (normalizzata a 0 nei grafici): solo gli stati a più bassa energia che derivano dagli orbitali pz degli atomi di boro contribuiscono alla conduzione, producendo un comportamento metallico.
- La proiezione della DOS sugli orbitali che giacciono sul piano è nulla in corrispondenza dell'energia di Fermi: la struttura alpha risulta quindi stabile perché tutti gli stati bonding disponibili vengono rimepiti
