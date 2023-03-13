class SistemPOS:
    # Memberi variabel-variabel public yang dapat digunakan untuk program secara kesuluruhan
    # DESCRIPTION FOR DICTIONARY --> { key : [[jumlah stok barang], [harga barang]]}
    toko = "Warung Makmur Jaya "
    __jenisBarang = { "Nutella" : 20000, "Ovaltine" : 10000, "Milo" : 8000 }

    def __init__(self, nama, saldo, bank) -> None:
        self.nama = nama
        self.saldo = saldo
        #parameter bank memiliki variabel yang bersifat privat dimana hal ini hanya dapat diakses melalui kelas ini sendiri 
        self.__kartuBank = bank 

    def print_KartuBank(self):
        #Atribut hanya bisa diakses oleh metode kelas. Apabila atribut ini dipanggil di main program, maka program akan mengalami error
        print(f"Kartu bank yang sedang anda gunakan adalah kartu {self.__kartuBank}") 

    def melihat_harga(self):
        #Metode ini berfungsi untuk melihat harga dari barang-barang yang terdapat dalam dictionary kelas SistemPOS
        pilihan = input("Ketik cemilan yang ingin dibeli = (Nutella / Ovaltine / Milo) ")
        if(pilihan in SistemPOS.__jenisBarang):
            print(f"Cemilan yang anda ingin berhasil ditemukan, toko kami menjualnya sebesar Rp {SistemPOS.__jenisBarang[pilihan]} per pieces")
        else :
            print("Cemilan yang anda sedang cari tidak tersedia untuk saat ini! Kami mohon!")

    def membeli_barang(self):
        #Metode ini berfungsi untuk membeli makanan dari toko warung makmur jaya
        pilihan = input("Ketik cemilan yang ingin dibeli = (Nutella / Ovaltine / Milo) ")
        if(pilihan in SistemPOS.__jenisBarang): #memeriksa apabilan cemilan yang dipilih terdapat dalam database warung 
            self.saldo -= SistemPOS.__jenisBarang[pilihan] #apabila uang yang dimiliki oleh pengguna cukup untuk membayar semua itu, dia butuh rf
            print(f"Cemilan yang anda ingin berhasil dibayar, saldo anda sekarang = {self.saldo}")
        else :
            print("Cemilan yang anda sedang cari tidak tersedia untuk saat ini! Kami mohon maaf!")

    def pindah_bank(self, bank):
        self.__kartuBank = bank #metode ini berguna untuk mengedit kartu bank apabila pengguna/pelanggan ingin mengubah password

pelanggan1 = SistemPOS("Toby Manurung", 1000000, "Bank Mandiri")

print(f"Selamat datang Pak/Bu {pelanggan1.nama}. Senang berbisnis dengan anda! ")
pelanggan1.print_KartuBank() 

pelanggan1.melihat_harga()
pelanggan1.membeli_barang()



    