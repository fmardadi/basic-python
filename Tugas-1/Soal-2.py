
r = float(input("Masukkan jari-jari lingkaran: "))
pi = 22/7

def hitung_luas_lingkaran(r):
    luas = pi * r * r
    return luas

luas = hitung_luas_lingkaran(r)

print("Luas lingkaran: {:.2f}".format(luas))