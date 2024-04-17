class LayangLayang:
    def __init__(self, d1, d2, sisi1, sisi2):
        self.__d1 = max(1, d1)  # Memastikan d1 tidak <= 0
        self.__d2 = max(1, d2)  # Memastikan d2 tidak <= 0
        self.__sisi1 = max(1, sisi1)  # Sisi yang sama panjang pertama
        self.__sisi2 = max(1, sisi2)  # Sisi yang sama panjang kedua

    def getDiagonals(self):
        return self.__d1, self.__d2

    def getSides(self):
        return self.__sisi1, self.__sisi2

    def luas(self):
        return 0.5 * self.__d1 * self.__d2
    
    def keliling(self):
        return 2 * (self.__sisi1 + self.__sisi2)

while True:
    try:
        d1 = int(input("Masukkan panjang diagonal 1: "))
        d2 = int(input("Masukkan panjang diagonal 2: "))
        sisi1 = int(input("Masukkan panjang sisi 1: "))
        sisi2 = int(input("Masukkan panjang sisi 2: "))
        layangLayang = LayangLayang(d1, d2, sisi1, sisi2)
        assert d1 > 0 and d2 > 0 and sisi1 > 0 and sisi2 > 0
        break
    except ValueError:
        print("Masukkan hanya angka saja!")
    except AssertionError:
        print("Nilai diagonal dan sisi tidak boleh nol atau negatif")

print("Diagonal: ", layangLayang.getDiagonals())
print("Sisi: ", layangLayang.getSides())
print("Luas Layang-Layang: ", layangLayang.luas())
print("Keliling Layang-Layang: ", layangLayang.keliling())
