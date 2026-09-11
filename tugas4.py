# Tugas 4 - Python Data Structures


# 1. List - Akses & Manipulasi

print("=== 1. LIST - AKSES & MANIPULASI ===")

data = ["Python", 20, "AI", 3.14, "Coding", 100]

print("List awal:", data)
print("Elemen pertama:", data[0])
print("Elemen terakhir:", data[-1])
print("Slicing [1:6:2]:", data[1:6:2])

print("\n--- append() ---")
print("Sebelum:", data)
data.append("Programming")
print("Sesudah:", data)

print("\n--- insert() ---")
print("Sebelum:", data)
data.insert(2, "Data")
print("Sesudah:", data)

print("\n--- extend() ---")
print("Sebelum:", data)
data.extend(["Structure", 50])
print("Sesudah:", data)

print("\n--- pop() ---")
print("Sebelum:", data)
data.pop()
print("Sesudah:", data)

print("\n--- remove() ---")
print("Sebelum:", data)
data.remove("AI")
print("Sesudah:", data)


# 2. Tuple - Immutability & Unpacking

print("\n=== 2. TUPLE - IMMUTABILITY & UNPACKING ===")

data_tuple = ("Python", "AI", "Data", "Coding", "Programming")

print("Tuple:", data_tuple)
print("Panjang tuple:", len(data_tuple))
print("Elemen indeks ke-2:", data_tuple[2])

bahasa, bidang, *rest = data_tuple

print("\nHasil unpacking:")
print("Variabel bahasa:", bahasa)
print("Variabel bidang:", bidang)
print("Sisa elemen:", rest)

print("Tuple bersifat immutable, sehingga elemennya tidak dapat diubah.")


# 3. Set - Keunikan & Operasi Himpunan

print("\n=== 3. SET - KEUNIKAN & OPERASI HIMPUNAN ===")

set_a = {"Python", "AI", "Data", "Coding", "Python"}
set_b = {"AI", "Data", "Web", "Programming"}

print("Set A:", set_a)
print("Set B:", set_b)

print("\nUnion (|):", set_a | set_b)
print("Intersection (&):", set_a & set_b)
print("Difference (-):", set_a - set_b)
print("Symmetric Difference (^):", set_a ^ set_b)

print("\nDuplikat 'Python' otomatis hilang dari Set A.")
print("Jumlah elemen Set A:", len(set_a))


# 4. Dictionary - Key/Value Dasar

print("\n=== 4. DICTIONARY - KEY/VALUE DASAR ===")

mahasiswa = {
    "nama": "Navita",
    "nim": "12345678",
    "angkatan": 2024,
    "kota": "Batam"
}

print("Data mahasiswa awal:")
print(mahasiswa)

print("\n--- Menambah key baru ---")
print("Sebelum:", mahasiswa)
mahasiswa["jurusan"] = "Teknologi Rekayasa Perangkat Lunak"
print("Sesudah:", mahasiswa)

print("\n--- Mengubah nilai key ---")
print("Sebelum:", mahasiswa)
mahasiswa["kota"] = "Batam"
print("Sesudah:", mahasiswa)

print("\n--- Menghapus key ---")
print("Sebelum:", mahasiswa)
del mahasiswa["jurusan"]
print("Sesudah:", mahasiswa)

print("\nKeys:", mahasiswa.keys())
print("Values:", mahasiswa.values())
print("Items:", mahasiswa.items())

print("\nIterasi key: value:")
for key, value in mahasiswa.items():
    print(key, ":", value)


# 5. Nested Structures

print("\n=== 5. NESTED STRUCTURES ===")

daftar_buku = [
    {
        "judul": "Python Dasar",
        "penulis": "Lily",
        "tahun": 2022
    },
    {
        "judul": "Belajar Artificial Intelligence",
        "penulis": "Jasmine",
        "tahun": 2024
    },
    {
        "judul": "Pemrograman Web",
        "penulis": "Gabriela",
        "tahun": 2021
    },
    {
        "judul": "Data Science untuk Pemula",
        "penulis": "Hannah",
        "tahun": 2023
    }
]

print("Semua judul buku:")
for buku in daftar_buku:
    print("-", buku["judul"])

tahun_tertentu = 2023

buku_terfilter = [
    buku for buku in daftar_buku
    if buku["tahun"] >= tahun_tertentu
]

print("\nBuku yang terbit >= 2023:")
for buku in buku_terfilter:
    print("-", buku["judul"], "(", buku["tahun"], ")")


# 6. Comprehension & Utilitas

print("\n=== 6. COMPREHENSION & UTILITAS ===")

angka = list(range(1, 21))

angka_genap = [x for x in angka if x % 2 == 0]
angka_kuadrat = [x ** 2 for x in angka]

print("Angka 1-20:", angka)
print("Angka genap:", angka_genap)
print("Kuadrat angka 1-20:", angka_kuadrat)

status_angka = {
    x: "genap" if x % 2 == 0 else "ganjil"
    for x in range(1, 11)
}

print("\nDict comprehension:")
print(status_angka)

kalimat = "Python adalah bahasa pemrograman"

huruf_unik = {
    huruf.lower()
    for huruf in kalimat
    if huruf.isalpha()
}

print("\nKalimat:", kalimat)
print("Huruf unik:", huruf_unik)


# 7. Keanggotaan & Pencarian Sederhana

print("\n=== 7. KEANGGOTAAN & PENCARIAN SEDERHANA ===")

buah = ["Melon", "Pepaya", "Mangga", "Apel", "Semangka", "Anggur"]

print("List buah:", buah)

print("\nApel ada di list:", "Apel" in buah)
print("Durian ada di list:", "Durian" in buah)

buah_set = {"Melon", "Pepaya", "Mangga", "Apel", "Semangka", "Anggur"}

print("Mangga ada di set:", "Mangga" in buah_set)
print("Durian ada di set:", "Durian" in buah_set)

if "Mangga" in buah:
    print("Mangga ditemukan pada indeks:", buah.index("Mangga"))
else:
    print("Mangga tidak ditemukan.")