set terminal pngcairo size 1000, 700 enhanced font "Arial, 14"
set output "pdos123468.png"

set title "pDOS sugli orbitali s e p degli atomi con 5 primi vicini"
set xlabel "Energia - E_F (eV)"
set ylabel "pDOS(E)"

Ef = -0.483

set arrow from 0, graph 0 to 0, graph 1 nohead lw 1 lc rgb "gray"

plot \
 "alphapdos.dat.pdos_atm#1(B)_wfc#1(s)" u ($1 - Ef):2 w l lw 2 lc rgb "red" title "s", \
 "alphapdos.dat.pdos_atm#1(B)_wfc#2(p)" u ($1 - Ef):3 w l lw 2 lc rgb "blue" title "pz", \
 "alphapdos.dat.pdos_atm#1(B)_wfc#2(p)" u ($1 - Ef):4 w l lw 2 lc rgb "green" title "px", \
 "alphapdos.dat.pdos_atm#1(B)_wfc#2(p)" u ($1 - Ef):5 w l lw 2 lc rgb "yellow" title "py"
