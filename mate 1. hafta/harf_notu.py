vize = float(input("Vize notunu giriniz(100 üzerinden)..: "))
final = float(input("Final notunu giriniz(100 üzerinden)..: "))

def harf_notu_hesapla(a,b):
    yuzluk_sonuc = a*40/100 + b*60/100
    if yuzluk_sonuc <= 100 and yuzluk_sonuc >= 90:
        harf_notu = "AA"
    elif yuzluk_sonuc < 90 and yuzluk_sonuc >= 80:
        harf_notu = "BA"
    elif yuzluk_sonuc < 80 and yuzluk_sonuc >= 70:
        harf_notu = "BB"
    elif yuzluk_sonuc < 70 and yuzluk_sonuc >= 60:
        harf_notu = "CB"
    elif yuzluk_sonuc < 60 and yuzluk_sonuc >= 50:
        harf_notu = "CC"
    elif yuzluk_sonuc < 50 and yuzluk_sonuc >= 40:
        harf_notu = "DC"
    elif yuzluk_sonuc < 40 and yuzluk_sonuc >= 30:
        harf_notu = "DD"
    elif yuzluk_sonuc < 30 and yuzluk_sonuc >= 20:
        harf_notu = "FD"
    elif yuzluk_sonuc < 20 and yuzluk_sonuc >= 0:
        harf_notu = "FF"
    return print(harf_notu)

harf_notu_hesapla(vize, final)