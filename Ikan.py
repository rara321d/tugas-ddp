from Animal import *

class Ikan(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, habitat, ukuran):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.habitat = habitat
        self.ukuran = ukuran
        
    def cetak_Ikan(self):
        super().cetak() 
        print("habitat\t\t:", self.habitat,
              "\nukuran\t\t:", self.ukuran)
        
Mas = Ikan("Mas", "Pakan ikan", "Air tawar", "Telur", "Kolam", "Kecil")
Mas.cetak_Ikan()      

Mujair = Ikan("Mujair", "Daun talas", "Air tawar", "Telur", "Kolam", "Sedang")
Mujair.cetak_Ikan()  