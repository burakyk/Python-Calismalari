print("FAKTORIYEL BULMA")

a = int(input("Faktoriyelini almak istediginiz sayiyi giriniz: "))
fact=1
b=a
while a>1:
    fact*=a
    a-=1
print("{} Sayisinin Faktoriyeli : {}".format(b,fact))

