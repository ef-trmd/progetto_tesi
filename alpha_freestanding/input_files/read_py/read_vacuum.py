from ase.io import read 
import os

if os.path.exists('../vacuum/etot_vacuum.dat'):
    os.remove('../vacuum/etot_vacuum.dat')

start = 1.5
end = 4.5
step = 0.5

for vacuum in  [round(start + i * step,2) for i in range(int((end - start) / step) + 1)]:

    structure = read(f'../vacuum/alpha_{vacuum}.out')
    
    with open(f'../vacuum/etot_vacuum.dat', 'a') as f:
        f.write(f'{vacuum} {structure.get_potential_energy()}\n')
