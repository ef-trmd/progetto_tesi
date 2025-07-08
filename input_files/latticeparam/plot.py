import numpy as np
import matplotlib.pyplot as plt

dat_files = {

	"50 Ry": "etot_ecut50_latticeparam.dat",
	"60 Ry": "etot_ecut60_latticeparam.dat",
	"70 Ry": "etot_ecut70_latticeparam.dat",
	"80 Ry": "etot_ecut80_latticeparam.dat"
	
	}
	
colors = ['r', 'g', 'b', 'y']

plt.figure(figsize=(8,6))

for i, (label, filename) in enumerate(dat_files.items()):
	data = np.loadtxt(filename)
	#x contiene i valori del lattice parameter
	x = data[:,0]
	#y contiene i valori dell'energia totale
	y = data[:,1]
	
	#fit parabolico
	coeffs = np.polyfit(x,y,2)
	poly = np.poly1d(coeffs)
	
	x_fit = np.linspace(9.5, 9.7, 100)
	y_fit = poly(x_fit)
	min_index = np.argmin(y_fit)
	
	plt.plot(x_fit, y_fit, label=f"Cutoff {label}", color = colors[i], linestyle = "-")
	plt.scatter(x, y, color = colors[i], marker = 'o')
	plt.scatter(x_fit[min_index], y_fit[min_index], marker='x', color = colors[i], label=f"Minimo {label}")
	
#legenda e assi
plt.xlabel("lattice parameter (a.u.)")
plt.ylabel("total energy (Ry)")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig("convergence_latticeparam_ecut", dpi=300)
plt.show()
