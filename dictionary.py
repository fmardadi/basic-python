pelanggan = {
    "nama": "farhan",
    "umur": 21
}

pelanggan_2 = {
    "nama": "andi",
    "umur": 18
}

print("Nama: {}".format(pelanggan["nama"]))
print("Umur: {}".format(pelanggan["umur"]))

# change value of dictionary
pelanggan["umur"] = 22

print("Nama: {}".format(pelanggan["nama"]))
print("Umur: {}".format(pelanggan["umur"]))

# loop through dictionary
for x in pelanggan:
    print(x)
    print(pelanggan[x])   
    print(pelanggan_2[x])   

# list of dictionary
daftar_pelanggan = []
daftar_pelanggan.append(pelanggan)
daftar_pelanggan.append(pelanggan_2)

for pelanggan in daftar_pelanggan:
    print("Nama: {}".format(pelanggan["nama"]))
    print("Umur: {}".format(pelanggan["umur"]))