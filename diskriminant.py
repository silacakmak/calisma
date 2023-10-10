#ikinci dereceden denklemlerde dikriminant uygulaması
# ax2+bx+c
import math
a=int(input("derecesi 2 olan bilinmeyenin katsayısını giriniz:"))
b=int(input("derecesi 1 olan bilinmeyenin katsayısını giriniz:"))
c=int(input("derecesi 0 olan bilinmeyenin katsayısını giriniz:"))
delta=(b*b)-(4*a*c)
if(delta<0):
    print("denklemin kökü yoktur")
elif(delta==0):
    print("denklemin eşit iki kökü vardır.")
    x=(-b)/(2*a)
    print("kökler:",x)
elif(delta>0):
    print("denklemin birbirinden farklı iki kökü vardır.")
    x1=((-b)-math.sqrt(delta))/(2*a)
    x2=((-b)+math.sqrt(delta))/(2*a)
    print("denklemin birinci kökü:",x1,"denklemin ikinci kökü:",x2)
