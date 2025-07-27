from ase.io import read 
import os

if os.path.exists('../ecut/etot_ecut.dat'):
    os.remove('../ecut/etot_ecut.dat')

start = 40
end = 80
step = 10

for ecut in  [round(start + i * step,2) for i in range(int((end - start) / step) + 1)]:

    structure = read(f'../ecut/alpha_{ecut}.out')
    
    with open(f'../ecut/etot_ecut.dat', 'a') as f:
        f.write(f'{ecut} {structure.get_potential_energy()}\n')
