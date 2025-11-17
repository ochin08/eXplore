

class Tao:
    def __init__(self, pangalan):
        self._pangalan = pangalan

    @property
    def pangalan(self):
        return self._pangalan

    @pangalan.setter
    def pangalan(self, value):
        if not value:
            raise ValueError("Hindi puwedeng walang pangalan.")
        self._pangalan = value

tao = Tao("Ramil")
print(tao.pangalan)  # Getter
tao.pangalan = "Juan"  # Setter
print(tao.pangalan)
