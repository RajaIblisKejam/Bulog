#-------------------
# Suplayer
#-------------------

class Petani:
    def __init__(self, nama, asal,):
        self.nama = nama
        self.asal = asal
        self.hasil_panen = []

    def panen (self, jumlah): #belum ditimbang, belum disortir kualitasnya
        beras_baru = Beras(jumlah, self.nama, self.asal)
        self.hasil_panen.append(beras_baru)

    def tampilkan_hasil_panen(self):
        print (f"=== Hasil Panen {self.nama} ===")
        for b in self.hasil_panen:
            print (b.info())
        print()

class Beras:
    def __init__(self, jumlah_karung, namapetani, asalpetani):
        self.jumlah_karung = jumlah_karung
        self.namapetani = namapetani
        self.asalpetani = asalpetani

    def info(self): #menampilkan informasi tentang beras yang disetorkan
        return f"Asal: {self.asalpetani} | Petani: {self.namapetani} | {self.jumlah_karung} Karung "
    

# CONTOH UJI COBA
def main():
    p1 = Petani("Pak Budi", "Desa Sukamaju")
    p1.panen(5)
    p1.tampilkan_hasil_panen()

    p2 = Petani("Bu Ani", "Desa Mulyo")
    p2.panen(3)
    p2.tampilkan_hasil_panen()

if __name__ == "__main__":
    main()



        