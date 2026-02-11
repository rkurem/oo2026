def elektrihind(voimsus_kw, aeg_h, elektrihind_kWh):
    kulu = voimsus_kw * aeg_h * elektrihind_kWh
    return round(kulu, 2)

#n2idisandmed
tulemus = elektrihind(17, 38, 0.2)

print("Elektrikulu eurodes: ", tulemus)
