print("""
**************************
Hosgeldiniz...

Islemler: 
1. Bakiye sorgulama
2. Para yatirma
3. Para cekme

**************************""")
bakiye =1000
while True:
    islem = input("Islem numarasi giriniz(cikmak icin q): ")

    if islem == 'q' :
        print("Yine bekleriz :)")
        break

    elif islem=='1':
        print("Bakiyeniz :",bakiye)

    elif islem=='2':
        a= int(input("Kac TL yatirmak istersiniz: "))
        bakiye +=a
        print("Isleminiz basariyla tamamlandi.")

    elif islem=='3':
        b=int(input("Kac TL cekmek istersiniz: "))
        if b<=bakiye:
            bakiye -=b
            print("Isleminiz basariyla tamamlandi.")
        else:
            print("islem basarisiz.Cekmek istediginiz tutar bakiyeden yuksek.")
