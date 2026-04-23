#koosta programm, kus sisendiks on kannu võimsus, sees oleva vee hulk
#ja algtemperatuur. Väljundiks on vee keemaminekuks kulunud aeg.


voimsus= int(input("Kirjuta kannu võimsus (dzaul): "))
hulk = float(input("Kirjuta kannu sees oleva vee hulk: "))
temp = int(input("Kirjuta algtemperatuur: "))

keem_temp = 100
temp2 = keem_temp - temp
arv = 4200 * hulk
sek = arv / voimsus
kokku = sek * temp2

print(kokku)

