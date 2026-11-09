N = int(input("Bir sayı söyle..: "))
toplam = 0

for i in range(N+1):
    toplam += i

print("1'den", N ,"ye kadar toplam..: ", toplam)