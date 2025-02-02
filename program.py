# GLOBAL DEĞİŞKENLER
name = None
note = None
ort = None

#MENÜ
def menu():

    global name, note, ort

    print("----------HOSGELDİNİZ----------")
    print(" ")
    print("Lütfen Seçim Yapınız:")
    print("\t1-Not Gir")
    print("\t2-Ortalama Göster")
    print("\t3-Notları Kaydet")
    print("\t4-Kaydı Oku")
    print("\t5-Çıkış")
    print(" ")
    print("-------------------------------\n\n")
    c = int(input("Seçim: "))
    
    #HATA LOOP
    if(not(c>=1 and c<=5)):
        print("HATALI GİRİŞ, LÜTFEN TEKRAR DENEYİN \n\n")
        return 1
    
    #SEÇİM SONUÇLARI
    if(c==1):
        dic = score()
        name = dic["name"]
        note = dic["score"]
        print("\n\nGirdi İşlemi Tamamlandı!")
        print("Devam etmek için herhangi bir duşa basın!")
        k=input()
        return 1
    elif(c==2):
        ort = ortalama(note)
        print("Öğrenci Ortlaması=",ort)
        print("Devam etmek için herhangi bir duşa basın!")
        k=input()
        return 1
    elif(c==3):
        kaydet(name,ort)
        print("\nİşlem tamamlandı. Devam etmek için herhangi bir duşa basın!")
        k=input()
        return 1
    elif(c==4):
        oku()
        print("\n\nDevam etmek için herhangi bir duşa basın!")
        k=input()
        return 1
    elif(c==5):
        print("-----------------İYİ GÜNLER DİLERİZ-----------------")
        return 0

    

#SCORE FONKSİYONU
def score():
    name = input("Öğrenci Adını Giriniz: ")
    score = int(input("Lütfen Öğrenci Puanını Giriniz: "))
    
    #HATA LOOP
    if(not(score<=100 and score>=0)):
        print("HATALI GİRİŞ, LÜTFEN TEKRAR DENEYİN \n\n")
        return score()
    
    return {"name":name,"score":score}



#ORTALAMA FONKSİYONU
def ortalama(note):
    if note >= 90 and note <= 100:
        ort = "AA"
    elif note >= 85 and note <= 89:
        ort = "BA"
    elif note >= 80 and note <= 84:
        ort = "BB"
    elif note >= 75 and note <= 79:
        ort = "CB"
    elif note >= 70 and note <= 74:
        ort = "CC"
    elif note >= 65 and note <= 69:
        ort = "DC"
    elif note >= 60 and note <= 64:
        ort = "DD"
    elif note >= 50 and note <= 59:
        ort = "FD"
    else:
        ort = "FF"
    return ort



#DOSYAYA YAZDIRMA FONKSİYONU
def kaydet(name,ort):
    with open("file.txt","a",encoding="utf-8") as f:
            f.write(f"{name}: {ort}\n")
            print("Kaydetme İşlemi Tamamlandı!")



#DOSYAYI OKUMA FONKSİYONU
def oku():
    with open("file.txt","r",encoding="utf-8") as f:
            print(f.read())



#PROGRAM SÜRDÜRME DÖNGÜSÜ
while True:
    secim = menu()
    if secim == 0:
        break
