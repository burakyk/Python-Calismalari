print("""****************************
Hesap Makinesi Programi

Islemler:

1.Toplama islemi
2.Cikarma islemi
3.Carpma islemi
4.Bolme islemi     
****************************      
""")

a = int(input("Birinci sayiyi giriniz: "))
b = int(input("Ikinci sayiyi giriniz: "))


islem = int(input("yapmak istediginiz islemi giriniz(1-4): "))



if islem == 1:
    print("{} ile {} toplami = {}".format(a,b,a+b))

elif islem == 2:
    print("{} - {}  = {}".format(a,b,a-b))

elif islem == 3:
    print("{} ile {} carpimi = {}".format(a,b,a*b))

elif islem == 4:
    print("{} / {}  = {}".format(a,b,a/b))

else :
    print("Lutfen gecerli bir islem sayisi giriniz !!!")
    islem = int(input("yapmak istediginiz islemi giriniz(1-4): "))
