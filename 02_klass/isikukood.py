import calendar
import time

class Isikukood:
    def __init__(self, isikukood):
        if len(isikukood) != 11:
            raise Exception("Vigane pikkus")
        self.kood = isikukood

    def kuupaev(self):
        return self.kood[5:7]

    def kuu(self):
        return self.kood[3:5]

    def kuu_nimi(self):
        kuu_nr = int(self.kuu())
        return calendar.month_name[kuu_nr]
    
    def aasta(self):
        nr=int(self.kood[0])
        return int(nr/2)*100+1800+ int(self.kood[1:3])

                
    def kontroll(self):
        kordajad = (1,2,3,4,5,6,7,8,9,1)
    
        summa = 0
        for i in range(10):
            summa = summa + kordajad[i] * int(self.kood[i])

        j22k = summa % 11

        if j22k != 10:
            kontrollnumber = j22k
        else:
            kontrollnumber = 0
        print("Isikukoodi kontrollnumber on:", kontrollnumber)
            
        if kontrollnumber == int(self.kood[10]):
            return "Kontrollnumber sobib, seega isikukood on õige"
        else:
            return "Tekkis viga, kontrollnumber ei ole sama"

ik1 = Isikukood("50602270268")
print(ik1.kuupaev())       
print(ik1.kuu())      
print(ik1.kuu_nimi())
print(ik1.aasta())
print(ik1.kontroll())

