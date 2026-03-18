from abc import ABC, abstractmethod

class Hindaja(ABC):
    @abstractmethod
    def hinda(self, punktid: int):
        pass

class AineHindaja(Hindaja):
    def __init__(self, aine_nimi: str):
        self.aine_nimi = aine_nimi
        self.tulemused = []

    def hinda(self, punktid: int):
        if punktid >= 90:
            hinne = 5
        elif punktid >= 75:
            hinne = 4
        elif punktid >= 50:
            hinne = 3
        else:
            hinne = 2

        self.tulemused.append((punktid, hinne))
        return f"{self.aine_nimi}: {punktid}p - hinne {hinne}"

class TestiHindaja(Hindaja):

    def __init__(self, testi_nimi: str, lävend: int):
        self.testi_nimi = testi_nimi
        self.lävend = lävend
        self.tulemused = []

    def hinda(self, punktid: int):
        if punktid >= self.lävend:
            tulemus = "Lävend ületatud"
        else:
            tulemus = "Tulemus ei ületanud lävendit"

        self.tulemused.append((punktid, tulemus))
        return f"{self.testi_nimi}: {punktid}/{self.lävend} - {tulemus}"

mat = AineHindaja("Matemaatika")
est = AineHindaja("Eesti keel")
eksam = TestiHindaja("Lõpueksam", 50)

print(mat.hinda(85))
print(mat.hinda(92))
print(est.hinda(42))
print()
print(eksam.hinda(70))
print(eksam.hinda(45))
print(eksam.hinda(51))
