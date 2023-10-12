import random
while True:
    x=int(input("Zar tahmininizi giriniz:"))
    print("bilgisayar zarı atıyor...")
    a=random.randint(1,6)
    if(a==x):
        print("zar değeri:", a)
        print("Tahmininiz doğru.Kazandınız.")
        break
    elif x<0 or x>6:
        print("Geçersiz değer girdiniz,lütfen geçerli bir sayı giriniz.")
        continue
    elif x!=a:
        print("zar değeri:",a)
        print("tahmininiz yanlış bir daha deneyin.")
        continue



