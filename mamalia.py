from animal import animal

# setiap class child itu memiliki 2 properti dan method
class mamalia(animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, jenis_kulit, ukuran_tubuh):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.jenis_kulit = jenis_kulit
        self.ukuran_tubuh = ukuran_tubuh
        
    def info_mamalia(self):
        super().info_animal()
        print('Alat Gerak \t\t\t :', self.jenis_kulit,
              '\nCara Bernapas \t\t\t :', self.ukuran_tubuh,
              '\n----------------------------------------------------')
        
mamalia = mamalia('Sapi', 'Rumput', 'Darat', 'Melahirkan', 'Sedikit Berbulu', 'Besar')
mamalia.info_mamalia()

# Mamalia 2
class mamalia2(animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, jenis_kulit, ukuran_tubuh):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.jenis_kulit = jenis_kulit
        self.ukuran_tubuh = ukuran_tubuh
        
    def info_mamalia2(self):
        super().info_animal()
        print('Alat Gerak \t\t\t :', self.jenis_kulit,
              '\nCara Bernapas \t\t\t :', self.ukuran_tubuh,
              '\n----------------------------------------------------')
        
mamalia2 = mamalia2('Anjing', 'Daging', 'Darat', 'Melahirkan', 'Berbulu', 'Sedang')
mamalia2.info_mamalia2()

# Mamalia 3

class mamalia3(animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, jenis_kulit, ukuran_tubuh):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.jenis_kulit = jenis_kulit
        self.ukuran_tubuh = ukuran_tubuh
        
    def info_mamalia3(self):
        super().info_animal()
        print('Alat Gerak \t\t\t :', self.jenis_kulit,
              '\nCara Bernapas \t\t\t :', self.ukuran_tubuh,
              '\n----------------------------------------------------')
        
mamalia3 = mamalia3('Harimau', 'Daging', 'Darat', 'Melahirkan', 'Berbulu', 'Besar')
mamalia3.info_mamalia3()