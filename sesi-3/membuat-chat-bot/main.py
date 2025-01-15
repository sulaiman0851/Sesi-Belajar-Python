inputan_user = input("""
pilih opsi dibawah ini!
1. masukkan list
2. munculkkan list
: """)

if inputan_user == 1:
    masukkan()
elif inputan_user == 2:
    munculkan()
else:
    print("masukkan angka hanya yang ada pada opsi sebelumnya!")

def masukkan():
    inputuser = int(input("masukkan list"))
