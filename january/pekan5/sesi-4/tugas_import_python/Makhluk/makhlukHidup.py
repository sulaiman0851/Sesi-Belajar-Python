class MakhlukHidup():
    def __init__(self, nama, jenis, umur):
        self.nama = nama
        self.jenis = jenis
        self.umur = umur
        print(f"jenis: {jenis}\nNama {jenis}: {nama}\numur {jenis}: {umur} tahun")
    
    def bernafas(self, nafas_type):
        return f"{self.jenis} {self.nama} bernafas dengan {nafas_type}"

    def bergerak(self):
        return f"{self.jenis} {self.nama} bisa bergerak"

    def berkembang_biak(self, type_ngentot):
        return f"{self.jenis} {self.nama} berkembang biak dengan cara {type_ngentot}"