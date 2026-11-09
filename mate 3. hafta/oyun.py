import random

random_sayi = random.randint(1,100)

while True:
    try:
        user = int(input("Bir sayı gir(1 ile 100 arasında)..: "))
        if user > random_sayi:
            print("Tahminin seçtiğim sayıdan büyük.")

        elif user < random_sayi:
            print("Tahminin seçtiğim sayıdan küçük.")

        else:
            break
    except ValueError:
        print("Lütfen sayı gir.")

print("Tebrikler doğru tahmin ettin!")