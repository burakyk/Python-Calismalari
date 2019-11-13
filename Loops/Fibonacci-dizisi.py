a = 1
b =1
fibonacci = [a,b]

x = int(input("Fibonacci dizisinin ilk kac terimini gormek istersiniz: "))

for i in range(x-2):
    a,b = b,a+b
    fibonacci.append(b)

print(fibonacci)