from abc import ABC,abstractmethod

class AkunBank(ABC):
    def __init__(self,nama,tahun,saldo):
        self.nama=nama
        self.tahun_daftar=tahun
        self.saldo_pelanggan=saldo
        
    def lihat_saldo(self):
        print(f"Nama Akun : {self.nama}\nJumlah Saldo : Rp {self.saldo_pelanggan}")
        
    @abstractmethod
    def transfer_saldo(self):
        pass
    
    @abstractmethod
    def suku_bunga(self):
        pass
    
class AkunGold(AkunBank):
    def __init__(self,nama,tahun,saldo):
        super().__init__(nama,tahun,saldo)
        
    def transfer_saldo(self):
        transfer=int(input("Masukkan Nominal Transfer : "))
        usia_akun=2023-self.tahun_daftar
        if self.saldo_pelanggan>=transfer:
            if transfer > 100000:
                if usia_akun >= 3:
                    self.saldo_pelanggan-=transfer
                    print("Berhasil transfer, biaya administrasi gratis")
                elif usia_akun < 3:
                    self.saldo_pelanggan-=transfer+2000
                    print("Berhasil transfer, biaya administrasi Rp 2000")
            
            else:
                self.saldo_pelanggan-=transfer
                print("Berhasil transfer, biaya administrasi gratis")
                
    def suku_bunga(self):
        usia_akun=2023-self.tahun_daftar
        
        if self.saldo_pelanggan>=1000000000:
            if usia_akun>=3:
                bungabulanan=self.saldo_pelanggan*0.01
                print(f"Bunga bulanan akun sebesar Rp {bungabulanan}")
            elif usia_akun<3:
                bungabulanan=self.saldo_pelanggan*0.02
                print(f"Bunga bulanan akun sebesar Rp {bungabulanan}")
        else:
            bungabulanan=self.saldo_pelanggan*0.03
            print(f"Bunga bulanan akun sebesar Rp {bungabulanan}")
            
class AkunSilver(AkunBank):
    def __init__(self,nama,tahun,saldo):
        super().__init__(nama,tahun,saldo)
        
    def transfer_saldo(self):
        transfer=int(input("Masukkan Nominal Transfer : "))
        usia_akun=2023-self.tahun_daftar
        if self.saldo_pelanggan>=transfer:
            if transfer > 100000:
                if usia_akun >= 3:
                    self.saldo_pelanggan-=transfer+2000
                    print("Berhasil transfer, biaya administrasi Rp 2000")
                elif usia_akun < 3:
                    self.saldo_pelanggan-=transfer+5000
                    print("Berhasil transfer, biaya administrasi Rp 5000")
            
            else:
                self.saldo_pelanggan-=transfer
                print("Berhasil transfer, biaya administrasi gratis")
                
    def suku_bunga(self):
        usia_akun=2023-self.tahun_daftar
        
        if self.saldo_pelanggan>=10000000:
            if usia_akun>=3:
                bungabulanan=self.saldo_pelanggan*0.01
                print(f"Bunga bulanan akun sebesar Rp {bungabulanan}")
            elif usia_akun<3:
                bungabulanan=self.saldo_pelanggan*0.02
                print(f"Bunga bulanan akun sebesar Rp {bungabulanan}")
        else:
            bungabulanan=self.saldo_pelanggan*0.03
            print(f"Bunga bulanan akun sebesar Rp {bungabulanan}")
            
akun1=AkunGold("Andi",2019,2000000000)
akun2=AkunSilver("Wawan", 2016, 80000000)

akun1.lihat_saldo()
akun1.transfer_saldo()
akun1.lihat_saldo()
akun1.suku_bunga()

akun2.lihat_saldo()
akun2.transfer_saldo()
akun2.lihat_saldo()
akun2.suku_bunga()
