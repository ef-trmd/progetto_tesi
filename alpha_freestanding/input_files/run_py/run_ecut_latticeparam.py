import os  

os.makedirs('../latticeparam', exist_ok=True)

start_latticeparam = 9.52
end_latticeparam = 9.64
step_latticeparam = 0.02

start_ecut = 50
end_ecut = 80
step_ecut = 10

for ecut in  [round(start_ecut + i * step_ecut,2) for i in range(int((end_ecut - start_ecut) / step_ecut) + 1)]:
    for latticeparam in  [round(start_latticeparam + i * step_latticeparam,2) for i in range(int((end_latticeparam - start_latticeparam) /  step_latticeparam) + 1)]:
        with open(f'../latticeparam/alpha_{ecut}_{latticeparam}.in', 'w') as f:
            f.write(f"""
&control
    prefix        = 'borophene',
    calculation   = 'scf',
    pseudo_dir    = '../../pseudo',
    outdir        = '../../outdir'
 /
 &system
    ibrav         = 4,
    celldm(1)     = {latticeparam},
    celldm(3)     = 2.0,
    nat           = 8,
    ntyp          = 1,
    ecutwfc       = {ecut},
    occupations= 'smearing',
    smearing   = 'marzari-vanderbilt',
    degauss = 0.035
 /
 &electrons
 /
ATOMIC_SPECIES
 B  10.811  B.pbesol-n-rrkjus_psl.1.0.0.UPF
ATOMIC_POSITIONS crystal
B 0.333333 0.000000 0.000000
B 0.666667 0.000000 0.000000
B 0.000000 0.333333 0.000000
B 0.333333 0.333333 0.000000
B 0.666667 0.333333 0.000000
B 0.000000 0.666667 0.000000
B 0.333333 0.666667 0.000000
B 0.666667 0.666667 0.000000
K_POINTS automatic
 9 9 1 0 0 0          
""")
        os.system(f"pw.x -inp ../latticeparam/alpha_{ecut}_{latticeparam}.in > ../latticeparam/alpha_{ecut}_{latticeparam}.out")
