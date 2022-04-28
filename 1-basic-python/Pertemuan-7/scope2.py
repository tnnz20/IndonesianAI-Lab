# scope global
# scope global di taruh di luar fungsi yang mana bisa diakses
# oleh semua variabel

x = 300 #scope global

def myfunc():
    print(x)
    y = 300 + x
    print(y)

myfunc()