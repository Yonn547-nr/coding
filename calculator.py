def tambah(x, y):
    return x + y

def kurang(x, y):
    return x - y

def kali(x, y):
    return x * y

def bagi(x, y):
    if y == 0:
        return "Error: Pembagian dengan nol tidak diperbolehkan."
    return x / y

def kalkulator():
    while True:
        print("\nPilih operasi:")
        print("1. Penjumlahan")
        print("2. Pengurangan")
        print("3. Perkalian")
        print("4. Pembagian")
        print("5. Keluar")

        pilihan = input("Masukkan pilihan (1/2/3/4/5): ")

        if pilihan == '5':
            print("Terima kasih telah menggunakan kalkulator. Sampai jumpa!")
            break  # Keluar dari loop

        if pilihan in ['1', '2', '3', '4']:
            angka1 = float(input("Masukkan angka pertama: "))
            angka2 = float(input("Masukkan angka kedua: "))

            if pilihan == '1':
                print(f"Hasil: {angka1} + {angka2} = {tambah(angka1, angka2)}")
            elif pilihan == '2':
                print(f"Hasil: {angka1} - {angka2} = {kurang(angka1, angka2)}")
            elif pilihan == '3':
                print(f"Hasil: {angka1} * {angka2} = {kali(angka1, angka2)}")
            elif pilihan == '4':
                print(f"Hasil: {angka1} / {angka2} = {bagi(angka1, angka2)}")
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    kalkulator()