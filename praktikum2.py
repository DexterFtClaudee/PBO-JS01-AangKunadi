# Program Cek Bilangan
print("--- Program Cek Genap, Ganjil, atau Prima ---")

angka = int(input("Masukkan sebuah bilangan bulat: "))

# 1. Cek Genap atau Ganjil menggunakan Modulus (%)
if angka % 2 == 0:
    print(f"{angka} adalah bilangan Genap.")
else:
    print(f"{angka} adalah bilangan Ganjil.")

# 2. Cek Bilangan Prima
# Bilangan prima harus lebih besar dari 1
is_prima = True
if angka > 1:
    for i in range(2, int(angka**0.5) + 1):
        if (angka % i) == 0:
            is_prima = False
            break
else:
    is_prima = False

if is_prima:
    print(f"{angka} juga merupakan bilangan Prima.")
else:
    print(f"{angka} bukan bilangan Prima.")