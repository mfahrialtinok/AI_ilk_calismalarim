while True:
    try:
        sayi = int(input("Bir sayı giriniz..: "))
        break

    except ValueError:
        print("Lütfen SAYI giriniz", end="\n")

print("Bir sayı girdiğiniz için teşekkürler!")