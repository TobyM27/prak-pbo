class SistemPOS:
    # DESCRIPTION FOR DICTIONARY --> { key : [[jumlah stok barang], [harga barang]]}
    toko = "Warung Makmur Jaya "
    __jenisBarang = { "Nutella" : 20000, "Ovaltine" : 10000, "Milo" : 8000 }

    def __init__(self, nama, saldo, bank) -> None:
        self.nama = nama
        self.saldo = saldo
        self.__kartuBank = bank 

    def melihat_harga(self):
        #Atribut
        pilihan = input("Ketik cemilan yang ingin dibeli = (Nutella / Ovaltine / Milo)")
        if(pilihan in SistemPOS.__jenisBarang):
            print(f"Cemilan yang anda ingin berhasil ditemukan, toko kami menjualnya sebesar Rp {SistemPOS.__jenisBarang[pilihan]} per pieces")
        else :
            print("Cemilan yang anda sedang cari tidak tersedia untuk saat ini! Kami mohon!")

    def membeli_barang(self):
        #Atribut
        pilihan = input("Ketik cemilan yang ingin dibeli = (Nutella / Ovaltine / Milo)")
        if(pilihan in SistemPOS.__jenisBarang):
            #jumlah_produk = int(input("Seberapa banyak yang anda ingin beli dari produk ini? "))
            self.saldo -= SistemPOS.__jenisBarang[pilihan]
            print(f"Cemilan yang anda ingin berhasil dibayar, saldo anda sekarang = {self.saldo}")
        else :
            print("Cemilan yang anda sedang cari tidak tersedia untuk saat ini! Kami mohon!")

    def pindah_bank(self, bank):
        self.__kartuBank = bank

    