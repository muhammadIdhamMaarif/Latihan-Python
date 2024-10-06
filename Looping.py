ganjil = [i for i in range(1, 101) if i % 2 != 0]
print(f"Jumlah bilangan ganjil dari 1 sampai 100: {len(ganjil)}")

tinggi = int(input("Masukkan tinggi segitiga: "))
for i in range(1, tinggi + 1):
    print('*' * i)

nilai_list = [10, 23, 45, 67, 89, 2, 5]
print(f"Nilai terbesar: {max(nilai_list)}, Nilai terkecil: {min(nilai_list)}")

