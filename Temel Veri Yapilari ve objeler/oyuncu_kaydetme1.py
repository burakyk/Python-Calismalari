print("Oyuncu kaydetme programi")
ad = input("Oyuncunun adi: ")
soyad= input("Oyuncunun soyadi: ")
takim = input("Oyuncunun takimi: ")

bilgiler = [ad,soyad,takim]

print("Bilgiler kaydediliyor...")

print("Oyuncu adi: {}\nOyuncu Soyadi: {}\nOyuncunun takimi: {}".format (bilgiler[0],bilgiler[1],bilgiler[2]))