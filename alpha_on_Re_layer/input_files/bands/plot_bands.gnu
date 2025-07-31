set terminal pngcairo size 1000, 700 enhanced font "Arial, 14"
set output "bands.png"

set title "Struttura a bande"
set xlabel "percorso nella BZ"
set ylabel "Energia - E_F (eV)"

set arrow from graph 0, first 0 to graph 1, first 0 nohead lw 2 lc rgb "red"

set xtics ("{/Symbol G}" 0.0000, "M" 0.5774, "K" 0.9107, "{/Symbol G}" 1.5773)

set for [x in "0.0000 0.5774 0.9107 1.5773"] arrow from x, graph 0 to x, graph 1 nohead dt 2 lc rgb "gray"

Ef = 5.1122

set key top right

plot[][-10:10] \
	"alphabands.dat.gnu" u 1:($2 -Ef) w l lw 2 lc rgb "blue" notitle, \
	NaN w l lw 2 lc rgb "red" title "E_F"
