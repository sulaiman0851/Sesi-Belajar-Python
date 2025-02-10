class Siswa:
    def __init__(self, nama, kelas, nilai_rata_rata):
        self.nama = nama
        self.kelas = kelas
        self.nilai_rata_rata = nilai_rata_rata

    def info(self):
        return f"Nama: {self.nama}, Kelas: {self.kelas}, Nilai Rata-rata: {self.nilai_rata_rata}"