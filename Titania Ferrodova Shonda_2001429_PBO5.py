
class Indonesia():
    def Ibukota(self):
        print("Jakarta adalah Ibukota Indonesia.")
 
    def Bahasa(self):
        print("Bahasa Indonesia adalah bahasa yang sering digunakan di Indonesia")
 
    def Keterangan(self):
        print("Indonesia adalah negara maritim.")
 
class Korsel():
    def Ibukota(self):
        print("Seoul adalah ibukota Korea Selatan.")
 
    def Bahasa(self):
        print("Bahasa korea adalah bahasa yang sering digunakan di Korea")
 
    def Keterangan(self):
        print("Korea adalah Negeri Gingseng")
 
obj_indo = Indonesia()
obj_KS = Korsel()
for country in (obj_indo, obj_KS):
    country.Ibukota()
    country.Bahasa()
    country.Keterangan()