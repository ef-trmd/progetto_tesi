from ase.io import read 
import os

start_latticeparam = 9.52
end_latticeparam = 9.64
step_latticeparam = 0.02

start_k = 7
end_k = 10
step_k = 1

for k in  [round(start_k + i * step_k,2) for i in range(int((end_k - start_k) / step_k) + 1)]:
     if os.path.exists(f'../latticeparam/etot_k{k}_latticeparam.dat'):
        os.remove(f'../latticeparam/etot_k{k}_latticeparam.dat')
     for latticeparam in  [round(start_latticeparam + i * step_latticeparam,2) for i in range(int((end_latticeparam - start_latticeparam) /  step_latticeparam) + 1)]:
         
            structure = read(f'../latticeparam/alpha_{k}_{latticeparam}.out')
    
            with open(f'../latticeparam/etot_k{k}_latticeparam.dat', 'a') as f:
                f.write(f'{latticeparam} {structure.get_potential_energy()}\n')
