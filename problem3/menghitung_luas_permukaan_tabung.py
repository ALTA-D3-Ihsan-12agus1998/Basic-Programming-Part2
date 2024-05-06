# input

# T = 20.0
# r = 4.0

print("\n'Menghitung Luas Permukaan Tabung'\n")
input_t = input("Masukkan tinggi : ")
input_r = input("Masukkan radius : ")


# kode disini
t = float(input_t)
r = float(input_r)

if r % 7 == 0 :
    phi = 22/7
else:
    phi = 3.14

Lpt = (2 * phi * r * (r + t))

print("Luas Permukaan Tabung = ", round(Lpt,2))
