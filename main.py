import json

sozluk='{"isim":"sıla","yas":"21","maas":4000,"medeni hali":"bekar"}'
bilgi=json.loads(sozluk)
with open("dosya.json","w",encoding="utf-8") as index:
    json.dump(bilgi,index)
    while True:
        x=int(input("kullanıcı bilgileri için 1,maaşa zam için 2,çıkmak için 3'e basınız."))
        if(x==1):
            print("kullanıcı bilgileri:",bilgi)
        elif(x==2):
            y=int(input("zam miktarını yazınız:"))

            bilgi["maas"]=bilgi["maas"]+y
            print("yeni maaş:",bilgi["maas"])
            with open("dosya.json","w",encoding="utf-8") as index:
                json.dump(bilgi,index,indent=4)
                print("yeni kullanici bilgiler:",bilgi)
        elif(x==0):
            break
        else:
            print("Geçerli bir değer giriniz.")



