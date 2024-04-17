class BelahKetupat:
    def __init__(self, sisi, d1, d2):
        self.__sisi = max(1, sisi)  # Memastikan sisi tidak <= 0
        self.__d1 = max(1, d1)  # Memastikan d1 tidak <= 0
        self.__d2 = max(1, d2)  # Memastikan d2 tidak <= 0

    def getSisi(self):
        return self.__sisi
    
    def getDiagonal(self):
        return (self.__d1, self.__d2)

    def luas(self):
        return 0.5 * self.__d1 * self.__d2
    
    def keliling(self):
        return 4 * self.__sisi

while True:
    try:
        sisi = int(input("Masukkan panjang sisi: "))
        d1 = int(input("Masukkan panjang diagonal 1: "))
        d2 = int(input("Masukkan panjang diagonal 2: "))
        belahKetupat = BelahKetupat(sisi, d1, d2)
        assert sisi > 0 and d1 > 0 and d2 > 0
        break
    except ValueError:
        print("Masukkan hanya angka saja!")
    except AssertionError:
        print("Nilai sisi dan diagonal tidak boleh nol atau negatif")

print("Sisi: ", belahKetupat.getSisi())
print("Diagonal: ", belahKetupat.getDiagonal())
print("Luas Belah Ketupat: ", belahKetupat.luas())
print("Keliling Belah Ketupat: ", belahKetupat.keliling())
