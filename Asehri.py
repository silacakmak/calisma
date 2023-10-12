while True:
    x=int(input("para miktarını giriniz:"))
    y=int(x/100)
    e=int((x-(y*100))/50)
    o=int((x-((e*50)+(y*100)))/10)
    b=int(x-((e*50)+(y*100)+(o*10)))
    if x==0:
        print("paranız yok fakirsiniz.")
        break
    elif x>100:
        top=int(y+e+o+b)
        print(y,"tane yüzlük bankot,",e,"tane ellilik bankot,",o,"tane onluk bankot,",b,"tane birlik bankot vardır.")
        print("toplam ",top,"tane bankot vardır.")
    elif x>50 and x<100:
        top = int( e + o + b)
        print( e, "tane ellilik bankot,", o, "tane onluk bankot,", b,
              "tane birlik bankot vardır.")
        print("toplam ",  top, "tane bankot vardır.")
    elif x<50 and x>10:
        top = int(o + b)
        print( o, "tane onluk bankot,", b,
              "tane birlik bankot vardır.")
        print("toplam ",  top, "tane bankot vardır.")
    elif x>0 and x<10 :
        top = int( b)
        print( b,
              "tane birlik bankot vardır.")
        print("toplam ",  b, "tane bankot vardır.")
    else:
        print("geçerli bir değer giriniz.")





