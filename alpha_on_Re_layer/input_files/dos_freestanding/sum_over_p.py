file_names = [
	"alphapdos.dat.pdos_atm#1(B)_wfc#2(p)",
	"alphapdos.dat.pdos_atm#2(B)_wfc#2(p)",
	"alphapdos.dat.pdos_atm#3(B)_wfc#2(p)",
	"alphapdos.dat.pdos_atm#4(B)_wfc#2(p)",
	"alphapdos.dat.pdos_atm#5(B)_wfc#2(p)",
	"alphapdos.dat.pdos_atm#6(B)_wfc#2(p)",
	"alphapdos.dat.pdos_atm#7(B)_wfc#2(p)",
	"alphapdos.dat.pdos_atm#8(B)_wfc#2(p)"
]

data = []

for file_name in file_names:
	with open(file_name, 'r') as f:
		lines = f.readlines()
		if file_name == file_names[0]:
			header = lines[0]
		body = lines[1:]
	data.append([list(map(float, row.split())) for row in body if row.strip()])
	
n_rows = len(data[0])
n_col = len(data[0][0])

sum = []
for i in range(n_rows):
	energy = data[0][i][0]
	row_sum = [0.0] * (n_col-1)
	for j in range(len(data)):
		for k in range(1,n_col):
			row_sum[k-1] += data[j][i][k]
	row = [energy] + row_sum
	sum.append(row)

with open("pdos_p.dat", "w") as f_out:
	f_out.write(header)
	for row in sum:
		f_out.write (" ".join(f"{val:.6f}" for val in row) + "\n")
