print("Faktoriyel bulma programina hos geldiniz...")
print("Cikmak icin q ya basiniz.")

while True:
    sayi = input("sayiyi giriniz: ")

    if(sayi == 'q'):
        print("Program sonlandiriliyor...")
        break
    else:
        sayi = int(sayi)
        fact=1
        for i in range(2,sayi+1):
            fact*=i
    print("Faktoriyel = ",fact)