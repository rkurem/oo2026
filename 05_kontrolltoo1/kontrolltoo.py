#1) koosta funkt, mis korrutab parameerina antud 2 arvu
#ning võtab neist ruutjuure.
#2)Arve võib rohkem olla, need antakse ette kogumina. Antud arvud korrutatakse
#kokku ning võetakse niimitmes ruutjuur(astendaja poordvaartus) kui mitu arvu oli.
#3) Klass, kus inimese palk 1a. Saab lisada koef muutuse palgaga (0.95 on -5% langus).
#saab kysida palka iga aasta. Saab kysida palka geo_kesk järgi.

import math

def ruutjuur(a, b):
    return round(math.sqrt(a * b), 2)

def geom_kesk(arvud):
    #tehe on ss arv ** 1/n
    korrutis = 1
    for arv in arvud:
        korrutis *= arv
    
    n = len(arvud)
    return round(korrutis ** (1/n), 4)

class Palk:
    def __init__(self, palk1aasta):
        self.palk1aasta = palk1aasta
        self.palgaMuutus = []

#palga keofitsent
    def lisa_koef(self, koef):
        self.palgaMuutus.append(koef) #lisan koefi andmed olevasolevasse listi, et andmeid ei rikuks
#palk igal aastal
    def palkIgaAasta(self):
        koikPalgad = [self.palk1aasta]
        praegunePalk = self.palk1aasta
            
        for koef in self.palgaMuutus:
            praegunePalk *= koef
            koikPalgad.append(round(praegunePalk, 2))
        return koikPalgad
            
#palk geom_kesk
    def PalkGeoKeskmisega(self):
        if len(self.palgaMuutus) == 0:
            return [self.palk1aasta]
            
        geo = geom_kesk(self.palgaMuutus)
        koikPalgad = [self.palk1aasta]
        praegunePalk = self.palk1aasta
        
        for _ in self.palgaMuutus:
            praegunePalk *= geo
            koikPalgad.append(round(praegunePalk, 2))
            
        return koikPalgad


#n2itandmed
print("kahe arvu ruutjuur:")
print(ruutjuur(7, 10))
print()
print("n arvude geomeetriline kesk:")
print(geom_kesk([5, 9]))
print(geom_kesk([2, 8, 4, 5])) 
print(geom_kesk([1, 1, 1, 1, 1]))
print()
print("palga andmed:")
inimene = Palk(1000)

inimene.lisa_koef(1.25)
inimene.lisa_koef(0.95)
print("koefitsendid:", inimene.palgaMuutus)
print("palgad:", inimene.palkIgaAasta())
print("palgad geom keskmise järgi:", inimene.PalkGeoKeskmisega())

