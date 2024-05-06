# '''
# Input Harga: 370000
# Input Diskon: 15
# Output: harga yang harus dibayar adalah Rp. 314.500
# '''

# Rumus
# Harga Diskon = (diskon/100) x Harga awal
# Harga akhir = harga awal - harga diskon

# Input
print("\n'Harga Bayar Setelah Diskon'\n")
harga_awal = input("Masukkan Harga Barang : ")
diskon = input("Masukkan Diskon : ")

# Kode Disini
ha = int(harga_awal)
d = int(diskon)

total_diskon = ((d / 100) * ha)
harga_akhir = (ha - total_diskon)

print("Harga Yang Harus Dibayar : ", harga_akhir)
