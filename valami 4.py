menuf=open("menu.csv")                     #a "menuf" a menu fájlt jelenti, maga a fájl, akármi művelet nélkül, hogy lehessen bele írni.
menul=menuf.read().split("\n")             #a "menul" a menu listát jelenti, használatra szétválasztva elemekre, hogy ne használat közben kelljen.
for i in range(len(menul)):
    menul[i]=menul[i].split(";")

asztalf=open("asztal.csv", "r+")
asztall=asztalf.read().split("\n")
for i in range(len(menuf)):
    asztall[i]=asztall[i].split(";")

receptekf=open("recept.csv", "r+")
receptekl=receptekf.read().split("\n")
for i in range(len(receptekl)):
    receptekl[i]=receptekl[i].split(";")

vasarlasokf=open("vasarlasok.csv", "r+")
vasarlasokl=vasarlasokf.read().split("\n")
for i in range(len(vasarlasokl)):
    vasarlasokl[i]=vasarlasokl[i].split(";")

raktarf=open("raktar.csv", "r+", encoding="utf-8")
raktarl=raktarf.read().split("\n")          #"raktarl" nem lesz használatban, csak a "raktars" raktar szótár előkészítésére van
raktars={}
for i in raktarl:
    raktars.update({i.split(";")[0]:i.split(";")[1]})

class Termek:
    def __init__(self,sor):
        self.sor=sor
        self.nev=menul[sor][0]
        self.ar=menul[sor][1]

class Recept:
    def __init__(self,sor):
        self.sor=sor
        self.nev=receptekl[sor][0]
        self.hozzavk=receptekl[sor][0:-1]

