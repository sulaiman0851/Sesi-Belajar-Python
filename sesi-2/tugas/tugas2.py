# Meminta jumlah nilai yang ingin dimasukkan
jumlah_nilai = input("Berapa nilai yang ingin anda Jumlahkan: ")

# Mengecek apakah input adalah angka
if jumlah_nilai.isdigit():
    jumlah_nilai = int(jumlah_nilai)
    
    # Membuat list untuk menyimpan nilai
    nilai_list = []
    
    # Meminta input nilai sesuai jumlah yang diminta
    for i in range(1, jumlah_nilai + 1):
        nilai = input(f"Masukkan Nilai ke-{i}: ")
        
        # Mengecek apakah nilai yang dimasukkan adalah angka
        if nilai.isdigit():
            nilai = int(nilai)
            
            # Mengecek apakah nilai berada dalam rentang yang valid
            if nilai < 1 or nilai > 100:
                print("Nilai kamu gak masuk akal, tolong masukkan lagi dengan benar!")
                break
            else:
                nilai_list.append(nilai)
        else:
            print("Input salah, tolong masukkan angka.")
            break
    else:
        # Menghitung rata-rata, nilai tertinggi, dan nilai terendah
        rata_rata = sum(nilai_list) / len(nilai_list)
        nilai_tertinggi = max(nilai_list)
        nilai_terendah = min(nilai_list)
        
        # Menampilkan hasil
        print(f"Nilai Rata-rata = {rata_rata}")
        print(f"Nilai Tertinggi = {nilai_tertinggi}")
        print(f"Nilai Terendah = {nilai_terendah}")
else:
    print("Input jumlah nilai salah, tolong masukkan angka.")
