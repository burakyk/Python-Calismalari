print("""****************************
Geometrik sekil hesaplama programi
***************************""")

sekil = input("Tipini bulmak istediginiz cokgeni yaziniz(ucgen-dortgen)")

if sekil=='ucgen':

    a = int(input("Ucgenin girmek istediginiz ilk kenari: "))
    b = int(input("Ucgenin girmek istediginiz ikinci kenari: "))
    c = int(input("Ucgenin girmek istediginiz diger kenari: "))

    if a + b > c > abs(a - b) or b + c > a > abs(b - c) or a + c > b > abs(a - c):

        if a==b and b==c:
            print("Ucgeniniz Eskenar bir ucgen")
        elif a==b or a==c or b==c:
            print("Ucgeniniz ikizkenar.")
        else:
            print("Girilen ucgen cesitkenar.")

    else:
        print("Girdiginiz degerlerle bir ucgen olusturulamaz.")

elif sekil=='dortgen':
    print("Lütfen kenarları sırayla giriniz.")
    a = int(input("Kenar-1:"))
    b = int(input("Kenar-2:"))
    c = int(input("Kenar-3:"))
    d = int(input("Kenar-4:"))

    if (a == b and a == c and a == d):
        print("Kare")
    elif (a == c and b == d):
        print("Dikdörtgen")
    else:
        print("Dörtgen")

else :
    print("Lutfen belirtilen cokgenlerden birini giriniz.")