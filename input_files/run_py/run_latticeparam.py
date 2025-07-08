import os  

os.makedirs('../latticeparam', exist_ok=True)

start = 9.0 #1.59A
end = 10.0 #1.76A
step = 0.2

for latticeparam in  [round(start + i * step,2) for i in range(int((end - start) / step) + 1)]:

    with open(f'../latticeparam/alpha_{latticeparam}.in', 'w') as f:
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
    ecutwfc       = 70,
    occupations= 'smearing',
    smearing   = 'marzari-vanderbilt',
    degauss = 0.035
    input_dft = 'pbesol'
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
    os.system(f"pw.x -inp ../latticeparam/alpha_{latticeparam}.in > ../latticeparam/alpha_{latticeparam}.out")
