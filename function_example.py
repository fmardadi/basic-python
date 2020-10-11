nama_buah = []

def tambah_nama_buah(nama):
    nama_buah.append(nama)
    print_nama_buah()

def print_nama_buah():
    for buah in nama_buah:
        print(buah)
    print("-----")

tambah_nama_buah("jeruk")
tambah_nama_buah("apel")
tambah_nama_buah("melon")
tambah_nama_buah("pisang")

def total(x,y):
    total = x + y
    return total

def total_buah_sisa():
    return 20

jumlah = total(3,2)
print(jumlah)

total_buah = len(nama_buah) + total_buah_sisa()
print(total_buah)