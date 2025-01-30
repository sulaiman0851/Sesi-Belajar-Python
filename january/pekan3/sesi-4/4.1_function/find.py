import random

angka_rahasia = random.randint(10)

jawaban_user = int(input("masukkan angka: "))

if jawaban_user == angka_rahasia:
    print("jawaban kamu benar!")
else:
    print("salah!")