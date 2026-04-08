# Pane näide käima, muuda andmeid. +
# Koosta jadaühenduse klassist kaks eksemplari, katseta tulemusi mitmesuguse pinge korral. +
# Lisa jadaühenduse klassile käsklus kogu eralduva võimsuse leidmiseks. +
# Väljasta jadaühenduse takistitest suurim takistus
# Väljasta jadaühendusest suurim ühele takistile langev pinge 5-voldise kogupinge juures
# Väljasta jadaühendusest suurim ühelt takistilt eralduv võimsus 5-voldise kogupinge juures

class Resistor:
    def __init__(self, R):
        self.R = R

    def get_potential(self, I):
        return I * self.R

    def get_power(self, U):
        return (U * U) / self.R

    def get_resistance(self):
        return self.R


class SeriesCircuit:
    def __init__(self):
        self.resistors = []

    def addResistor(self, resistor):
        self.resistors.append(resistor)

    def getTotalResistance(self):
        total = 0
        for r in self.resistors:
            total += r.get_resistance()
        return total

    def getCurrent(self, U):
        return U / self.getTotalResistance()

    def getTotalPower(self, U):
        return U * self.getCurrent(U)

    def getMaxResistance(self):
        biggest = self.resistors[0].get_resistance()
        for r in self.resistors:
            if r.get_resistance() > biggest:
                biggest = r.get_resistance()
        return biggest

    def getMaxVoltage(self, U_total):
        I = self.getCurrent(U_total)
        biggest = self.resistors[0].get_potential(I)
        for r in self.resistors:
            voltage = r.get_potential(I)
            if voltage > biggest:
                biggest = voltage
        return biggest

    def getMaxPower(self, U_total):
        I = self.getCurrent(U_total)
        biggest = self.resistors[0].get_power(self.resistors[0].get_potential(I))
        for r in self.resistors:
            power = r.get_power(r.get_potential(I))
            if power > biggest:
                biggest = power
        return biggest

r1 = SeriesCircuit()
r1.addResistor(Resistor(100))
r1.addResistor(Resistor(200))
r1.addResistor(Resistor(300))

r2 = SeriesCircuit()
r2.addResistor(Resistor(50))
r2.addResistor(Resistor(150))
r2.addResistor(Resistor(250))


print("Jadayhendus 1")
print("Kogutakistus:", r1.getTotalResistance())
print("Koguvõimsus 5V juures:", r1.getTotalPower(5))
print("Suurim takistus:", r1.getMaxResistance())
print("Suurim pinge 5V juures:", r1.getMaxVoltage(5))
print("Suurim võimsus 5V juures:", r1.getMaxPower(5))

print()

print("Jadayhendus 2")
print("Kogutakistus:", r2.getTotalResistance())
print("Koguvõimsus 5V juures:", r2.getTotalPower(5))
print("Suurim takistus:", r2.getMaxResistance())
print("Suurim pinge 5V juures:", r2.getMaxVoltage(5))
print("Suurim võimsus 5V juures:", r2.getMaxPower(5))
