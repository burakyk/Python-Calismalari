"""
Problem 1
Kullanıcıdan aldığınız bir sayının mükemmel olup olmadığını bulmaya çalışın.

Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse bu sayıya "mükemmel sayı" denir. Örnek olarak, 6 mükemmel bir sayıdır. (1 + 2 + 3 = 6)
"""

sayi = int(input("Sayi giriniz"))

dizi = []
toplam=0
for i in range(1,sayi):
    if sayi%i==0 :
        dizi.append(i)

for i in dizi:
    toplam+=i

if toplam == sayi:
    print("Bu sayi Mukemmel bir sayidir.")
else:
    print("Girdiginiz sayi mukemmel bir sayi degil :)")