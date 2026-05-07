#JOONE VÕRRAND

#Koosta liides joone y-i väärtuse leidmiseks vastavalt x-i väärtusele. Koosta automaattestid kontrollimaks mitut punkti sirgel y=3x
#Koosta realiseeriv klass, millele antakse konstruktoris ette x-i kordaja. Kontrolli klassi eksemplari oskuste vastavust testidele

import unittest
import matplotlib.pyplot as plt

class Joon:
    def arvutaY(self, x):
        pass
    
class Joon2(Joon):
    def __init__(self, kordaja):
        self.kordaja = kordaja
    
    def arvutaY(self, x):
        return self.kordaja * x
    

#Loo teine realiseeriv klass, millele saab ette anda kordaja ja vabaliikme. Kontrolli selle klassi tööd liidese kaudu testidega
#joontele y=3x ja y=3x+2. Koosta funktsioon, mis saab parameetriks x-ide massiivi ning liidesele vastava y-koordinaatide arvutava klassi
#ning tagastab vastavate y-ite massiivi. Kontrolli klasside ja funktsiooni tööd automaat.

class JoonVabaliikmega(Joon):
    def __init__(self, kordaja, vabaliige):
        self.kordaja = kordaja
        self.vabaliige = vabaliige
        
    def arvutaY(self, x):
        return self.kordaja * x + self.vabaliige
    
def arvutaYid(xid, joon):
    return [joon.arvutaY(x) for x in xid]

#Kuva parameetritele vastav joon ekraanile koos koordinaattelgedega.
#Kasutaja saab parameetreid muuta ning vastavalt muutub ka joonis

def joonista(joon):
    xid = [-3, -2, -1, 0, 1, 2, 3]
    yid = arvutaYid(xid, joon)
    
    plt.plot(xid, yid)
    plt.axhline(0, color="black")
    plt.axvline(0, color="black")

    plt.grid()
    plt.show()

kordaja = float(input("Kirjuta kordaja väärtus: "))
vaba = float(input("Kirjuta vabaliikme väärtus: "))

j = JoonVabaliikmega(kordaja, vaba)
joonista(j)


#autmaattesti osa
class TestJooned(unittest.TestCase):
    def kontrollSirge3x(self, joon):
        self.assertEqual(joon.arvutaY(0), 0)
        self.assertEqual(joon.arvutaY(1), 3)
        self.assertEqual(joon.arvutaY(2), 6)
    
    #1 test
    def test3x(self):
        self.kontrollSirge3x(Joon2(3))
    #2 test
    def testVabaliikmega_3x(self):
        self.kontrollSirge3x(JoonVabaliikmega(3, 0))
    #3 test
    def testVabaliikmega(self):
        j= JoonVabaliikmega(3, 2)
        self.assertEqual(j.arvutaY(0), 2)
        self.assertEqual(j.arvutaY(3), 11)
        self.assertEqual(j.arvutaY(4), 14)
        self.assertEqual(j.arvutaY(1), 5)    
    #4 test
    def testArvutaYid_Joon2(self):
        yid = arvutaYid([0, 1, 2, 3], Joon2(3))
        self.assertEqual(yid, [0, 3, 6, 9])
    #5 test
    def testArvutaYid_Vabaliikmega(self):
        yid = arvutaYid([0, 1, 2], JoonVabaliikmega(3, 2))
        self.assertEqual(yid, [2, 5, 8])
    
if __name__ == "__main__":
    unittest.main()
