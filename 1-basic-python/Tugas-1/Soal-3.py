#Soal nomor 3 Ujian Praktek

Teori = float(input("Masukan Nilai Teori : "))
Praktek = float(input("Masukan Nilai Praktek : "))

if Teori >= 70 and Praktek >=70:
    print("Selamat, anda lulus!")
elif Teori >= 70 and Praktek < 70:
    print("Anda harus mengulang ujian Praktek.")
elif Teori < 70 and Praktek >= 70:
    print("Anda harus mengulang ujian Teori.")
else:
    print("Anda harus mengulang ujian Teori dan Praktek")