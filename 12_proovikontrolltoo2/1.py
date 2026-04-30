#Hulknurk
#* Korrapärase hulknurgaga tegelevale klassile antakse keskpunkti koordinaadid,
#tipu kaugus keskpunktist ning tippude arv. Käsuga saab küsida tippude koordinaadid ning hulknurga pindala.

#* Vastav hulknurk joonistatakse ekraanile.

#* Kasutajal on slaider nurkade arvu määramiseks. Kuvatakse vastav hulknurk ja selle arvuline pindala.
#Kõrvale joonistatakse tulp, mille kõrgus sõltub hulknurga pindalast.

import math

class Hulknurk:
    def __init__(self, keskX, keskY, r, t):
        self.keskX=keskX
        self.keskY=keskY
        self.r=r
        self.t=t
    
    def tipud(self):
        koordinaadid = []
        for i in range(self.t):
            nurk = 2 * math.pi * i / self.t
            x = self.keskX + self.r * math.cos(nurk)
            y = self.keskY + self.r * math.sin(nurk)
            koordinaadid.append((x, y))
        return koordinaadid
    
    def pindala(self):
        return (self.t * self.r**2 * math.sin(2 * math.pi / self.t)) / 2
    

h = Hulknurk(5, 5, 5, 3) 

print("Tippude koordinaadid:")
for t in h.tipud():
    print(t)

print("Pindala:", h.pindala())
