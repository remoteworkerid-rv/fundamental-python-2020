# TIPE DATA SKALAR ==> TIPE DATA SEDERHANA
anak1 = 'rydha'
anak2 = 'oji'
anak3 = 'maop'
anak4 = 'lemben'

print(anak1)
print(anak2)
print(anak3)
print(anak4)

print('\nTIPE DATA LIST/DAFTAR/ARRAY')
anak = ['rydha', 'oji', 'maop', 'lemben']
print(anak)
anak.append('lentrak')
print(anak)

print('\nmenyapa anak ke 2')
print(f'hai {anak[1]}')

print('\nmenyapa semua anak')
for a in anak:
    print(f'hai {a}')

print('\nmenyapa semua anak : cara ribet')
for a in range (0, len(anak)):
    print(f'{a+1}. hai {anak[a]}')