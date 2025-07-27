from ase.io import read 
import os

if os.path.exists('../stress/etot_latticeparam.dat'):
    os.remove('../stress/etot_latticeparam.dat')

start = 9.52
end = 9.64
step = 0.02

for latticeparam in  [round(start + i * step,2) for i in range(int((end - start) / step) + 1)]:

    structure = read(f'../stress/alpha_{latticeparam}.out')
    
    with open(f'../stress/etot_latticeparam.dat', 'a') as f:
        f.write(f'{latticeparam} {structure.get_potential_energy()}\n')
