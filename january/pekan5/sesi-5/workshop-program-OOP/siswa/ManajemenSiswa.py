from .Siswa import Siswa

class ManajemenSiswa:
    def __init__(self):
        self.daftar_siswa = []

    def tambah_siswa(self, nama, kelas, nilai_rata_rata):
        siswa = Siswa(nama, kelas, nilai_rata_rata)
        self.daftar_siswa.append(siswa)

    def lihat_siswa(self):
        if not self.daftar_siswa:
            print("Belum ada data siswa.")
        else:
            for i, siswa in enumerate(self.daftar_siswa, start=1):
                print(f"{i}. {siswa.info()}")

    def hapus_siswa(self, nama):
        for siswa in self.daftar_siswa:
            if siswa.nama == nama:
                self.daftar_siswa.remove(siswa)
                print(f"Siswa {nama} berhasil dihapus.")
                return
        print(f"Siswa {nama} tidak ditemukan.")