import os

def leggi_dat(path):
    """
    Legge le configurazioni del borofene nei file .dat
    Input:
        path (stringa): percorso dei file
    Returns:
        f.readlines() (lista): contiene le stringhe con le coordinate cristallografiche di ciascun atomo di B
    """
    with open(path, 'r') as f:
        return f.readlines()


def genera_relax_in(B_coordinates):
    """
    Crea i file relax.in per ciascuna configurazione di borofene su substrato di Re(0001) con 4 layers
    Input:
        B_coordinates (lista): coordinate degli atomi di B
        nat (intero): numero totale di atomi (48 di Re + B variabile tra 27 e 35)
    Returns:
        testo da inserire in relax.in
    """
    nat = 48 + len(B_coordinates)
    return f"""&control
    calculation = 'relax',
    prefix = 'borophene',
    outdir = './outdir',
    pseudo_dir = '../../../pseudo'
    /

&system
    ibrav = 4,
    celldm(1) = 18.074, !2*sqrt(3)*2.761 = 9.564 ang = 18.074 bohr
    celldm(3) = 2.3304, !4.458*5/9.564 con vuoto = 4.458*3 = 13.374 A
    nat = {nat},
    ntyp = 2,
    ecutwfc = 60,
    occupations= 'smearing',
    smearing   = 'marzari-vanderbilt',
    degauss = 0.03
    /
&electrons
    /
&ions
    /
ATOMIC_SPECIES
 B  10.811  B.pbesol-n-rrkjus_psl.1.0.0.UPF
 Re 186.207 re_pbesol_v1.2.uspp.F.UPF
ATOMIC_POSITIONS crystal
Re 0.166667 0.000000 0.000000 0 0 0
Re 0.666667 0.000000 0.000000 0 0 0
Re 0.000000 0.166667 0.000000 0 0 0
Re 0.500000 0.166667 0.000000 0 0 0
Re 0.333333 0.333333 0.000000 0 0 0
Re 0.833333 0.333333 0.000000 0 0 0
Re 0.166667 0.500000 0.000000 0 0 0
Re 0.666667 0.500000 0.000000 0 0 0
Re 0.000000 0.666667 0.000000 0 0 0
Re 0.500000 0.666667 0.000000 0 0 0
Re 0.333333 0.833333 0.000000 0 0 0
Re 0.833333 0.833333 0.000000 0 0 0
Re 0.000000 0.000000 0.100000 0 0 0
Re 0.500000 0.000000 0.100000 0 0 0
Re 0.333333 0.166667 0.100000 0 0 0
Re 0.833333 0.166667 0.100000 0 0 0
Re 0.166667 0.333333 0.100000 0 0 0
Re 0.666667 0.333333 0.100000 0 0 0
Re 0.000000 0.500000 0.100000 0 0 0
Re 0.500000 0.500000 0.100000 0 0 0
Re 0.333333 0.666667 0.100000 0 0 0
Re 0.833333 0.666667 0.100000 0 0 0
Re 0.166667 0.833333 0.100000 0 0 0
Re 0.666667 0.833333 0.100000 0 0 0
Re 0.166667 0.000000 0.200000
Re 0.666667 0.000000 0.200000
Re 0.000000 0.166667 0.200000
Re 0.500000 0.166667 0.200000
Re 0.333333 0.333333 0.200000
Re 0.833333 0.333333 0.200000
Re 0.166667 0.500000 0.200000
Re 0.666667 0.500000 0.200000
Re 0.000000 0.666667 0.200000
Re 0.500000 0.666667 0.200000
Re 0.333333 0.833333 0.200000
Re 0.833333 0.833333 0.200000
Re 0.000000 0.000000 0.300000
Re 0.500000 0.000000 0.300000
Re 0.333333 0.166667 0.300000
Re 0.833333 0.166667 0.300000
Re 0.166667 0.333333 0.300000
Re 0.666667 0.333333 0.300000
Re 0.000000 0.500000 0.300000
Re 0.500000 0.500000 0.300000
Re 0.333333 0.666667 0.300000
Re 0.833333 0.666667 0.300000
Re 0.166667 0.833333 0.300000
Re 0.666667 0.833333 0.300000
{''.join(B_coordinates)}
K_POINTS automatic
4 4 1 0 0 0
"""

for n_buchi in range(1,10):
    dat_folder = os.path.join("allowed_config", f"{n_buchi}_vacancies")
    qe_folder = os.path.join("qe_jobs", f"{n_buchi}_vacancies")

    #Evita errori se mancano cartelle in allowed_config
    if not os.path.isdir(dat_folder):
        continue

    os.makedirs(qe_folder, exist_ok=True)


    for dat_file in os.listdir(dat_folder):
        if not dat_file.endswith(".dat"):
            continue

        name = dat_file.replace(".dat", "")
        config_dir = os.path.join(qe_folder, name)
        os.makedirs(config_dir, exist_ok=True)

        # Creo cartella outdir
        outdir_path = os.path.join(config_dir, "outdir")
        os.makedirs(outdir_path, exist_ok=True)

        # Leggo le coordinate e creo relax.in
        dat_path = os.path.join(dat_folder, dat_file)
        B_coordinate = leggi_dat(dat_path)
        relax_in = genera_relax_in(B_coordinate)

        relax_path = os.path.join(config_dir, f"{name}.relax.in")
        with open(relax_path, 'w') as f:
            f.write(relax_in)
