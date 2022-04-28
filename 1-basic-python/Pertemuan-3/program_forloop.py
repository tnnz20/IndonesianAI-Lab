#program input data dengan for

#untuk input jumlah data
count =int(input("Masukan jumlah data : "))

#list pelanggan
nama_pelanggan = []
umur_pelanggan = []
print()

#for untuk memasukan data
for i in range(count):
    print("Data ke- {}".format(i+1))
    nama = input("Masukan Nama : ")
    umur = int(input("Masukan Umur : "))
    print()

    nama_pelanggan.append(nama)
    umur_pelanggan.append(umur)

print()
#for untuk menampilkan data
for i in range(len(nama_pelanggan)):
    print("Data Pelanggan ke- {}".format(i+1))
    print("Nama : ", nama_pelanggan[i])
    print("Umur :", umur_pelanggan[i])
    print()