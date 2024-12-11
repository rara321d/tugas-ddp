from Animal import *

class Burung(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis, bunyi):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis = jenis
        self.bunyi = bunyi
        
    def cetak_burung(self):
        super().cetak() 
        print("jenis\t\t:", self.jenis,
              "\nbunyi\t\t:", self.bunyi)
        
Merpati = Burung("Merpati", "Biji-bijian", "udara", "Telur", "Kolumbidae", "cooo-wook-wokk") 
Merpati.cetak_burung()

Elang = Burung("Elang", "Daging", "Laut", "Telur", "Predator", "wooo-woouhhh") 
Elang.cetak_burung()      