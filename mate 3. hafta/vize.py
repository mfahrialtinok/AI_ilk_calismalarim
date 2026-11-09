import datetime
import time

print("Lütfen vize tarihinizi girin.")
gun = int(input("Gün..: "))
ay = int(input("Ay...: "))
yil = int(input("Yıl..: "))
saat = int(input("Saat.: "))
dakika = int(input("Dk...: "))

vize = datetime.datetime(day=gun, month=ay, year=yil, hour=saat, minute=dakika)

print("\nGirdiğiniz vize tarihi..: ", vize.strftime("%d/%m/%Y %H:%M"))

while True:
    su_an = datetime.datetime.now()
    kalan_zaman = vize - su_an
    kalan_zaman_temiz = str(kalan_zaman).split(".")[0]

    print(f"Sınava kalan süre..: {kalan_zaman_temiz}", end="\r")