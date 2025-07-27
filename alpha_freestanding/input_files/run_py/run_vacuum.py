import os  

os.makedirs('../vacuum', exist_ok=True)

start = 1.5
end = 4.5
step = 0.5

for vacuum in  [round(start + i * step,2) for i in range(int((end - start) / step) + 1)]:

    with open(f'../vacuum/alpha_{vacuum}.in', 'w') as f:
        f.write(f"""
&control
    prefix        = 'borophene',
    calculation   = 'scf',
    pseudo_dir    = '../../pseudo',
    outdir        = '../../outdir'
 /
 &system
    ibrav         = 4,
    celldm(1)     = 9.5,
    celldm(3)     = {vacuum},
    nat           = 8,
    ntyp          = 1,
    ecutwfc       = 50,
    occupations= 'smearing',
    smearing   = 'marzari-vanderbilt',
    degauss    = 0.02
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
 6 6 1 0 0 0          
""")
    os.system(f"pw.x -inp ../vacuum/alpha_{vacuum}.in > ../vacuum/alpha_{vacuum}.out")
