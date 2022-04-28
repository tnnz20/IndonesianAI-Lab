"""\
file handling digunakan untuk
-menambahkan
-menghapus
-mengedit
suatu file txt menggunakan python """

import os

# "r" untuk read suatu file
# "rb" untuk file eror bila menggunakan windows
# read() membaca keseluruhan file
r = open('Pertemuan-5/filetxt.txt' , 'r').read()
print(r)
# readline() membaca pada baris pertama 
print("\nini menggunakan readline".upper())
r2 = open('Pertemuan-5/filetxt.txt' , 'r').readline()
print(r2)
# readlines() membaca file dengan format list
# bisa menggunakan index untuk pemangilan setiap baris
# r[1] , r[0]
print("ini menggunakan readlines".upper())
r = open('Pertemuan-5/filetxt.txt' , 'r').readlines()
print(r)

# "a" untuk menambahkan isi text atau append
f = open('Pertemuan-5/filetxt.txt' , 'a')
f.write(" Tulisan baru")
f.close

# "w" untuk menulis ulang file
f = open('Pertemuan-5/filetxt.txt' , 'w')
f.write(" Tulisan baru")
f.close

# untuk menghapus file
os.remove('Pertemuan-5/filetxt.txt')
