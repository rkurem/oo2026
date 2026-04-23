#Koosta programm, millele antakse ette näitväärtused välistemperatuuri, kannu temperatuuri ning 30 sekundi jooksul
#muutunud kraadide kohta (võib olla ka murdarv). Programmilt saab küsida etteantud temperatuuril
#jahtutud kraadide arv 30 sekundi jooksul. Testimiseks andmed: kelder 10 kraadi,
#kann 20 kraadi, 30 sekundiga jahtus 0,1 kraadi. 60 kraadi pealt võiks jahtuda
#30 sekundiga 0,5 kraadi.

def valem(v2lis_temp, kann_temp, muutus):
    vastus= muutus / (kann_temp - v2lis_temp)
    return vastus

def jahtumine_30s(v2lis_temp, k, temp):
    vastus2 = k * (temp - v2lis_temp)
    return vastus2

v2lis = 10
kann = 20
muutus = 0.1

k = valem(v2lis, kann, muutus)

temp_test = 60
tulemus = jahtumine_30s(v2lis, k, temp_test)

print("30 sekundiga jahtub", temp_test, "kraadi juures", round(tulemus,2))
