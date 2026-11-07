fiyat = int(input("Ürünün fiyatını gir(tl)..: "))
indirim = int(input("İndirim oranı yüzde kaç?..: "))

def indirim_hesapla(a, b):
    return a - a*b/100 

print(indirim_hesapla(fiyat, indirim), "tl")