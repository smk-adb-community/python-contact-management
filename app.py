import contact

# Memuat semua kontak yang ada di file JSON
daftar_kontak = contact.load_kontak()

while True:
    print("***** Menu *****")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Hapus Kontak")
    print("4. Cari Kontak")
    print("5. Keluar Program")
    print("***** Menu *****")

    menu = input("Pilih menu : ")

    if menu == "5":
        contact.save_kontak(daftar_kontak)
        print("program selesai berjalan,Terimakasih.")
        break
    elif menu == "1":
        contact.display_kontak(daftar_kontak)
    elif menu == "2":
        kontak = contact.new_kontak()
        daftar_kontak.append(kontak)
        print("kontak berhasil ditambahkan!")
    elif menu == "3":
        contact.hapus_kontak(daftar_kontak)
    elif menu == "4":
        contact.cari_kontak(daftar_kontak)
    else:
        print("Menu tidak tersedia")