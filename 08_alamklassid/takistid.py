#Loo programmiga kolm takistit. Esimese takistus 110 oomi, teise takistus 220 oomi, kolmanda takistus 4700 oomi (ehk 4,7 kilooomi).
#Arvuta iga takisti puhul vool 5-voldise pinge korral.
#Paiguta need kolm takistit massiivi. Rakenda igaühele pinge 5 volti, liida kokku tekkivad voolud nagu juhtub rööpühenduse korral

class Resistor:
    def __init__(self, R):
        self.R = R

    def get_current(self, U):
        return U / self.R

r1 = Resistor(110)
r2 = Resistor(220)
r3 = Resistor(4700)

U = 5

print(r1.get_current(U))
print(r2.get_current(U))
print(r3.get_current(U))
