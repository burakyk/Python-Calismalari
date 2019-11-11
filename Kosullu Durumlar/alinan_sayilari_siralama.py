a = float(input("1. sayiyi giriniz: "))
b = float(input("2. sayiyi giriniz: "))
c = float(input("3. sayiyi giriniz: "))

enbuyuk = ""
enkucuk = ""
orta = ""


if a>b and a>c:
    enbuyuk = a
    if b>c:
        enkucuk=c
        orta=b
    else:
        enkucuk=b
        orta =c

if b>c and b>a:
    enbuyuk=b
    if a>c:
        enkucuk=c
        orta =a
    else:
        enkucuk=a
        orta =c

if c>a and c>b:
    enbuyuk=c
    if b>a:
        enkucuk=a
        orta =b
    else:
        enkucuk=b
        orta =a


print("girilen en buyuk sayi {}",enbuyuk)
print("{} > {} > {}".format(enbuyuk,orta,enkucuk))