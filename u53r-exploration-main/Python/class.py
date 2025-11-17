






# Gumawa tayo ng class na tinatawag na "Tao"
class Tao:
    def __init__(self, pangalan, edad):
        self.pangalan = pangalan
        self.edad = edad

    def batiin(self):
        print(f"Kumusta! Ako si {self.pangalan}, {self.edad} taong gulang.")

# Gumawa tayo ng object mula sa class na Tao
tao1 = Tao("Ramil", 20)

print(tao1.pangalan)

# Tawagin ang method na batiin
tao1.batiin()