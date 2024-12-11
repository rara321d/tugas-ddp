from Animal import *

class Ular(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, design, racun):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.design = design
        self.racun = racun
        
    def cetak_ular(self):
        super().cetak() 
        print("design\t\t:", self.design,
              "\nracun\t\t:", self.racun)
        
anaconda = Ular("Anaconda", "Kambing", "Amazon", "Bertelur", "Batik solo", "Tidak terbiasa") 
anaconda.cetak_ular()   

piton = Ular("Piton", "Kelinci", "Hutan", "Betrelur", "Kotak kotak", "Berbiasa") 
piton.cetak_ular()       
              