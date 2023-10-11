import json

while True:
    takim = input("Takımınızı giriniz: ")
    ms_input = input("Toplam kaç maç oynandı giriniz: ")

    try:
        ms = int(ms_input)
    except ValueError:
        print("Geçerli bir tam sayı giriniz.")
        continue

    g_input = input("Takımın galibiyet sayısı: ")

    try:
        g = int(g_input)
        if g < 0 or g > ms:
            print("Geçerli bir galibiyet sayısı giriniz.")
            continue
    except ValueError:
        print("Geçerli bir tam sayı giriniz.")
        continue

    m_input = input("Takımın mağlubiyet sayısı: ")

    try:
        m = int(m_input)
        if m < 0 or m > ms - g:
            print("Geçerli bir mağlubiyet sayısı giriniz.")
            continue
    except ValueError:
        print("Geçerli bir tam sayı giriniz.")
        continue

    b_input = input("Takımın berabere kaldığı maç sayısı:")

    try:
        b = int(b_input)
        if b < 0 or b > ms - g - m:
            print("Geçerli bir berabere sayısı giriniz.")
            continue
    except ValueError:
        print("Geçerli bir tam sayı giriniz.")
        continue

    tp = (g * 3) + (m * 0) + b
    sozluk={"galibiyet":g,"mağlubiyet":m,"berabere":b,"toplam puan":tp}
   # bilgi=json.loads(sozluk)

    with open("takım.json","w",encoding="utf-8") as index:
        json.dump(sozluk,index)
    print("Takımın toplam puanı:", tp)
    break