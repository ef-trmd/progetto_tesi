set terminal pngcairo size 1000, 700 enhanced font "Arial, 14"
set output "pdos_px.png"

set title "confronto DOS proiettate su borofene, stati px"
set xlabel "Energia - E_F (eV)"
set ylabel "pDOS(E)"

Ef1 = -0.483
Ef2 = -1.9497
Ef3 = 5.0575

set arrow from 0, graph 0 to 0, graph 1 nohead lw 1 lc rgb "gray"

plot[-20:]  \
 "../dos_freestanding/pdos_p.dat" u ($1 - Ef1):4 w l lw 2 lc rgb "red" title "freestanding", \
 "../dos_without_Re/pdos_p.dat" u ($1 - Ef2):4 w l lw 2 lc rgb "blue" title "no substrate", \
 "../dos_with_Re/pdos_p.dat" u ($1 - Ef3):4 w l lw 2 lc rgb "green" title "with substrate"
