from ase.io import read 
import os

if os.path.exists('../degauss/etot_degauss.dat'):
    os.remove('../degauss/etot_degauss.dat')

start = 0.01
end = 0.05
step = 0.01

for degauss in  [round(start + i * step,2) for i in range(int((end - start) / step) + 1)]:

    structure = read(f'../degauss/alpha_{degauss}.out')
    
    with open(f'../degauss/etot_degauss.dat', 'a') as f:
        f.write(f'{degauss} {structure.get_potential_energy()}\n')
