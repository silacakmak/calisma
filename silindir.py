#silindirin yüzey alanı ve hacmini bulan uygulama
while True:
 x=int(input("silindirin yüzey alanı için 1,hacmi için 2,çıkış için 3'e basınız."))
 pi=3.14
 if(x==1 or x==2):
  r=float(input("silindirinizin yarıçapını giriniz:"))
  h=float(input("silindirinizin yüksekliğini giriniz:"))
  if x==1:
     ya=((2*pi*r)*h)+(2*pi*r*r)
     print("silindirinizin yüzey alanı:",ya)
  elif x==2:
     v=(pi*r*r)*h
     print("silindirinizin hacmi:",v)
 elif x==3:
     print("çıkış yapılıyor.")
     break
 else:
     print("geçerli bir değer giriniz.")


