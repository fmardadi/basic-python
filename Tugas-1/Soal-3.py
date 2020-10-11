nilai_minimum = float(input("Nilai minimun: "))

nilai_teori = float(input("Nilai teori: "))
nilai_praktek = float(input("Nilai prakrek: "))

if nilai_teori >= nilai_minimum and nilai_praktek >= nilai_minimum:
    print("Lulus")
elif nilai_teori >= nilai_minimum and nilai_praktek < nilai_minimum:
    print("Anda mengulang ujian praktek")
elif nilai_teori < nilai_minimum and nilai_praktek >= nilai_minimum:
    print("Anda mengulang ujian teori")
else:
    print("Anda mengulang ujian teori dan praktek")