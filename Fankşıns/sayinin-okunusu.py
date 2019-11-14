"""
Problem 4
Kullanıcıdan 2 basamaklı bir sayı alın ve bu sayının okunuşunu bulan bir fonksiyon yazın.

Örnek: 97 ---------> Doksan Yedi
"""

birler =  ["","Bir","İki","Üç","Dört","Beş","Altı","Yedi","Sekiz","Dokuz"]
onlar = ["","On","Yirmi","Otuz","Kırk","Elli","Altmış","Yetmiş","Seksen","Doksan"]

def oku(sayi):

    a = int(sayi / 10)
    b = int(sayi % 10)

    print("",onlar[a],birler[b])


while True:
    sayi = input("Sayiyi giriniz(Cikmak icin q): ")

    if sayi == 'q':
        print("Cikis yapiliyor...")
        break
    else:
        sayi = int(sayi)
        oku(sayi)