set terminal pngcairo size 1000, 700 enhanced font "Arial, 14"
set output "just_alpha_pdos12.png"

set title "pDOS"
set xlabel "Energia - E_F (eV)"
set ylabel "pDOS(E)"

Ef = -1.9497

set arrow from 0, graph 0 to 0, graph 1 nohead lw 1 lc rgb "gray"

plot[][] \
 'justalphapdos.dat.pdos_atm#6(B)_wfc#1(s)' u ($1 - Ef):2 w l lw 2 lc rgb "red" title "s", \
 'justalphapdos.dat.pdos_atm#6(B)_wfc#2(p)' u ($1 - Ef):3 w l lw 2 lc rgb "blue" title "pz", \
 'justalphapdos.dat.pdos_atm#6(B)_wfc#2(p)' u ($1 - Ef):4 w l lw 2 lc rgb "green" title "px", \
 'justalphapdos.dat.pdos_atm#6(B)_wfc#2(p)' u ($1 - Ef):5 w l lw 2 lc rgb "yellow" title "py"
