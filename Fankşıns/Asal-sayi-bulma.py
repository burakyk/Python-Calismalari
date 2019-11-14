def asallik(sayi):
    if(sayi == 1):
        return False
    elif(sayi == 2):
        return True
    else:
        for i in range(2,sayi):
            if (sayi % i == 0):
                return False
        return True

while True:
    sayi = input("Sayiyi giriniz(Cikmak icin q): ")

    if (sayi == 'q'):
        break

    else:
        sayi = int(sayi)

        if asallik(sayi):
            print("Girilen sayi asal !")
        else:
            print("Girilen sayi asal degil.")

print("Written by BYK")