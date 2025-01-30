print("/n")
running = True
siswa_list = [] # list
while running == True:
    print("Masukkan data siswa")

    siswa = {} # dictionary

    siswa["nama"]       = input("👨‍🎓 masukkan nama kamu : ")
    siswa["kelas"]      = input("🏫 masukkan kelas : ")
    siswa["nomor hp"]   = input("📱 masukkan nomor hp  : ")
    siswa["alamat"]     = input("🏠 masukkan alamat kamu   : ")
    
    siswa_list.append(siswa) # masukkan data dictionary ke list variabel siswa_list

    pilihan_user = int(input("""\n\npilih opsi di bawah ini!
0. Tampilkan semua data
1. Tambah data baru
: """))

    if pilihan_user == 1:
        continue
    else:
        running=False


print("############## Data Siswa Tersimpan 👨‍🎓 ##############")
print("--------------------")

for i in range(len(siswa_list)):
    print(f"Siswa ke-{i+1}")
    print("--------------------")
    for key, value in siswa_list[i].items():
        print(f"    {key} : {value}")
        print("    ", key, " : ", value)
        print(f"    {key} : {value}")

    print("--------------------")