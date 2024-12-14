from animal import animal

# setiap class child itu memiliki 2 properti dan method
class carnivora(animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, indra_berburu, kecepatan_lari, cara_bernapas):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.indra_berburu = indra_berburu
        self.kecepatan_lari = kecepatan_lari
        self.cara_bernapas = cara_bernapas
        
    def info_carnivora(self):
        super().info_animal()
        print('Indra Berburu menggunakan \t :', self.indra_berburu,
              '\nKecepatan Lari \t\t\t :', self.kecepatan_lari,
              '\nCara Bernapas \t\t\t :', self.cara_bernapas,
              '\n--------------------------------------------------------')
        
carnivora = carnivora('Harimau', 'Daging', 'Darat', 'Melahirkan', 'Taring', 'Sangat Cepat', 'Paru-Paru')
carnivora.info_carnivora()

# Carnivora 2
class carnivora2(animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, indra_berburu, kecepatan_lari, cara_bernapas):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.indra_berburu = indra_berburu
        self.kecepatan_lari = kecepatan_lari
        self.cara_bernapas = cara_bernapas
        
    def info_carnivora2(self):
        super().info_animal()
        print('Indra Berburu menggunakan \t :', self.indra_berburu,
              '\nKecepatan Lari \t\t\t :', self.kecepatan_lari,
              '\nCara Bernapas \t\t\t :', self.cara_bernapas,
              '\n--------------------------------------------------------')
        
carnivora2 = carnivora2('Serigala', 'Hewan Kecil', 'Darat', 'Melahirkan', 'Taring', 'Cepat', 'Paru-Paru')
carnivora2.info_carnivora2()

# Carnivora 3
class carnivora3(animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, indra_berburu, kecepatan_lari, cara_bernapas):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.indra_berburu = indra_berburu
        self.kecepatan_lari = kecepatan_lari
        self.cara_bernapas = cara_bernapas
        
    def info_carnivora3(self):
        super().info_animal()
        print('Indra Berburu menggunakan \t :', self.indra_berburu,
              '\nKecepatan Lari \t\t\t :', self.kecepatan_lari,
              '\nCara Bernapas \t\t\t :', self.cara_bernapas,
              '\n--------------------------------------------------------')
        
carnivora3 = carnivora3('Beruang', 'Serangga, Madu, Buah', 'Darat', 'Melahirkan', 'Taring', 'Cepat', 'Paru-Paru')
carnivora3.info_carnivora3()