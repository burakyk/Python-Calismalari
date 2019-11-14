def tambolen(sayi):
    x = []
    for i in range(2,sayi):
        if(sayi % i ==0):
            x.append(i)
    return x

while True:
    sayi = input("Sayi(Cikmak icin q): ")

    if(sayi == "q"):
        print("Program sonlandiriliyor...")
        break

    else:
        sayi = int(sayi)
        print("Tam bolenler : ",tambolen(sayi))

print("btw Written by BYK canim haberin olsun")