# kilpkonn
# 
# kilpkonnal on t2isarvulised koordinaadid x ja y ning suund ["vasakule", "yles", "paremale", "alla"] ning
# k2sklused edasi() ning keeraparemale(). Edasi-k2skluse puhul liigub kilpkonn yhe koordinaadi j2rgi edasi,
# keeraParemale() keerab 90 kraadi paremale.
# 
# Koosta kilpkonna objekt ning n2itprogrmam tema t88 katsetamiseks, saab ette anda x ja y koordinaadi.
class Kilpkonn:
    suunad= {
            "vasakule": [-1, 0],
            "paremale": [1, 0],
            "yles": [0, 1],
            "alla": [0, -1]
            }
    def __init__(self, ux, uy):
        self.x=ux
        self.y=uy
        self.suund="paremale"
        
    def keeraParemale(self):
        sd=list(Kilpkonn.suunad.keys())
        koht=sd.index(self.suund)
        koht=(koht+1) % 4
        self.suund=sd[koht]
        
    def edasi(self):
        self.x+=Kilpkonn.suunad[self.suund][0]
        self.y+=Kilpkonn.suunad[self.suund][1]
        
    def liigu(self, sammud):
        for s in sammud:
            self.edasi() if s=="e" else s.keeraParemale()
        
    
    def asukoht (self):
        return str(self.x) + ", "+str(self.y)
    
    def __str__(self):
        return self.asukoht()
    
k1=Kilpkonn(3, 7)
k1.liigu("eeeeeeeeee")
print(k1.asukoht())
print(k1)
k1.edasi()
print(k1)
k1.keeraParemale()
print(k1)
k1.edasi()
print(k1)

k2=Kilpkonn(-3, 11)
k2.edasi()
print(k2)

