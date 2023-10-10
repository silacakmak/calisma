#pozitif bölenlerin toplamını bulan uygulama
x=int(input("bir sayı giriniz:"))
sum=0


for i in range(1,x+1):
    if(x%i==0):
        sum=sum+i
    i=i+1
print("pozitif bölenlerin toplamı:",sum)


