"""
Problem 5
1'den 100'e kadar olan sayılardan pisagor üçgeni oluşturanları ekrana yazdıran bir fonksiyon yazın.(a <= 100,b <= 100)
"""
#-----BYK-----

def pisagor():

    pisagor_listesi = []
    for i in range(1,101):
        for j in range(1,101):
            a =( j**2 + i**2 ) ** 0.5
            if a == int(a):
                pisagor_listesi.append((i,j,int(a)))
    return pisagor_listesi
for i in pisagor():
    print(i)