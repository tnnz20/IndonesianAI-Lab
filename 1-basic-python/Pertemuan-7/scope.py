# scope merupakan istilah variable dalam sebuah fungsi
# ada dua scope scope global dan local

def myfunc():
    x =300 # x merupakan scope local
    print(x)

myfunc()