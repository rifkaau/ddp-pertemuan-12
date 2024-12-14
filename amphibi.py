from animal import animal

# setiap class child itu memiliki 2 properti dan method
class amphibi(animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, jenis_air, cara_bernapas):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.jenis_air = jenis_air
        self.cara_bernapas = cara_bernapas
        
    def info_amphibi(self):
        super().info_animal()
        print('Jenis Air \t\t\t :', self.jenis_air,
              '\nCara Bernapas \t\t\t :', self.cara_bernapas,
              '\n--------------------------------------------------------')
        
amphibi = amphibi('Buaya', 'Daging', 'Darat dan Air', 'Bertelur', 'Air Tawar', 'Paru-Paru')
amphibi.info_amphibi()

# Amphibi 2
class amphibi2(animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, jenis_air, cara_bernapas):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.jenis_air = jenis_air
        self.cara_bernapas = cara_bernapas
        
    def info_amphibi2(self):
        super().info_animal()
        print('Jenis Air \t\t\t :', self.jenis_air,
              '\nCara Bernapas \t\t\t :', self.cara_bernapas,
              '\n--------------------------------------------------------')
        
amphibi2 = amphibi2('Katak', 'Lalat', 'Darat dan Air', 'Bertelur', 'Air Tawar', 'kulit dan paru-paru')
amphibi2.info_amphibi2()

# Amphibi 3
class amphibi3(animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, jenis_air, cara_bernapas):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.jenis_air = jenis_air
        self.cara_bernapas = cara_bernapas
        
    def info_amphibi3(self):
        super().info_animal()
        print('Jenis Air \t\t\t :', self.jenis_air,
              '\nCara Bernapas \t\t\t :', self.cara_bernapas,
              '\n--------------------------------------------------------')
        
amphibi3 = amphibi3('Salamander', 'Udang Air Asin', 'Darat dan Air', 'Bertelur', 'Air Tawar', 'Paru-paru')
amphibi3.info_amphibi3()

