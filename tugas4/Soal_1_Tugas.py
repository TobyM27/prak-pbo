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
    
processor_1 = Processor('AMD', 'Ryzen 5 7600', 3100000, 4, '3.8Ghz')
processor_2 = Processor("Intel", "Intel CORE i5-13400", 3200000, 4,'4.6Ghz')
ram_1 = RAM('G.Skill','DDR4 SODimm PC19200/2400MHz',1500000,'4GB')
ram_2 = RAM('G.SKILL','Flare X5 DDDR5-6000',2100000,'2x16GB')
hdd_1 = HDD('Seagate','HDD 2.5 inch',295000,'500GB',7200)
hdd_2 = HDD('WD BLack','HDD 2.5 inch',4950000,'2000GB',7200)
vga_1 = VGA('MSI','VGA GTX 1050TI', 3100000,'2GB')
vga_2 = VGA('AsRock','Radeon RX 6800 XT Phantom 16GB', 8300000,'16GB')
psu_1 = PSU('Corsair','Corsair V550',250000,'500W')
psu_2 = PSU('Thermaltake','Toughpower GF1 650W', 1500000,'650W')

komputer_rakitan = [[processor_1, ram_1, hdd_1, vga_1, psu_1], [processor_2,ram_2,hdd_2,vga_2,psu_2]]

rakitan_queue = 1
for x in komputer_rakitan:
    print(f"Komputer {rakitan_queue}")
    rakitan_queue += 1
    for y in x:
        print(y)