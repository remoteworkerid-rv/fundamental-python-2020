# KONTRUKSI DASAR PYTHON

# Sequential : Eksekusi Urutan
print("hello world!")
print("Rydha Valenda")
print("4 Sep 2020")
print("-" * 7)

# Percabangan : Eksekusi Terpilih
jalur_cepat = False

if jalur_cepat:
    print("Belok Kanan")
else:
    print("Lurus Saja\n")

# Perulangan : Loop
jumlah_anak = 4

for index_anak in range (1, jumlah_anak+1): #jumlah perulangan 5-1 = 4
    print(f'anak ke -{index_anak}')
