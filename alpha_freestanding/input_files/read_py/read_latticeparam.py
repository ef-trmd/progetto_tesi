from ase.io import read 
import os

if os.path.exists('../latticeparam/etot_latticeparam.dat'):
    os.remove('../latticeparam/etot_latticeparam.dat')

start = 9.0
end = 10.0
step = 0.2

for latticeparam in  [round(start + i * step,2) for i in range(int((end - start) / step) + 1)]:

    structure = read(f'../latticeparam/alpha_{latticeparam}.out')
    
    with open(f'../latticeparam/etot_latticeparam.dat', 'a') as f:
        f.write(f'{latticeparam} {structure.get_potential_energy()}\n')
