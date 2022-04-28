#perulangan dengan break
#break akan menghentikan perulangan sesuai kondisi

for i in range(5):
    if i == 3:
        break
    print(i)
print()
#list
buah =['apel','jeruk','pisang']
for i in buah:
    print(i.upper())
    if i == 'pisang':
        break
    print("====")
print("\nPerulangan List selesai")