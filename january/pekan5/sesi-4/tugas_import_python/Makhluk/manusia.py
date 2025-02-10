from Makhluk import MakhlukHidup

class Manusia(MakhlukHidup):
    def __init__(self, pekerjaan, bahasa, kewarganegaraan):
        self.pekerjaan = pekerjaan
        self.bahasa = bahasa
        self.kewarganegaraan = kewarganegaraan

    def berpikir(self):
        return f"👨‍💻Manusia mempunyai pekerjaan: {self.pekerjaan}\n🧏‍♂️Manusia ini berbahasa: {self.bahasa}\n🆔Kewarganegaraan: {self.kewarganegaraan}"

    def berbicara():
        print("manusia bisa berbicara")

    def berkarya():
        print("manusia bisa berkarya")