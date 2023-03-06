class Mahasiswa():
    tahun_sekarang = 2023
    def __init__(self, nama, NIM, kelasPBO, jumlahSKS, tahun_lahir):
        self.nama = nama
        self.NIM = NIM
        self.kelasPBO = kelasPBO
        self.jumlahSKS = jumlahSKS
        self.tahun_lahir = tahun_lahir 
    def outputUmur(self):
        umur = Mahasiswa.tahun_sekarang - self.tahun_lahir
        print("Mahasisw ini berumur " + str(umur) + " tahun")

mhs1 = Mahasiswa("Toby", 121140099, "B", 4, 2003)

mhs1.outputUmur()
print("Mahasiswa ini bernama " + mhs1.nama)
print("Mahasiswa ini memiliki NIM = " + str(mhs1.NIM))
print("Mahasiswa ini memilih kelas PBO R" + mhs1.kelasPBO)
print("Pada semester 4, mahasiswa ini memiliki total SKS sebanyak " + str(mhs1.jumlahSKS))