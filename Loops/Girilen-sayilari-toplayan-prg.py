"""
Problem 4
Her bir while döngüsünde kullanıcıdan bir sayı alın ve kullanıcının girdiği sayıları "toplam" isimli bir değişkene ekleyin. Kullanıcı "q" tuşuna bastığı zaman döngüyü sonlandırın ve ekrana "toplam değişkenini" bastırın.

İpucu : while döngüsünü sonsuz koşulla başlatın ve kullanıcı q'ya basarsa döngüyü break ile sonlandırın.
"""
toplam=0
while True:
    a = input("Toplama eklemek istediginiz sayiyi giriniz: ")
    if a == 'q':
        print("Toplam :",toplam)
        break
    a=int(a)
    toplam += a
