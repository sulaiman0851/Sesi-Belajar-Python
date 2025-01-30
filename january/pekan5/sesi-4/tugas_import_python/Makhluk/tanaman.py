from Makhluk import MakhlukHidup

class Tanaman(MakhlukHidup):
    def __init__(self, jenisBunga, warnaBunga):
        self.jenisBunga = jenisBunga
        self.warnaBunga = warnaBunga

    def menyerap_air(self):
        print(f"{self.jenisBunga} bisa menyerap air")

    def berbunga(self):
        print(f"{self.jenisBunga} bisa berbunga")