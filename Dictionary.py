kontak = {
    "Andi": {"telepon": "081234567890", "email": "andi@mail.com"},
    "Budi": {"telepon": "081987654321", "email": "budi@mail.com"}
}
kontak["Cici"] = {"telepon": "081223344556", "email": "cici@mail.com"}
for nama in kontak.keys():
    print(nama)  # Cetak semua nama kontak
kontak["Andi"]["telepon"] = "081112223344"
