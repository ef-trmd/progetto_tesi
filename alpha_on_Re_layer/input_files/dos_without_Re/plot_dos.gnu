set terminal pngcairo size 1000, 700 enhanced font "Arial, 14"
set output "just_alpha_dos.png"

set title "DOS"
set xlabel "Energia - E_F (eV)"
set ylabel "DOS(E)"

Ef = -1.9497

set arrow from 0, graph 0 to 0, graph 1 nohead lw 1 lc rgb "gray"

plot[][] "justalphados.dat" u ($1 - Ef):2 w l lw 2 lc rgb "red" notitle
