import subprocess
import os

for n_buchi in range(1, 10):
    qe_folder = os.path.join("qe_jobs", f"{n_buchi}_vacancies")

    for config_name in os.listdir(qe_folder):
        config_dir = os.path.join(qe_folder, config_name)

        # Cerco il file .relax.in nella cartella
        for input_file in os.listdir(config_dir):
            if input_file.endswith(".relax.in"):
               input_path = os.path.join(config_dir, input_file)
               output_path = input_path.replace(".relax.in", ".relax.out")
               name = input_file.replace(".relax.in", "")
                
               with open(output_path, "w") as out_path:
                   subprocess.run(
                       ["pw.x", "-inp", input_file],
                       stdout=out_path,
                       stderr=subprocess.STDOUT,
                       cwd=config_dir
                   )
