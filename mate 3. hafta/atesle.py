import time

sayi = int(input("Bir sayı gir..: "))

while sayi != 0:
    print(sayi)
    sayi -= 1
    time.sleep(1)

print("Ateşle!")