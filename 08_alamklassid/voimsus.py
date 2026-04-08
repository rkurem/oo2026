# Lisa takistile väli lubatud maksimumvõimsuse kohta. Selle sisestamine on vajalik konstruktoris.
# Loo käsk kontrollimaks, kas parameetrina antud pinge on vastava takisti puhul lubatud - st.
# kas pingestamisel eralduv võimsus jääb lubatud maksimuvõimsuse piiresse
# Koosta takistitest massiiv. Koosta funktsioon, mis loob uue massiivi takistitest, mille lubatud võimsus jääb etteantud pinge korral lubatud piiresse.

class Resistor:
    def __init__(self, R, max_power):
        self.R = R                 
        self.max_power = max_power  

    def get_current(self, U):
        return U / self.R

    def get_power(self, U):
        return self.get_current(U) * U

    def is_allowed(self, U):
        return self.get_power(U) <= self.max_power

def filter_resistors(resistors, voltage):
    result = []

    for r in resistors:
        if r.is_allowed(voltage):
            result.append(r)

    return result

resistors = [
    Resistor(220, 0.25),
    Resistor(100, 0.5),
    Resistor(330, 0.1)
]

voltage = 5

safe = filter_resistors(resistors, voltage)

print("Sobivad takistid 5V juures:", len(safe))
for r in safe:
    print(f"  {r.R}R(takistus) (max võimsus: {r.max_power}W)")
