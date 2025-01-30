#    5 Latihan Struktur Data Dasar
#    Latihan 1: List
#    Buat program untuk:
#    1.Membuat list berisi 5 nama.          ✔
#    2.Menambahkan satu nama ke dalam list. ✔
#    3.Menghapus satu nama dari list.       ✔
#    4.Mengurutkan list secara alfabetis.   ✔
#    
#    Kode yang diharapkan:
#    nama = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
#    nama.append("Frank")
#    nama.remove("Charlie")
#    nama.sort()
#    print(nama)

# 1.Membuat list berisi 5 nama.
nama = ["Alice", "Bob", "Charlie", "Diana", "Eve"]

# 2.Menambahkan satu nama ke dalam list.
nama.append("Frank")

# 3.Menghapus satu nama dari list.
nama.remove("Charlie")

# 4.Mengurutkan list secara alfabetis.
nama.sort()


print(nama,"\n\n\n\n")







# Latihan 2: Tuple
# Buat program untuk:
# 1.Membuat tuple berisi 5 angka.
# 2.Menghitung jumlah angka tertentu di dalam tuple.
# 3.Menampilkan indeks dari angka pertama yang ditemukan.
# Kode yang diharapkan:
angka = (1, 2, 3, 2, 4)
print(angka.count(2))  # Output: 2
print(angka.index(3))  # Output: 2