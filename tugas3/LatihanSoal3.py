#TugasLatihanNo2
class AkunBank():
    list_pelanggan = []

    def __init__(self, no_pelanggan, nama_pelanggan, jumlah_saldo):
        self.__no_pelanggan = no_pelanggan
        self.__nama_pelanggan = nama_pelanggan
        self.__jumlah_saldo = jumlah_saldo
        self.list_pelanggan.append(self.__no_pelanggan)
    
    def menu_utama():
        print("Selamat datang di Bank Jago \n Halo formating needed, ingin melakukan apa? \n")
        print("1. Lihat saldo")
        print("2. Tarik tunai")
        print("3. Transfer saldo")
        print("4. Keluar")

        #opsi 5 tuh gacha dapat uang kaget

        input_user = int(input("Masukkan nomor input: "))
        match input_user:
            case 1:
                self.lihat_saldo()
            case 2:
                self.tarik_tunai()
            case 3:
                self.transfer()
            case 4:
                pass
            case default:
                print ("Inputkan suatu bilangan masbro, dan antara 1-4")

    def list_pelanggan():
        pass

    def lihat_saldo():
        print(f'{self.__nama_pelanggan} memiliki saldo Rp {self.__jumlah_saldo}')

    def tarik_tunai():
        __saldo = int(input("Masukkan jumlah nominal yang ingin ditarik: "))
        if(self.__jumlah_saldo >= __saldo):
            print("Saldo berhasil ditarik!")
            self.__jumlah_saldo -= __saldo
        else:
            print("Nominal saldo yang Anda punya tidak cukup! ")
            self.tarik_tunai()

    def transfer():
        __jmlh_transfer = int(input("Masukkan nominal yang ingin ditransfer: "))
        __rek_tujuan = int(input("Masukkan no rekening tujuan: "))
        


Akun1 = AkunBank(1234, "Toby Manurung", 5000000)
Akun2 = AkunBank(1234, "Daniel Hutabarat", 4000000)
Akun2 = AkunBank(1234, "Yesi Tampubolon", 6000000)
