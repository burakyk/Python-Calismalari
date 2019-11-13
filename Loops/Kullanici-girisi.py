print("""************************
Kullanici Giris Programi
************************""")

sys_username = "byk"
sys_passwd = "hellostranger:)"
giris_hakki = 3
while True:
    username = input("Kullanici adini giriniz: ")
    passwd = input("Sifrenizi giriniz: ")

    if sys_username != username or sys_passwd != passwd:
        giris_hakki -= 1
        if giris_hakki == 0:
            print("Dogrulama bloklandi lutfen daha sonra tekrar deneyiniz...")
            break
        print("Kullanici adi veya sifre yanlis lutfen tekrar deneyiniz...")


    else:
        print("Giris yapiliyor lutfen bekleyiniz...")
        break