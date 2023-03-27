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
        self.nama = "Processor"
        self.jumlah_core = jumlah_core
        self.kecepatan_processor = kecepatan_processor
    def __str__(self):
        return f"{self.nama} ini merupakan tipe {self.jenis} yang dibuat oleh {self.merk}"

class RAM(Komputer):
    def __init__(self, nama, jenis, harga, merk,ram_capacity) -> None:
        super().__init__(nama, jenis, harga, merk)
        self.nama = "RAM"
        self.ram_capacity = ram_capacity
    def __str__(self):
        return f"{self.nama} ini memiliki kapasitas {self.jenis} yang dibuat oleh {self.merk}"

class HDD(Komputer):
    def __init__(self, nama, jenis, harga, merk,drive_capacity,rpm) -> None:
        super().__init__(nama, jenis, harga, merk)
        self.nama = "SATA"
        self.drive_capacity = drive_capacity
        self.rpm = rpm
    def __str__(self):
        return f"{self.nama} ini memiliki kapasitas {self.jenis} yang dibuat oleh {self.merk}"

class VGA(Komputer):
    def __init__(self, nama, jenis, harga, merk,video_capacity) -> None:
        super().__init__(nama, jenis, harga, merk)
        self.nama = "VGA"
        self.video_capacity = video_capacity

    def __str__(self) :
        return f"{self.nama} ini memiliki kapasitas {self.jenis} yang dibuat oleh {self.merk}"

class PSU(Komputer):
    def __init__(self, nama, jenis, harga, merk,daya) -> None:
        super().__init__(nama, jenis, harga, merk)
        self.nama = "PSU"
        self.daya = daya

    def __str__(self):
        return f"{self.nama} ini memiliki kapasitas {self.jenis} yang dibuat oleh {self.merk}"