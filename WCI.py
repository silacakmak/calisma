#rüzgar soğuma endeksi hesaplama uygulaması
import math
t,v=map(float,input("hava sıcaklığını (derece üzerinden) ve rüzgar hızını (km/saat) belirtiniz  \n").split())
if(t>-45 and v>5):
    wci=35.74+ (0.6215*t) - (35.75 * pow(v,0.16))+ ((0.4275*t)*pow(v,0.16))
    print("girmiş olduğunuz değerlere göre rüzgar soğuma endeksi:",wci)
else:
    print("girmiş olduğunuz değerlere göre rüzgar soğuma endeksi hesaplanamaz,\n"
     " sıcaklık-45 dereceden büyük ve rüzgar hızı 5km/saatten büyük olmalıdır.Geçerli bir değer giriniz.")



