class SistemPOS:
    # Memberi variabel-variabel public yang dapat digunakan untuk program secara kesuluruhan
    # DESCRIPTION FOR DICTIONARY --> { key : [[jumlah stok barang], [harga barang]]}
    toko = "Warung Makmur Jaya "
    __jenisBarang = { "Nutella" : 20000, "Ovaltine" : 10000, "Milo" : 8000 }

    def __init__(self, nama, saldo, bank) -> None:
        self.nama = nama
        self.saldo = saldo
        self.__kartuBank = bank #parameter bank memiliki variabel yang bersifat privat dimana hal ini hanya dapat diakses melalui kelas ini sendiri 

    def melihat_harga(self):
        #Atribut
        pilihan = input("Ketik cemilan yang ingin dibeli = (Nutella / Ovaltine / Milo)")
        if(pilihan in SistemPOS.__jenisBarang):
            print(f"Cemilan yang anda ingin berhasil ditemukan, toko kami menjualnya sebesar Rp {SistemPOS.__jenisBarang[pilihan]} per pieces")
        else :
            print("Cemilan yang anda sedang cari tidak tersedia untuk saat ini! Kami mohon!")

    def membeli_barang(self):
        #Metode ini benar-benar membikin om Sam minder dan tidak tahu mau bagaimana lagi
        pilihan = input("Ketik cemilan yang ingin dibeli = (Nutella / Ovaltine / Milo)")
        if(pilihan in SistemPOS.__jenisBarang): #memeriksa apabilan cemilan yang dipilih terdapat dalam database warung 
            self.saldo -= SistemPOS.__jenisBarang[pilihan] #apabila uang yang dimiliki oleh pengguna cukup untuk membayar semua itu, dia butuh rf
            print(f"Cemilan yang anda ingin berhasil dibayar, saldo anda sekarang = {self.saldo}")
            siap nat 
            
        else :
            print("Cemilan yang anda sedang cari tidak tersedia untuk saat ini! Kami mohon!")

    def pindah_bank(self, bank):
        self.__kartuBank = bank #metode ini berguna untuk mengedit kartu bank apabila pengguna/pelanggan ingin mengubah password

pelanggan1 = SistemPOS("Toby Manurung", 1000000, "Bank Mandiri")

print(f"Selamat datang Pak/Bu {pelanggan1.nama}. Senang berbisnis dengan anda! ")
print(f"Wow! Kami baru pertama kali melayani seseorang pelanggan toko yang memakai kartu bank {pelanggan1.__kartuBank}") 
#Sistem perangkat lunak sengaja mendapatkan error supaya dapat mendemonstrasikan bahwa atribut __kartuBank hanya dapat diakses oleh orang yang terdekat

pelanggan1.melihat_harga()
pelanggan1.membeli_barang()



    