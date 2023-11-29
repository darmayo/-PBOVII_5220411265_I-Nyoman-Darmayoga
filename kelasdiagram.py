# Definisi kelas Perpustakaan
class Perpustakaan:
    def __init__(self, nama, lokasi):
        self.nama = nama
        self.lokasi = lokasi

# Definisi kelas PerpusItem
class PerpusItem:
    def __init__(self):
        self.katalog = []

    def tambah(self, item):
        self.katalog.append(item)

# Definisi kelas Buku
class Buku:
    def __init__(self, judul, kategori, isbn, penulis, halaman, ukuran, rak, sinopsis):
        self.judul = judul
        self.kategori = kategori
        self.isbn = isbn
        self.penulis = penulis
        self.halaman = halaman
        self.ukuran = ukuran
        self.rak = rak
        self.sinopsis = sinopsis

# Definisi kelas Majalah
class Majalah:
    def __init__(self, judul, kategori, issn, editor, halaman, ukuran, rak, ringkasan, volume, edisi):
        self.judul = judul
        self.kategori = kategori
        self.issn = issn
        self.editor = editor
        self.halaman = halaman
        self.ukuran = ukuran
        self.rak = rak
        self.ringkasan = ringkasan
        self.volume = volume
        self.edisi = edisi

# Definisi kelas DVD
class DVD:
    def __init__(self, judul, kategori, kode, sutradara, durasi, format_, rak, ringkasan, pemeran, genre):
        self.judul = judul
        self.kategori = kategori
        self.kode = kode
        self.sutradara = sutradara
        self.durasi = durasi
        self.format_ = format_
        self.rak = rak
        self.ringkasan = ringkasan
        self.pemeran = pemeran
        self.genre = genre

# Contoh penggunaan
if __name__ == "__main__":
    perpustakaan = Perpustakaan("Perpustakaan Umum", "Perpustakaan Kota")
    perpustakaan_item = PerpusItem()

    buku1 = Buku("Python for Beginners", "Programming", "978-1-564319-102-6", "darma", 300, "A5", "Rak 1", "Dasar-dasar pemrograman Python")
    majalah1 = Majalah("Data Science Weekly", "Data Science", "123-4-1234-9122-3", "shidiq", 50, "A4", "Rak 2", "Ringkasan mingguan berita ilmu data", 10, 52)
    dvd1 = DVD("The Matrix", "Sci-Fi", "987-6-5432-1098-7", "momoy", 120, "DVD", "Rak 3", "Film sci-fi klasik", "dodit", "Sci-Fi")

    perpustakaan_item.tambah(buku1)
    perpustakaan_item.tambah(majalah1)
    perpustakaan_item.tambah(dvd1)

    print(f"\nPerpustakaan: {perpustakaan.nama}\nLokasi: {perpustakaan.lokasi}\n")
    print("Katalog:")
    for item in perpustakaan_item.katalog:
        if isinstance(item, Buku):
            print(f"Buku: {item.judul}\nKategori: {item.kategori}\nISBN: {item.isbn}\nPenulis: {item.penulis}\nHalaman: {item.halaman}\nUkuran: {item.ukuran}\nRak: {item.rak}\nSinopsis: {item.sinopsis}\n")
        elif isinstance(item, Majalah):
            print(f"Majalah: {item.judul}\nKategori: {item.kategori}\nISSN: {item.issn}\nEditor: {item.editor}\nHalaman: {item.halaman}\nUkuran: {item.ukuran}\nRak: {item.rak}\nRingkasan: {item.ringkasan}\nVolume: {item.volume}\nEdisi: {item.edisi}\n")
        elif isinstance(item, DVD):
            print(f"DVD: {item.judul}\nKategori: {item.kategori}\nKode: {item.kode}\nSutradara: {item.sutradara}\nDurasi: {item.durasi}\nFormat: {item.format_}\nRak: {item.rak}\nRingkasan: {item.ringkasan}\nPemeran: {item.pemeran}\nGenre: {item.genre}\n")
