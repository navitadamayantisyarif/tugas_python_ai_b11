# Tugas 5 - Python Function and Class


# ==========================================
# 1. FUNCTION
# ==========================================

def greet(nama: str) -> str:
    """
    Mengembalikan teks sapaan.
    """
    return f"Halo, {nama}!"


def tambah(a: float, b: float = 0.0) -> float:
    """
    Mengembalikan hasil penjumlahan a + b.
    """
    return a + b


def rata_rata(angka: list[float]) -> float:
    """
    Mengembalikan rata-rata angka dengan 2 angka di belakang koma.
    Jika list kosong, mengembalikan 0.0.
    """
    if len(angka) == 0:
        return 0.0

    return round(sum(angka) / len(angka), 2)


# ==========================================
# 2. CLASS STUDENT
# ==========================================

class Student:
    def __init__(
        self,
        nama: str,
        nim: str,
        nilai: list[float] | None = None
    ):
        """
        Inisialisasi data mahasiswa.
        """
        self.nama = nama
        self.nim = nim
        self.nilai = nilai if nilai is not None else []

    def tambah_nilai(self, skor: float):
        """
        Menambahkan satu skor ke dalam list nilai.
        """
        self.nilai.append(skor)

    def rata_nilai(self) -> float:
        """
        Menghitung rata-rata nilai menggunakan function rata_rata().
        """
        return rata_rata(self.nilai)

    def status(self, threshold: float = 70.0) -> str:
        """
        Mengembalikan status LULUS jika rata-rata >= threshold.
        """
        if self.rata_nilai() >= threshold:
            return "LULUS"

        return "TIDAK LULUS"

    def __str__(self):
        """
        Mengembalikan representasi string objek Student.
        """
        return (
            f"Student(nama='{self.nama}', "
            f"nim='{self.nim}', "
            f"rata={self.rata_nilai()}, "
            f"status={self.status()})"
        )


# ==========================================
# 3. DEMO PROGRAM
# ==========================================

if __name__ == "__main__":

    print("=== FUNCTIONS ===")

    # Demo greet()
    print("greet('Gabriela'):", greet("Gabriela"))

    # Demo tambah()
    print("tambah(5, 7):", tambah(5, 7))
    print("tambah(10):", tambah(10))

    # Demo rata_rata()
    print("rata_rata([80, 90, 100]):", rata_rata([80, 90, 100]))
    print("rata_rata([]):", rata_rata([]))


    print("\n=== CLASS STUDENT ===")

    # Membuat mahasiswa pertama
    mahasiswa1 = Student(
        nama="Navita",
        nim="12345678"
    )

    mahasiswa1.tambah_nilai(80)
    mahasiswa1.tambah_nilai(85)
    mahasiswa1.tambah_nilai(90)

    # Membuat mahasiswa kedua
    mahasiswa2 = Student(
        nama="Lily",
        nim="22334455"
    )

    mahasiswa2.tambah_nilai(60)
    mahasiswa2.tambah_nilai(65)
    mahasiswa2.tambah_nilai(70)

    # Menampilkan mahasiswa pertama
    print("\nData mahasiswa pertama:")
    print(mahasiswa1)
    print("Nilai:", mahasiswa1.nilai)
    print("Rata-rata:", mahasiswa1.rata_nilai())
    print("Status:", mahasiswa1.status())

    # Menampilkan mahasiswa kedua
    print("\nData mahasiswa kedua:")
    print(mahasiswa2)
    print("Nilai:", mahasiswa2.nilai)
    print("Rata-rata:", mahasiswa2.rata_nilai())
    print("Status:", mahasiswa2.status())