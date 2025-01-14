# Meminta input nilai ujian
nilai_input = input("Masukkan nilai ujian (1-100): ")

# Mengecek apakah input adalah angka 
# dan dalam rentang 0-100
if nilai_input.isdigit():
    nilai = int(nilai_input)
    
    if nilai < 1 or nilai > 100:
        print("Nilai yang kamu inputkan salah, tolong masukkan angka antara 1 sampai 100.")
    else:
        # Menentukan tingkat pencapaian berdasarkan nilai
        if nilai >= 90:
            pencapaian = "A (Sangat Baik)"
        elif nilai >= 80:
            pencapaian = "B (Baik)"
        elif nilai >= 70:
            pencapaian = "C (Cukup)"
        elif nilai >= 60:
            pencapaian = "D (Kurang)"
        else:
            pencapaian = "E (Sangat Kurang)"
        
        # Menampilkan hasil
        print(f"Nilai Anda: {pencapaian}")
        
        # Menentukan apakah lulus atau tidak
        if nilai >= 70:
            print("Selamat! Anda lulus ujian.")
        else:
            print("Mohon belajar lebih giat, Anda belum lulus.")
else:
    print("Nilai yang kamu inputkan salah, tolong gunakan angka!")
