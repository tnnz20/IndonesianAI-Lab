#python menu
#list untuk data 
nama =[]
notelp = []

#perulangan while
print("Selamat Datang!\n")
while True:
    print(
        "------Menu------\n"
        "1. Daftar Kontak\n"
        "2. Tambah Kontak\n"
        "3. Keluar\n"
    )

    pilih= input("Pilih menu: ")
    print()

    if pilih == "1":
        print("Daftar Kontak")
        for i in range(len(nama)):
            print("Nama: {}".format(nama[i]))
            print("No Telpon: {}\n".format(notelp[i]))
           
    elif pilih == "2":
        tambah_nama = input("Nama: ")
        tambah_notelp = input("No Telpon: ")

        nama.append(tambah_nama)
        notelp.append(tambah_notelp)
        
        print("Kontak berhasil ditambah\n")    
    elif pilih == "3":
        print("Program Selesai, Sampai jumpa!")
        break
    else:
        print("Menu Tidak ada\n")