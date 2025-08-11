import subprocess

for n_buchi in range(1, 10):
    qe_folder = os.path.join("qe_jobs", f"{n_buchi}_vacancies")

    for config_name in os.listdir(qe_folder):
        config_dir = os.path.join(qe_folder, config_name)

        # Cerco il file .relax.in nella cartella
        for file in os.listdir(config_dir):
            if file.endswith(".relax.in"):
                input_path = os.path.join(config_dir, file)
                output_path = input_path.replace(".relax.in", ".relax.out")
                
                with open(output_path, "w") as out_file:
                    subprocess.run(
                        ["pw.x", "-inp", input_path],
                        stdout=out_file,
                        stderr=subprocess.STDOUT,
                        cwd=config_dir
                    )