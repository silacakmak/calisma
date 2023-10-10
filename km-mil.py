

#km-mil hesaplama

while True:
    x = int(input("Çıkmak için 0'a, km'den mile dönüştürmek için 1'e, mil'den km'ye dönüştürmek için 2'ye basınız: "))

    if x == 1:
        try:
            y = float(input("Mile dönüştürmek istediğiniz kilometreyi yazınız: "))
            omil = y * 1.609344
            print(y, " km = ", omil, " mil eder.")
        except ValueError:
            print("Geçerli bir sayı giriniz.")

    elif x == 2:
        try:
            y = float(input("Km'ye dönüştürmek istediğiniz mili yazınız: "))
            omil = y * 0.621371192
            print(y, " mil = ", omil, " km eder.")
        except ValueError:
            print("Geçerli bir sayı giriniz.")

    elif x == 0:
        print("Çıkış yapılıyor")
        exit()

    else:
        print("Geçerli bir değer giriniz.")
        break
