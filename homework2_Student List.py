

ogrenciList = ["Ali Can","Ayse Yilmaz","Mustafa Kod","Hakan Alp","Fatma Sari"]


def ogrenciEkle():   # Tek bir ögrenci kaydetmek icin. Aldığı isim soy isim ile listeye öğrenci ekleyen
    adSoyad = input("Kayit olacak Ogrenci giriniz : ")
    ogrenciList.append(adSoyad)
    print("Isleminiz Basari Ile Gerceklestirildi...")


def ogrenciSil(): # Aldığı isim soy isim ile eşleşen değeri listeden kaldıran
    adSoyad = input("Silinecek ögrenci ad soyad Girin : ")
    ogrenciList.remove(adSoyad)
    print("Isleminiz Basari Ile Gerceklestirildi...")
    

def cokluOgrenciEkle():  # Listeye birden fazla öğrenci eklemeyi mümkün kılan
    while True:
        print("1 - ögrenci Listesi Ekle\n2 - cikis yap")
        secim = input("Bir Islem Seciniz : ")
        if secim == "2":
            break
        elif secim == "1":
            liste=[]
            while True:
                adSoyad = input("Kaydedilecek ögrenci girin : \nCikis yapmak icin q harfine basin : ")
                if adSoyad == "q":
                    break
                liste.append(adSoyad)
            ogrenciList.extend(liste)
        else:
            print("Gecersiz islem")
    print("Isleminiz Basari Ile Gerceklestirildi...")


def listeYazdir():     # Listedeki tüm öğrencileri tek tek ekrana yazdıran
    print("\n")
    for i in ogrenciList:
        print(i,end=" - ")
    print("\n")



def ogrenciNoBul():  # Öğrencinin listedeki index numarası öğrenci numarası olarak kabul edildiğini düşünerek öğrencinin numarasını öğrenmeyi mümkün kılan
    adSoyad = input("Numarasini ögrenmek istediginiz ögrenciyi giriniz : ")

    if adSoyad in ogrenciList:
        indeks = ogrenciList.index(adSoyad)
        print("\n")
        print(f"{adSoyad} isimli ögrencinin numarasi : {indeks}' dir...")
    else:
        print("ogrenci listede bulunamadi")
    


def cokluOgrenciSil(): # Listeden birden fazla öğrenci silmeyi mümkün kılan (döngü kullanınız)
    while True:
        print("1 - Silinecek ögrenci giriniz\n2 - cikis yap")
        secim = input("Bir Islem Seciniz : ")
        if secim == "2":
            break
        elif secim == "1":
            liste=[]
            while True:
                adSoyad = input("Silinecek ögrencileri girin : \nCikis yapmak icin q harfine basin : ")
                if adSoyad == "q":
                    break
                liste.append(adSoyad)
            for i in liste:
                ogrenciList.remove(i)
        else:
            print("Gecersiz islem")
    print("Isleminiz Basari Ile Gerceklestirildi...")


def mainfunc():  # menü icin main fonksiyon
    while True:
        print("\n") # Menüler arasinda bosluk birakarak karisiklik olmasin.
        
        print("*************  Ögrenci Islemleri Menüsü...!   ****************")
        print("1 - Ögrenci Ekle\n2 - Ögrenci Sil\n3 - Coklu Ögrenci Ekle\n4 - Ögrenci Listesi Yazdir\n5 - Ögrenci No Bul\n6 - Coklu Ögrenci Sil\n7 - Cikis Yap")

        secim = input("Lütfen bir islem seciniz :  ")
        if secim == "1":
            ogrenciEkle()
        elif secim == "2":
            ogrenciSil()
        elif secim == "3":
            cokluOgrenciEkle()
        elif secim == "4":
            listeYazdir()
        elif secim == "5":
            ogrenciNoBul()
        elif secim == "6":
            cokluOgrenciSil()
        elif secim == "7":
            break
        else:
            print("Lütfen menüden gecerli bir secim yapiniz...!")



mainfunc()


