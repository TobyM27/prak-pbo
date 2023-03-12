#TugasLatihanNo2
import random

class AkunBank():
    list_pelanggan_ID = []
    list_pelanggan_nama = []
    list_pelanggan_Saldo = []
    l_limit = 1
    u_limit = 100

    def __init__(self, no_pelanggan, nama_pelanggan, jumlah_saldo):
        self.__no_pelanggan = no_pelanggan
        self.__nama_pelanggan = nama_pelanggan
        self.__jumlah_saldo = jumlah_saldo
        self.list_pelanggan_ID.append(self.__no_pelanggan)
        self.list_pelanggan_nama.append(self.__nama_pelanggan)
        self.list_pelanggan_Saldo.append(self.__jumlah_saldo)
    
    def menu_utama():
        print("Selamat datang di Bank Jago \n Halo formating needed, ingin melakukan apa?\n1. Lihat saldo\n2. Tarik tunai\n3. Transfer saldo\n4. Gacha dapat uang kaget! promo spesial buat KAMU!\n5. Keluar")
        #opsi 5 tuh gacha dapat uang kaget

        input_user = int(input("Masukkan nomor input: "))
        if input_user == 1:
            AkunBank.lihat_saldo()
        elif input_user == 2:
            AkunBank.tarik_tunai
        elif input_user == 3:
            AkunBank.transfer
        elif input_user == 4:
            AkunBank.gacha
        elif input_user == 5:
            print("kami berterima kasih atas pilihan anda untuk menggunakan bank JayaJayaJaya! ")
            exit()
        else:
            print("Mohon hanya memberi input yang telah kami tetapkan! (yaitu 1-5)")

    def lihat_saldo():
        print(f"{self.__nama_pelanggan} memiliki saldo Rp {self.__jumlah_saldo}")
        AkunBank.menu_utama(self)

    def tarik_tunai():
        __saldo = int(input("Masukkan jumlah nominal yang ingin ditarik: "))
        if(self.__jumlah_saldo >= __saldo):
            print("Saldo berhasil ditarik!")
            self.__jumlah_saldo -= __saldo
        else:
            print("Nominal saldo yang Anda punya tidak cukup! ")
            self.tarik_tunai()

    def transfer():
        __nilai_transfer = int(input("Masukkan nominal yang ingin ditransfer: "))
        if __nilai_transfer <= self.__jumlah_saldo:
            __rek_tujuan = int(input("Masukkan no rekening tujuan: "))
            if __rek_tujuan in self.list_pelanggan_ID:
                __validasi = (input(f"Apakah anda yakin tujuan rekening yang anda ketik benar? (Y/N) \n"))
                if __validasi == ("Y" or 'y'):
                    print(f"Selamat, Proses transfer sejumlah Rp.{__nilai_transfer} ke {self.self.list_pelanggan_ID} sukses! ")
                    AkunBank.menu_utama(self)
                elif __validasi == ("N" or "n"):
                    print("Baiklah, silahkan balik ke menu utama untuk mengakses layanan transfer atau lainnya! ")
                    AkunBank.menu_utama(self)
            else:
                print("Mohon maaf, no pelanggan yang anda input tidak terdapat dalam database bank kami!")
                AkunBank.menu_utama(self)
        else:
            print(f"Mohon maaf, namun jumlah saldo yang anda miliki dalam rekening ini tidak cukup untuk melakukan proses transaksi! ")
            AkunBank.menu_utama(self)

    def gacha():
        print("Apakah anda siap untuk melakukan gacha uang kaget? (Y/N)")
        __validasi_gacha = (input(f"Apakah anda yakin tujuan rekening yang anda ketik benar? (Y/N) \n"))
        if __validasi_gacha == ("Y" or 'y'):
            __hasil_gacha = random.randint(AkunBank.l_limit, AkunBank.u_limit)
            if(__hasil_gacha == 50 or 51):
                print("Selamat anda telah memenangkan gacha. Rp50.000 akan segera ditambahkan ke rekening anda")
                self.__jumlah_saldo += 50000
        elif __validasi_gacha == ("N" or "n"):
            print("Baiklah, silahkan balik ke menu utama untuk mengakses layanan Bank JayaJayaJaya ")
            AkunBank.menu_utama(self)

        __hasil_gacha = random.randint(AkunBank.l_limit, AkunBank.u_limit)


Akun1 = AkunBank(1234, "Toby Manurung", 5000000)
Akun2 = AkunBank(1234, "Daniel Hutabarat", 4000000)
Akun2 = AkunBank(1234, "Yesi Tampubolon", 6000000)
