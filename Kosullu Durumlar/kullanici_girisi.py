print("*******************************\nKullanici girisi\n*******************************")

username = 'byk'
password = 'xoraxjusttry'

username_1 = input("Kullanici adinizi giriniz: ")
password_1 = input("Sifreyi giriniz: ")

if username==username_1 and password==password_1:
    print("Giris yapiliyor lutfen bekleyiniz...")

elif username==username_1 and password!=password_1:
    print("Hatali sifre girisi")

elif username!=username_1 and password==password_1:
    print("Hatali kullanici adi girisi")

else:
    print("Kullanici adi ve sifre hatali")