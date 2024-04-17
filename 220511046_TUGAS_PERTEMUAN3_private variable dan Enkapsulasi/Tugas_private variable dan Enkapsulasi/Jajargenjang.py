class JajarGenjang:
    def __init__(self, alas, tinggi, sisi_miring):
        self.__alas = max(1, alas)  # Memastikan alas tidak <= 0
        self.__tinggi = max(1, tinggi)  # Memastikan tinggi tidak <= 0
        self.__sisi_miring = max(1, sisi_miring)  # Memastikan sisi miring tidak <= 0

    def getAlas(self):
        return self.__alas
    
    def getTinggi(self):
        return self.__tinggi
    
    def getSisiMiring(self):
        return self.__sisi_miring

    def luas(self):
        return self.__alas * self.__tinggi
    
    def keliling(self):
        return 2 * (self.__alas + self.__sisi_miring)

while True:
    try:
        alas = int(input("Masukkan panjang alas: "))
        tinggi = int(input("Masukkan tinggi: "))
        sisi_miring = int(input("Masukkan panjang sisi miring: "))
        jajarGenjang = JajarGenjang(alas, tinggi, sisi_miring)
        assert alas > 0 and tinggi > 0 and sisi_miring > 0
        break
    except ValueError:
        print("Masukkan hanya angka saja!")
    except AssertionError:
        print("Nilai alas, tinggi, dan sisi miring tidak boleh nol atau negatif")

print("Alas: ", jajarGenjang.getAlas())
print("Tinggi: ", jajarGenjang.getTinggi())
print("Sisi Miring: ", jajarGenjang.getSisiMiring())
print("Luas Jajar Genjang: ", jajarGenjang.luas())
print("Keliling Jajar Genjang: ", jajarGenjang.keliling())
