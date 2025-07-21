import numpy as np
import matplotlib.pyplot as plt	
	
#plot stress
data_stress = np.loadtxt('stress_latticeparam.dat')
#x contiene i valori del lattice parameter
x_stress = data_stress[:,0]
#y contiene i valori dello stress lungo x
y_stress = data_stress[:,1]
#y contiene i valori dello stress lungo y
z_stress = data_stress[:,2]

plt.plot(x_stress, y_stress, color = 'g', marker = 'o', label="stress lungo x (Ry/bohr^3)")
plt.plot(x_stress, z_stress, color = 'b', marker = 'o', label="stress lungo y (Ry/bohr^3)")

plt.axhline(0, color='gray', linestyle = "-")


#legenda e assi
plt.xlabel("lattice parameter (a.u.)")
plt.ylabel("stress (Ry/bohr^3)")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig("stress_latticeparam", dpi=300)
plt.show()
