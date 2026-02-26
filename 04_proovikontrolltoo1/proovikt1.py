import math
from PIL import Image, ImageDraw

class Kolmnurk:
    xid=[]
    yid=[]
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.xid=[x1, x2, x3]
        self.yid=[y1, y2, y3]
    
    def __str__(self):
        return ", ".join(["("+str(paar[0])+ ", "+str(paar[1])+")"for paar in zip(self.xid, self.yid)])
    
    def tekstiks(self):
        vastus=""
        for nr in range(3):
            vastus+=" ("+str(self.xid[nr])+", "+str(self.yid[nr])+")"
        return vastus
        
class Hulknurk:
    xid = []
    yid= []
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.xid = [x1, x2, x3]
        self.yid = [y1, y2, y3]

    def lisa_punkt(self, x, y):
        self.xid.append(x)
        self.yid.append(y)
        
    def ymbermoot(self):
        pyth = 0
        for nr in range(len(self.xid)):
            dx = self.xid[(nr+1) % len(self.xid)] - self.xid[nr]
            dy = self.yid[(nr+1) % len(self.yid)] - self.yid[nr]
            pyth += math.sqrt(dx*dx + dy*dy)
        return pyth

    def __str__(self):
        return ", ".join(["("+str(paar[0])+ ", "+str(paar[1])+")"for paar in zip(self.xid, self.yid)])
    
    def tekstiks(self):
        vastus=""
        for nr in range(len(self.xid)):
            vastus+=" ("+str(self.xid[nr])+", "+str(self.yid[nr])+")"
        return vastus
    
    def nihuta(self, dx, dy):
        for i in range(len(self.xid)):
            self.xid[i] += dx
            self.yid[i] += dy
    
    def size(self, tegur):
        for i in range(len(self.xid)):
            self.xid[i] *= tegur
            self.yid[i] *= tegur
            
    pilt1=Image.new("RGB", (200, 200))
    g=imageDraw.ImageDraw(Pilt1)
    g.rectangle((10, 10, 30, 20))
    g.line((40, 10, 40, 20))
    g.ellipse((10, 30, 30, 40))
    g.text((40, 30), "tere")
    pilt1.save("pilt1.gif", "GIF")

print("Kolmnurga andmed")
k1= Kolmnurk(1, 3, 2, 4, 3, 5)
print(k1.xid, k1.yid)
k2= Kolmnurk(11, 12, 13, 14, 8, 9)
print (k2)
print(k2.xid, k2.yid)
print(list(zip(k2.xid, k2.yid)))
print(k2.tekstiks())

print(" ")

print("Hulknurga andmed")
h = Hulknurk(1, 3, 2, 0, 3, 5)
print(h)
print(h.ymbermoot())
h.lisa_punkt(4, 6)
print(h)

print(h.ymbermoot())

h.nihuta(2, 3)
print(h)

h.size(2)
print(h)
