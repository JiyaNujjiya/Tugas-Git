data_panen = {
    'lokasi1': {
        'nama_lokasi' : 'Kebun A',
        'hasil_panen' : {
            'padi': 1200,
            'jagung': 800,
            'kedelai': 500
        }
    },
    'lokasi2': {
        'nama_lokasi':'Kebun B',
        'hasil_panen':{
            'padi':1500,
            'jagung':900,
            'kedelai': 450
        }
    },
    'lokasi3': {
        'nama_lokasi':'Kebun C',
        'hasil_panen':{
            'padi':1100,
            'jagung':750,
            'kedelai': 600
        }
    },
    'lokasi4': {
        'nama_lokasi':'Kebun D',
        'hasil_panen':{
            'padi':1300,
            'jagung':850,
            'kedelai': 550
        }
    },
    'lokasi5': {
        'nama_lokasi':'Kebun E',
        'hasil_panen':{
            'padi':1400,
            'jagung':950,
            'kedelai': 480
        }
    }   
}

# 1. Tampilkan seluruh data dari data_panen
print("Seluruh Data Panen:")
for lokasi, info in data_panen.items():
    print(f"{lokasi}: {info}")

# 2. Tampilkan jumlah hasil panen jagung dari lokasi2
jagung_lokasi2 = data_panen['lokasi2']['hasil_panen']['jagung']
print(f"\nJumlah hasil panen jagung dari lokasi2: {jagung_lokasi2}")

# 3. Tampilkan nama lokasi dari lokasi3
nama_lokasi3 = data_panen['lokasi3']['nama_lokasi']
print(f"\nNama lokasi dari lokasi3: {nama_lokasi3}")

# 4. Masukkan jumlah hasil panen padi dan kedelai setiap lokasi ke dalam variabel yang berbeda
padi_panen = {}
kedelai_panen = {}
for lokasi, info in data_panen.items():
    padi_panen[lokasi] = info['hasil_panen']['padi']
    kedelai_panen[lokasi] = info['hasil_panen']['kedelai']

print("\nJumlah hasil panen padi setiap lokasi:")
print(padi_panen)
print("\nJumlah hasil panen kedelai setiap lokasi:")
print(kedelai_panen)

# 5. Buat variabel terpisah untuk menyimpan jumlah hasil panen padi dan kedelai dari setiap lokasi
jumlah_padi = sum(padi_panen.values())
jumlah_kedelai = sum(kedelai_panen.values())
print(f"\nTotal hasil panen padi: {jumlah_padi}")
print(f"Total hasil panen kedelai: {jumlah_kedelai}")

# 6. Buat percabangan untuk menentukan lokasi yang memerlukan perhatian khusus
print("\nStatus lokasi berdasarkan hasil panen:")
for lokasi, info in data_panen.items():
    padi = info['hasil_panen']['padi']
    jagung = info['hasil_panen']['jagung']
    if padi > 1300 or jagung > 800:
        print(f"{info['nama_lokasi']} memerlukan perhatian khusus.")
    else:
        print(f"{info['nama_lokasi']} dalam kondisi baik.")