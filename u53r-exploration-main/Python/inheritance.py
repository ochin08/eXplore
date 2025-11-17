





# Parent class
class Hayop:
    def __init__(self, pangalan):
        self.pangalan = pangalan

    def kilos(self):
        print(f"{self.pangalan} ay kumikilos.")

# Child class
class Aso(Hayop):
    def tahol(self):
        print(f"{self.pangalan} ay tumatahol.")

# Gamitin ang child class
akong_aso = Aso("Bantay")
akong_aso.kilos()   # galing sa parent class
akong_aso.tahol()   # galing sa child class
