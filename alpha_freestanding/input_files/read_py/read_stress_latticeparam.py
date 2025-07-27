from ase.io import read 
import os

if os.path.exists('../stress/stress_latticeparam.dat'):
    os.remove('../stress/stress_latticeparam.dat')

start = 9.52
end = 9.64
step = 0.02

for latticeparam in  [round(start + i * step,2) for i in range(int((end - start) / step) + 1)]:

    structure = read(f'../stress/alpha_{latticeparam}.out')
    
    with open(f'../stress/stress_latticeparam.dat', 'a') as f:
        f.write(f'{latticeparam} {structure.get_stress()[0]} {structure.get_stress()[1]}\n')
