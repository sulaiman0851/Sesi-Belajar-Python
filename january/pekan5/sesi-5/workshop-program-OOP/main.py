from siswa.ManajemenSiswa import ManajemenSiswa

# Inisialisasi ManajemenSiswa
manajemen = ManajemenSiswa()

while True:
    print("\nMenu:")
    print("1. Tambah Siswa")
    print("2. Lihat Siswa")
    print("3. Hapus Siswa")
    print("4. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        nama = input("Nama: ")
        kelas = input("Kelas: ")
        nilai_rata_rata = float(input("Nilai Rata-rata: "))
        manajemen.tambah_siswa(nama, kelas, nilai_rata_rata)
    elif pilihan == "2":
        manajemen.lihat_siswa()
    elif pilihan == "3":
        nama = input("Nama siswa yang ingin dihapus: ")
        manajemen.hapus_siswa(nama)
    elif pilihan == "4":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid.")