import random

class Robot: 
    jumlah_turn = 0
    alive = True
    def __init__(self,nama,health,damage) -> None:
        self.nama = nama
        self.health = health
        self.damage = damage
    def terima_aksi(self,damage):
        if damage > self.health:
            self.health=0
            print(f"{self.nama} telah menerima damage sebesar {damage} poin, sisa health : {self.health}")
            print(f"{self.nama} telah mati secara terhormat!")
            Robot.alive = False 
        else:
            self.health += damage
            print(f"{self.nama} telah menerima damage sebesar {damage} poin dengan sisa health sebesar {self.health}")
    def lakukan_aksi(self,other):
        if self.nama == "Antares":
            if (Robot.jumlah_turn % 3) == 0:
                self.damage = self.damage * 1.5
                Robot.terima_aksi(other,self.damage)
                self.damage = 5 #to be changed
            else:
                Robot.terima_aksi(other,self.damage)
        elif self.nama == "Alphasetia":
            if (Robot.jumlah_turn % 2) == 0:
                self.health += 4000 #to be changed 
                Robot.terima_aksi(other,self.damage)
                return f"Alphasetia mendapatkan health tambahan sebesar 4000\n" #to be changed 
            else:
                Robot.terima_aksi(other,self.damage)
                return f"Alphasetia mendapatkan health tambahan sebesar 4000\n"
        elif self.nama == "Lecalicus":
            if (Robot.jumlah_turn % 4) == 0:
                self.damage = self.damage * 2 
                self.health += 7000
                Robot.terima_aksi(other,self.damage)
                self.damage = 5500
                return f"Lecalicus mendapatkan health tambahan sebesar 7000\n"
            else:
                Robot.terima_aksi(other,self.damage)
                return f"Lecalicus mendapatkan health tambahan sebesar 7000\n"

class Antares(Robot):
    def __init__(self):
        super().__init__("Antares", 50000, 5000)

class Alphasetia(Robot):
    def __init__(self):
        super().__init__("Alphasetia", 40000, 6000)

class Lecalicus(Robot):
    def __init__(self):
        super().__init__("Lecalicus", 45000, 5500)

print("Welcome to the game! Selamat datang ke game ini yaitu Pertandingan Robot Yamako")
robot_pilihan = int(input("Siapakah yang akan jadi robot pilihanmu? (1 = Antares, 2 = Alphasetia, 3 = Lecalicus) =  "))
while robot_pilihan <= 3 and robot_pilihan > 0:
    if robot_pilihan == 1:
        myrobot = Antares()
        robot_pilihan = 0
    elif robot_pilihan == 2:
        myrobot = Alphasetia()
        robot_pilihan = 0
    elif robot_pilihan == 3:
        myrobot = Lecalicus()
        robot_choice = 0
    else : 
        print("Pilihan antara 1, 2, dan 3 saja!")
        robot_pilihan = int(input("Siapakah yang akan jadi robot pilihanmu? (1 = Antares, 2 = Alphasetia, 3 = Lecalicus) =  "))
pilihan_musuh = int(input("Siapakah yang akan jadi musuh robotmu? (1 = Antares, 2 = Alphasetia, 3 = Lecalicus) =  "))
while pilihan_musuh <= 3 and pilihan_musuh > 0:
    if pilihan_musuh == 1:
        robot_musuh = Antares()
        pilihan_musuh = 0
    elif pilihan_musuh == 2:
        robot_musuh = Alphasetia()
        pilihan_musuh = 0
    elif pilihan_musuh == 3:
        robot_musuh = Lecalicus()
        pilihan_musuh = 0
    else:
        print("Pilihan antara 1, 2, dan 3 saja!")
        pilihan_musuh = int(input("Siapakah yang akan jadi musuh robotmu? (1 = Antares, 2 = Alphasetia, 3 = Lecalicus) =  "))
        
print("Untuk tahap selanjutnya, mohon pilih 1 untuk batu, 2 untuk kertas, dan 3 untuk gunting")
while Robot.alive:
    Robot.jumlah_turn += 1 
    print(f"Turn saat ini: {Robot.jumlah_turn}")
    print(f"Robotmu ({myrobot.nama} - {myrobot.health} HP), robot musuh ({robot_musuh.nama} - {robot_musuh.health} HP)")
    myturn = int(input(f"Pilih tangan robotmu ({myrobot.nama}) : "))
    enemyturn = random.randint(1,3)
    print(f"Robot lawan {robot_musuh.nama} memilih : {enemyturn}")

    if myturn == 1:
        if enemyturn == 1:
            print("Tidak ada yang menang suit!")
        elif enemyturn == 2:
            print(Robot.lakukan_aksi(robot_musuh, myrobot))
        elif enemyturn == 3:
            print(Robot.lakukan_aksi(myrobot, robot_musuh))
    elif myturn == 2:
        if enemyturn == 1:
            print(Robot.lakukan_aksi(myrobot, robot_musuh))
        elif enemyturn == 2:
            print("Tidak ada yang menang suit!")
        elif enemyturn == 3:
            print(Robot.lakukan_aksi(robot_musuh, myrobot))
    elif myturn == 3:
        if enemyturn == 1:
            print(Robot.lakukan_aksi(robot_musuh, myrobot))
        elif enemyturn == 2:
            print(Robot.lakukan_aksi(myrobot, robot_musuh))
        elif enemyturn == 3:
            print("Tidak ada yang menang suit!\n")

print("Pertandingan berakhir!")
