from decimal import Decimal, getcontext

# Imposta la precisione numerica
getcontext().prec = 10

input_file = "big_hex_1.relax.in"
output_file = "big_hex_3.relax.in"

updated_lines = []

with open(input_file, 'r') as file:
    for line in file:
        if line.strip().startswith("Re"):
            parts = line.strip().split()
            x = Decimal(parts[1])

            if abs(x - Decimal('0.833333')) < Decimal('0.000001'):
                new_x = Decimal('0.000000')
            else:
                new_x = (x + Decimal('1')/Decimal('3')) % Decimal('1')

            # Ricostruisce la linea con x aggiornato, mantenendo le altre coordinate
            new_line = f"{parts[0]} {new_x:.6f} {parts[2]} {parts[3]}"
            if len(parts) > 4:
                # Aggiungi eventuali flag (es. 0 0 0)
                new_line += ' ' + ' '.join(parts[4:])
            updated_lines.append(new_line + "\n")
        else:
            updated_lines.append(line)

# Scrive il nuovo file
with open(output_file, 'w') as file:
    file.writelines(updated_lines)

print("Coordinate modificate e salvate in:", output_file)
