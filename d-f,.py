#dereceyi fahrenheit a çevirme uygulaması
while True:
 x=int(input("dereceyi fahrenheit'a çevirmek için 1 ,fahrenheit 'ı dereceye çevirmek için 2,tekrar başlatmak "
             "için 3'e basınız."))
 if x==1:
     y=float(input("Çevirmek istediğiniz dereceyi girin:"))
     f=(y * 1.8)+ 32
     print("girdiğiniz derecenin fahrenheit değeri=",f)
 elif x==2:
     y = float(input("Çevirmek istediğiniz fahrenheit değerini girin:"))
     c=(y-32)/1.8
     print("girdiğiniz fahrenheit değerinin  derece değeri=", c)
 elif x==3:
     print("çıkış yapılıyor,program tekrar başlatılıyor.")
     break

 else:
     print("lütfen geçerli bir değer giriniz.")



