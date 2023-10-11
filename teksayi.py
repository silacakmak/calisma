print("sayı aralığını giriniz.\n")
k=int(input("başlangıç sayısını giriniz."))
b=int(input("aralığın bitiş sayısını giriniz"))
for k in range(k,b,1):
    if k%2!=0:
        print(k)