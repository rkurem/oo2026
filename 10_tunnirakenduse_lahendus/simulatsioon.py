class SimulatsiooniProgramm:
    def __init__(self, maht_liitrites, temp, valis_temp):
        self.maht = maht_liitrites  # liitrites
        self.temp = temp            # °C
        self.valis_temp = valis_temp

    def jahtu_100s(self):
        vahe = self.temp - self.valis_temp
        
        if vahe <= 0:
            return
        jahtumine = (vahe / 80) * (2 / self.maht)
        
        self.temp -= jahtumine

    def simuleeri(self, sammud):
        for i in range(sammud):
            self.jahtu_100s()
            print(f"Aeg: {(i+1)*100}s, Temp: {self.temp:.2f}°C")
            
kann = SimulatsiooniProgramm(1.0, 100, 20)
kann.simuleeri(10)
