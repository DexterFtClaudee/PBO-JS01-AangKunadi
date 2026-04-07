# Program Menghitung BMI
print("--- Program Hitung BMI ---")

# Input: berat (kg) dan tinggi (cm)
berat = float(input("Masukkan berat badan Anda (kg): "))
tinggi_cm = float(input("Masukkan tinggi badan Anda (cm): "))

# Konversi tinggi cm ke meter
tinggi_m = tinggi_cm / 100

# Rumus BMI: berat / (tinggi^2)
bmi = berat / (tinggi_m ** 2)

# Output nilai BMI
print(f"\nSkor BMI Anda: {bmi:.2f}")

# Cek kategori berdasarkan nilai BMI
if bmi < 18.5:
    kategori = "Underweight"
elif 18.5 <= bmi <= 24.9:
    kategori = "Normal"
elif 25 <= bmi <= 29.9:
    kategori = "Overweight"
else:
    kategori = "Obese (Obesitas)"

print(f"Kategori: {kategori}")