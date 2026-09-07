# Tugas 3 - Python Basics

# 1. Deklarasi Variabel dan Tipe Data

nama = "Navita"                                      # String
umur = 20                                            # Integer
tinggi = 150.0                                         # Float
mahasiswa = True                                     # Boolean
hobi = ["Membaca", "Menyanyi", "Bermain Musik", "Desain", "Berenang"]  # List

print("=== 1. Deklarasi Variabel dan Tipe Data ===")
print("Nama:", nama)
print("Umur:", umur)
print("Tinggi:", tinggi)
print("Mahasiswa:", mahasiswa)
print("Hobi:", hobi)


# 2. Manipulasi String

print("\n=== 2. Manipulasi String ===")

nama_depan = "Navita"
nama_belakang = "Damayanti"

nama_lengkap = nama_depan + " " + nama_belakang

print("Gabungan nama:", nama_lengkap)
print("Panjang nama:", len(nama_lengkap))
print("Huruf besar:", nama_lengkap.upper())
print("Huruf kecil:", nama_lengkap.lower())


# 3. Operasi Matematika Sederhana

print("\n=== 3. Operasi Matematika ===")

angka1 = 20
angka2 = 6

print("Penjumlahan:", angka1 + angka2)
print("Pengurangan:", angka1 - angka2)
print("Perkalian:", angka1 * angka2)
print("Pembagian:", angka1 / angka2)
print("Pembagian bulat:", angka1 // angka2)
print("Sisa pembagian:", angka1 % angka2)


# 4. List dan Akses Elemen

print("\n=== 4. List dan Akses Elemen ===")

buah = ["Melon", "Pepaya", "Mangga", "Apel", "Semangka"]

print("List awal:", buah)
print("Elemen pertama:", buah[0])
print("Elemen ketiga:", buah[2])

buah.append("Anggur")
print("Setelah menambahkan item:", buah)

buah.remove("Apel")
print("Setelah menghapus item:", buah)


# 5. Input dari User

print("\n=== 5. Input dari User ===")

nama_user = input("Masukkan nama Anda: ")
umur_user = input("Masukkan umur Anda: ")

print("Halo, nama saya", nama_user, "dan umur saya", umur_user, "tahun.", "hobi saya adalah", hobi[0], "dan", hobi[1], ".")
