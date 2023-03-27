#Tugas Single Inheritance 
class Komputer:
    def __init__(self,nama,jenis,harga,merk) -> None:
        self.nama = nama
        self.jenis = jenis
        self.harga = harga
        self.merk = merk

class Processor(Komputer):
    def __init__(self, nama, jenis, harga, merk,jumlah_core,kecepatan_processor) -> None:
        super().__init__(nama, jenis, harga, merk)
        pass

class RAM(Komputer):
    def __init__(self, nama, jenis, harga, merk,ram_capacity) -> None:
        super().__init__(nama, jenis, harga, merk)
        pass

class HDD(Komputer):
    def __init__(self, nama, jenis, harga, merk,drive_capacity,rpm) -> None:
        super().__init__(nama, jenis, harga, merk)

class VGA(Komputer):
    def __init__(self, nama, jenis, harga, merk,video_capacity) -> None:
        super().__init__(nama, jenis, harga, merk)

class PSU(Komputer):
    def __init__(self, nama, jenis, harga, merk,daya) -> None:
        super().__init__(nama, jenis, harga, merk)