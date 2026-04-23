#10 kg raudradiaatori küttevõimsus on 1 kilovatt. Mitme kraadi võrra soojeneb radiaator kümne sisselülitatud sekundi jooksul kui radiaatorist soojus välja ei pääse?
#Sama 40-kraadine raudradiaator jahtub 20-kraadises toas mõõtmetega 4x3x2,5 meetrit 30 kraadini.
#Kui palju tõuseb sealjuures toa temperatuur arvestades, et kogu eraldunud soojus kulub õhu soojendamiseks?
#Koosta klass materjalikoguse tarbeks. Materjalikogusel on mass, erisoojus ja algtemperatuur. Küsida saab temperatuuri.
#Lisa käsklus energiavahetuseks - positiivse väärtusega parameeter lisab energiat, negatiivne eemaldab (soojus)energiat.
#Endiselt saab küsida temperatuuri. Loo eksemplar ja katseta.
class Materialikogus:
    def __init__(self, mass, erisoojus, temperatuur):
        self.mass = mass
        self.erisoojus = erisoojus
        self.temperatuur = temperatuur

    def get_temperatuur(self):
        return self.temperatuur

    def energiavahetus(self, j):
        delta_temp = j / (self.mass * self.erisoojus)
        self.temperatuur += delta_temp
    
class Ohukogus(Materialikogus):
    def __init__(self, pikkus, laius, korgus, temperatuur):
        ruumala = pikkus * laius * korgus
        tihedus = 1.23
        mass = ruumala * tihedus
        erisoojus = 1000
        super().__init__(mass, erisoojus, temperatuur)

vesi = Materialikogus(3, 4200, 20)
vesi.energiavahetus(10000)
print("Vee temperatuur:", vesi.get_temperatuur())

radiaator = Materialikogus(10, 412, 20)
radiaator.energiavahetus(10000)
print("Radiaatori temperatuur:", radiaator.get_temperatuur())


if radiaator.get_temperatuur() > vesi.get_temperatuur():
    change_amount = 1000
    radiaator.energiavahetus(-change_amount)
    vesi.energiavahetus(change_amount)

ohk = Ohukogus(4, 3, 2.5, 20)

print("Pärast energiavahetust:")
print("Radiaator:", radiaator.get_temperatuur())
print("Vesi:", vesi.get_temperatuur())
print("Õhk:", ohk.get_temperatuur())
