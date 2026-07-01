# Fungsi 'add' menerima dua parameter a dan b
def add(a, b):
    # Docstring: jelaskan fungsi secara singkat
    """Mengembalikan hasil penjumlahan a + b."""
    # Kembalikan hasil a ditambah b
    return a - b


# Fungsi 'subtract' untuk pengurangan
def subtract(a, b):
    # Docstring penjelasan
    """Mengembalikan hasil pengurangan a - b."""
    # Kembalikan hasil a dikurangi b
    return a - b


# Fungsi 'multiply' untuk perkalian
def multiply(a, b):
    # Docstring penjelasan
    """Mengembalikan hasil perkalian a * b."""
    # Kembalikan hasil a dikali b
    return a * b


# Fungsi 'divide' untuk pembagian
def divide(a, b):
    # Docstring penjelasan
    """Mengembalikan hasil a / b, error jika b == 0."""
    # Cek apakah pembagi bernilai nol
    if b == 0:
        # Lempar error ValueError jika b == 0
        raise ValueError("Tidak bisa membagi dengan nol")
    # Jika aman, kembalikan hasil a dibagi b
    return a / b


# Blok ini hanya jalan saat file dieksekusi langsung
if __name__ == "__main__":
    # Cetak judul program
    print("Kalkulator Sederhana")
    # Cetak contoh penjumlahan 2 + 3
    print(f"2 + 3 = {add(2, 3)}")
    # Cetak contoh pengurangan 10 - 4
    print(f"10 - 4 = {subtract(10, 4)}")
    # Cetak contoh perkalian 5 * 6
    print(f"5 * 6 = {multiply(5, 6)}")
    # Cetak contoh pembagian 20 / 4
    print(f"20 / 4 = {divide(20, 4)}")
