#peulangan dengan continue
#continue akan memprint melewati sesuai kondisi

for i in range(5):
    if i == 3:
        continue
    print(i)

print()

#kondisi apabila genap print ganjil
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

print()
#kondisi apabila genap print ganjil
for i in range(10):
    if i % 2 == 1:
        continue
    print(i)

print()
#kondisi apabila ada jeruk maka akan terlewati
buah =['apel','jeruk','pisang']
for i in buah:
    if i == 'jeruk':
        continue
    print(i)
