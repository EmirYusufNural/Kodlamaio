class OgrenciKayitSistemi:
    def __init__(self):
        self.ogrenciler = []

    def ogrenci_ekle(self, isim, soyisim):
        yeni_ogrenci = {"isim": isim, "soyisim": soyisim}
        # Aynı isim ve soyisme sahip öğrencileri listeden çıkar
        self.ogrenciler = [ogrenci for ogrenci in self.ogrenciler if ogrenci["isim"] != isim or ogrenci["soyisim"] != soyisim]

        # Yeni öğrenci, öğrenci listesinde son öğrenciyle aynı değilse listeye ekle
        if not self.ogrenciler or self.ogrenciler[-1] != yeni_ogrenci:
            self.ogrenciler.append(yeni_ogrenci)

        # Öğrenci numaralarını index numaraları olarak belirle
        for i in range(len(self.ogrenciler)):
            self.ogrenciler[i]["numara"] = i

    def ogrencileri_listele(self):
        for ogrenci in self.ogrenciler:
            print(f"{ogrenci['numara']}: {ogrenci['isim']} {ogrenci['soyisim']}")

    def ogrenci_sil(self, numaralar):
        # Numaraları sırala ve sondan başlayarak silmeye başla
        for numara in sorted(numaralar, reverse=True):
            if numara < len(self.ogrenciler):
                del self.ogrenciler[numara]
                # Numaraları tekrar belirle
                for i in range(len(self.ogrenciler)):
                    self.ogrenciler[i]["numara"] = i


def main():
    # OgrenciKayitSistemi nesnesi oluştur
    kayit_sistemi = OgrenciKayitSistemi()

    # Öğrenci ekle
    kayit_sistemi.ogrenci_ekle("Ahmet", "Yilmaz")
    kayit_sistemi.ogrenci_ekle("Ayse", "Yilmaz")
    kayit_sistemi.ogrenci_ekle("Ali", "Demir")
    kayit_sistemi.ogrenci_ekle("Emir","Yusuf")
    # Öğrencileri listele
    kayit_sistemi.ogrencileri_listele()

    # Öğrenci sil
    kayit_sistemi.ogrenci_sil([3,1,2,0])

    # Değişiklikleri kaydedip, öğrencileri tekrar listele
    kayit_sistemi.ogrencileri_listele()


if __name__ == '__main__':
    main()

