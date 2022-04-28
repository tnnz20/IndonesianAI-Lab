a = 220
b = 33
c = 55

# operator 
# > , < , != , >= , <= , and , or , not 
if b > a:
    print("b lebih besar dari a")
elif b == a:
    print("b sama dengan a")
else:
    print("b lebih kecil dari a")

print()

if (b < a) & (c > a):
    print("Kondisi benar")
else:
    print("kondisi salah")