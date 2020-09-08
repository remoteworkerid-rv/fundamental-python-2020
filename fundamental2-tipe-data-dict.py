"""Tipe data dictionary hanya sekedar menghubungkan antara KEY dan Value
KVP = KEY VALUE PAIR
Dictionary = Kamus
"""

kamus_ind_eng = {'anak': 'son', 'paman': 'uncle', 'ayah': 'Father', 'ibu': 'Mother'}

print(kamus_ind_eng)
print(kamus_ind_eng['anak'])
print(kamus_ind_eng['paman'])
print(kamus_ind_eng['ayah'])
print(kamus_ind_eng['ibu'])

print('\nData ini dikirim oleh server gojek untuk melihat keberadaan gojek terdekat disekitar aplikasi')
data_dari_server_gojek = {
    'tanggal' : '2020-09-09',
    'driver_list': [{'nama': 'rydha', 'jarak': 10},
                    {'nama': 'oji', 'jarak': 20},
                    {'nama': 'maop', 'jarak': 50},
                    {'nama': 'lemben', 'jarak': 1000}]
}
print(data_dari_server_gojek)
print(f"Driver sekitar aplikasi adalah {data_dari_server_gojek['driver_list']}")
print(f"Driver ke-1 {data_dari_server_gojek['driver_list'][0]}")
print(f"Driver ke-4 {data_dari_server_gojek['driver_list'][3]}")
print(f"Driver terdekat berjarak {data_dari_server_gojek['driver_list'][0]['jarak']}")

