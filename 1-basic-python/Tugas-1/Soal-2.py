#Soal no 2 Luas Lingkaran

phi = 22/7
r = int(input("Masukan Jari-jari : "))

luas = float(phi * (r**2))

print("Luas lingkaran dengan jari-jari", r, "cm adalah", "{:.2f}".format(luas), "cm\u00b2")
print(type(luas))