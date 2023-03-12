class OgrenciSistemi:
    def __init__(self):
        self.ogrenciler = []

    def ogrenci_ekle(self, isim, soyisim):
        numara = len(self.ogrenciler) + 1  # öğrenci numarası, öğrenci listesinin uzunluğu + 1 olacak
        ogrenci = {"numara": numara, "isim": isim, "soyisim": soyisim}
        self.ogrenciler.append(ogrenci)

    def ogrenci_sil(self, numara):
        for ogrenci in self.ogrenciler:
            if ogrenci['numara'] == numara:
                self.ogrenciler.remove(ogrenci)

    def ogrenci_listele(self):
        for ogrenci in self.ogrenciler:
            print(f"{ogrenci['numara']}: {ogrenci['isim']} {ogrenci['soyisim']}")
            print("*********************************************************")

def main():
    ogrenci_sistemi = OgrenciSistemi()
    while True:
        print("1- Öğrenci Ekle")
        print("2- Öğrenci Sil")
        print("3- Öğrenci Listele")
        print("4- Çıkış")
        secim = int(input("Seçiminiz: "))
        if secim == 1:
            isim = input("Öğrencinin adı: ")
            soyisim = input("Öğrencinin soyadı: ")
            ogrenci_sistemi.ogrenci_ekle(isim, soyisim)
        elif secim == 2:
            numara = int(input("Silmek istediğiniz öğrencinin numarasını girin: "))
            ogrenci_sistemi.ogrenci_sil(numara)
        elif secim == 3:
            ogrenci_sistemi.ogrenci_listele()
        elif secim == 4:
            break
        else:
            print("Hatalı seçim. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()


