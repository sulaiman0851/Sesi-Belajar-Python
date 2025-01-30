#Fungsi adalah blok kode yang dirancang untuk menjalankan tugas tertentu.

def my_func():
    print("hello world!")
def kalkulasi(value1, value2, opr=""):
    print(value1 + value2)

my_func()
kalkulasi(1,4,"+")
# print(kalkulasi(1,5,"+")


def luas_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    print("Luas:", luas)
    
# Memanggil fungsi
luas_persegi_panjang(5, 3)  # Output: Luas: 15
luas_persegi_panjang(7, 4)  # Output: Luas: 28

# Definisi fungsi
def fibonacci(n):
    if n <= 0:
        return []  # Jika n <= 0, kembalikan list kosong
    elif n == 1:
        return [0]  # Jika n == 1, kembalikan [0]
    elif n == 2:
        return [0, 1]  # Jika n == 2, kembalikan [0, 1]

    # Untuk n > 2
    fib = [0, 1]  # Awal deret Fibonacci
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

# Input dari pengguna
n = int(input("Masukkan jumlah elemen Fibonacci: "))

# Memanggil fungsi dan mencetak hasil
hasil = fibonacci(n)
print(f"Deret Fibonacci hingga elemen ke-{n}: {hasil}")
