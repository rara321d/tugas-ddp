class person:
    def _init_(self, nama, umur, jeniskelamin):
        self.nama = nama
        self.umur = umur
        self.jeniskelamin = jeniskelamin

    def jalan(self):
        print(f"{self.nama} bisa berjalan")

    def ngomong(self):
        print(f"Dia berbicara karena dia {self.jeniskelamin}")


class Supir(person):
    def _init_(self, nama, umur, jeniskelamin, sim):
        super()._init_(nama, umur, jeniskelamin)
        self.sim = sim 

    def nyupir(self):
        print(f"{self.nama} bisa nyupir karena memiliki SIM {self.sim}")



class Mahasiswa(person):
    def _init_(self, nama, umur, jeniskelamin, nim):
        super()._init_(nama, umur, jeniskelamin)
        self.nim = nim

    def belajar(self):
        print(f"{self.nama} sedang belajar dengan nim {self.nim}")

bayu = person("bayu", 20, "Laki-Laki", "A")
bayu.jalan()
bayu.ngomong()

andi = Supir("andi", 30, "Laki-Laki", "A")
andi.nyupir()

bunga = Mahasiswa("bunga", 20, "perempuan", "132452")
bunga.belajar()
bunga.nyupir