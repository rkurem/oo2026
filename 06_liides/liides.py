from datetime import datetime
from abc import ABC, abstractmethod

class Adder(ABC):
    @abstractmethod
    def add(self, nr: float) -> None:
        pass
    
    @abstractmethod
    def getSum(self) -> float:
        pass
    
    def greet(self) -> None:
        print("Hello")


#looge Adder-i alamklass SimpleAdder
#defineerige meetodid lisamiseks ja summa leidmiseks
class SimpleAdder(Adder):
    def __init__(self):
        self.total = 0
        
    def add(self, nr: float) -> None:
        self.total += nr
        
    def getSum(self) -> float:
        return self.total

#looge klass CharCounter. Selle eksemplarile saab lisada sõnu. charcounter jätab tema
#sees oleva adderi kaudu meelde sõnade tähtede koguarvu
    
class CharCounter:
    def __init__(self, adder: Adder):
        self.adder = adder
        self.wordAdder = None
        
    def AddWord(self, word):
        self.adder.add(len(word))
        
        if self.wordAdder is not None:
            self.wordAdder.add(1) 
    
    def GetChars(self):
        return self.adder.getSum()

#tee charcounter klassile k2sklus sõnade loendru määramiseks
#juhul, kui loendur on m22ratud, sellisel huhul suurendatakse iga sõna puhul
#loendurit ühe võrra
#kysi loendatud sõnade arvu, loenduri puudumisel vastatakse -1
#kasuta loendamiseks adderi eraldi eksemplari
    
    def setWordCounter(self):
        self.wordAdder = SimpleAdder()

    def getWordCount(self):
        if self.wordAdder is None:
            return -1
        return self.wordAdder.getSum()

#Koosta uus adderi alamklass, mis toimib nõnda, et eksemplari loomisel antakse
#sinna faili nimi andmete hoidmiseks. Igal lisamisel kirjutatakse faili kogus
#ja lisamise kellaaeg. Summa küsimisel arvutatakse andmed failist kokku
#kasutatakse sama faili andmeid ka kordual käivitamisel
#näitprogramm, kasutajalt küsitatakse lauseid. iga lause sõnad salvestatakse
#charcounter + uue adderi abil faili. eraldi käsu peale saab kysida mitme tähe
#andmeid on salvestatud.

    
class FileAdder(Adder):
    def __init__(self, filename):
        self.filename = filename

    def add(self, nr: float) -> None:
        timeNow = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(self.filename, "a") as f:
            f.write(f"{nr},{timeNow}\n")
        
    def getSum(self) -> float:
        total = 0
        with open(self.filename, "r") as f:
            for a in f:
                value = float(a.split(",")[0])
                total += value
        return total
        
a=SimpleAdder()
count = CharCounter(a)
count.setWordCounter()

a.add(10)
print(a.getSum())
a.add(5)
print(a.getSum())

count.AddWord("Ben")
count.AddWord("tere")
count.AddWord("Albert")

print(count.GetChars())
print(count.getWordCount())


a2:Adder = FileAdder("data.txt")
a2.add(17)
a2.add(50)
print(a2.getSum())
