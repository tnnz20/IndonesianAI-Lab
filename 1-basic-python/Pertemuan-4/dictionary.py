#tipe data dictionary

thisdict = {
    'model':'Ford',
    'tipe ' :"mobil",
    'tahun':"1980"
}
#print semua elemen
print(thisdict)
print()

#print salah satu elemen pada dictionary
x = thisdict['model']
print(x)
print()
#menganti salah satu elemen
thisdict['tahun']= '1990'

#menambahkan elemen
thisdict['warna'] = "Merah"
print(thisdict)
print()

#perulangan untuk print semua elemen
for i in thisdict:
    print(i.upper(), ":",thisdict[i])