from datetime import datetime

user = int(input("Doğum yılınız nedir?..: "))
this_year = datetime.now().year

if this_year - user >= 18:
    print("Ehliyet alabilirsin.")

else: 
    print("Henüz reşit değilsin.")