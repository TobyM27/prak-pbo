class Rumah:
    def __init__(self,biaya_hidup, jumlah_penghuni) -> None:
        self.biaya_hidup = biaya_hidup
        self.jumlah_penghuni = jumlah_penghuni

    def hitung_pengeluaran(self):
        hasil_pengeluaran = self.biaya_hidup * self.jumlah_penghuni
        print(f"pengeluaran anda sebesar {hasil_pengeluaran} !")

class Toko:
    def __init__(self, pendapatan, jumlah_hari) -> None:
        self.__pendapatan = pendapatan
        self.__jumlah_hari = jumlah_hari

    def hitung_pendapatan(self):
        hasil_pendapatan = self.__pendapatan * self.__jumlah_hari
        print(hasil_pendapatan)

class Ruko(Rumah, Toko):
    def __init__(self, biaya_hidup, jumlah_penghuni, pendapatan, jumlah_hari) -> None:
        super().__init__(biaya_hidup, jumlah_penghuni)
        super().__init__(pendapatan, jumlah_hari)

    def hitung_laba_bersih(self):
        hasil_laba = (Toko.hitung_pendapatan(self)) - (Rumah.hitung_pengeluaran(self))
        print(hasil_laba)

Herman = Ruko(biaya_hidup=2000000, jumlah_penghuni=5, pendapatan=10000000, jumlah_hari=31)
print(Herman.hitung_pengeluaran())
