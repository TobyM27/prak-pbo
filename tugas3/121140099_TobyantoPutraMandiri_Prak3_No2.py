#TugasLatihanNo2
import random

class AkunBank:
    list_pelanggan_ID = []
    list_pelanggan_nama = []
    list_pelanggan_Saldo = []
    l_limit = 1
    u_limit = 100

    def __init__(self, no_pelanggan, nama_pelanggan, jumlah_saldo) -> None:
        self.__no_pelanggan = no_pelanggan
        self.__nama_pelanggan = nama_pelanggan
        self.__jumlah_saldo = jumlah_saldo
        self.list_pelanggan_ID.append(self.__no_pelanggan)
        self.list_pelanggan_nama.append(self.__nama_pelanggan)
        self.list_pelanggan_Saldo.append(self.__jumlah_saldo)

    def teks_dekor(self):
        print("-----------------------------------\n")
        AkunBank.menu_utama(self)
    
    def menu_utama(self):
        print("Selamat datang di Bank JayaJayaJaya \n Halo, apa yang anda ingin lakukan sekarang?\n1. Lihat saldo\n2. Tarik tunai\n3. Transfer saldo\n4. Gacha dapat uang kaget! promo spesial buat KAMU!\n5. Keluar")
        #opsi 5 tuh gacha dapat uang kaget

        input_user = int(input("Masukkan nomor input: "))
        if input_user == 1:
            AkunBank.lihat_saldo(self)
        elif input_user == 2:
            AkunBank.tarik_tunai(self)
        elif input_user == 3:
            AkunBank.transfer(self)
        elif input_user == 4:
            AkunBank.gacha(self)
        elif input_user == 5:
            print("kami berterima kasih atas pilihan anda untuk menggunakan bank JayaJayaJaya! ")
            exit()
        else:
            print("Mohon hanya memberi input yang telah kami tetapkan! (yaitu 1-5)")

    def lihat_saldo(self):
        print(f"{self.__nama_pelanggan} memiliki saldo Rp {self.__jumlah_saldo}")
        AkunBank.teks_dekor(self)

    def tarik_tunai(self):
        __saldo = int(input("Masukkan jumlah nominal yang ingin ditarik: "))
        if(self.__jumlah_saldo >= __saldo):
            print("Saldo berhasil ditarik!")
            self.__jumlah_saldo -= __saldo
            print(f"Setelah penarikan uang, saldo yang tersisa dalam rekening anda sebesar : {self.__jumlah_saldo}")
            AkunBank.teks_dekor(self)
        else:
            print("Nominal saldo yang Anda punya tidak cukup! ")
            self.tarik_tunai(self)
            AkunBank.teks_dekor(self)

    def transfer(self):
        __nilai_transfer = int(input("Masukkan nominal yang ingin ditransfer: "))
        if __nilai_transfer <= self.__jumlah_saldo:
            __rek_tujuan = int(input("Masukkan no rekening tujuan: "))
            if __rek_tujuan in self.list_pelanggan_ID:
                __validasi = (input(f"Apakah anda yakin tujuan rekening yang anda ketik benar? (Y/N) \n"))
                if __validasi == ("Y" or 'y'):
                    print(f"Selamat, Proses transfer sejumlah Rp.{__nilai_transfer} ke {self.list_pelanggan_ID} sukses! ")
                    AkunBank.teks_dekor(self)
                elif __validasi == ("N" or "n"):
                    print("Baiklah, silahkan balik ke menu utama untuk mengakses layanan transfer atau lainnya! ")
                    AkunBank.teks_dekor(self)
            else:
                print("Mohon maaf, no pelanggan yang anda input tidak terdapat dalam database bank kami!")
                AkunBank.teks_dekor(self)
        else:
            print(f"Mohon maaf, namun jumlah saldo yang anda miliki dalam rekening ini tidak cukup untuk melakukan proses transaksi! ")
            AkunBank.teks_dekor(self)

    def gacha(self):
        __validasi_gacha = (input(f"Apakah anda siap untuk melakukan gacha uang kaget? (Y/N)\n"))
        if __validasi_gacha == ("Y" or 'y'):
            __hasil_gacha = random.randint(AkunBank.l_limit, AkunBank.u_limit)
            if(__hasil_gacha == 50 or 51):
                print("Selamat anda telah memenangkan gacha. Rp50.000 akan segera ditambahkan ke rekening anda")
                self.__jumlah_saldo += 50000
            else :
                print("Mohon maaf, sepertinya hoki anda sedang tidak baik-baik saja hari ini! ")
                AkunBank.teks_dekor(self)
        elif __validasi_gacha == ("N" or "n"):
            print("Baiklah, silahkan balik ke menu utama untuk mengakses layanan Bank JayaJayaJaya ")
            AkunBank.teks_dekor(self)

Akun1 = AkunBank(1234, "Toby Manurung", 5000000)
Akun2 = AkunBank(3456, "Daniel Hutabarat", 4000000)
Akun2 = AkunBank(1556, "Yesi Tampubolon", 6000000)

Akun1.menu_utama()