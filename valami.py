menuf=open("menu.csv")                     #a "menuf" a menu fájlt jelenti, maga a fájl, akármi művelet nélkül, hogy lehessen bele írni.
menul=menuf.read().split("\n")             #a "menul" a menu listát jelenti, használatra szétválasztva elemekre, hogy ne használat közben kelljen.
for i in range(len(menul)):
    menul[i]=menul[i].split(";")

asztalf=open("asztal.csv", "r+")
asztall=asztalf.read().split("\n")
for i in range(len(asztall)):
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

class Vasarlas:
    def __init__(self,termekek):
        """
        termekek (list):
            A vásárolni kivánt termékek, a .hozzaad() művelettel lehet módositani.
        """
        self.termekek=list(termekek)
    def hozzaad(self,mit):
        """
        mit (str):
            EGY termék neve, amit a vásárlásba be akarunk tenni
        """
        self.termekek.append(mit)
mode=0
##0: fo"menu"
##1: e'telek
##2: rakta'r
##3: rendele's
##4: e'tlap
##5: receptek
while 1==1:
    if mode==0:
        choose=int(input("0;etelek\n1;raktar\n2;rendeles\nirja be a kivánt művelet melletti számot!\n>"))
        if choose==0:
            mode=1
        if choose==1:
            mode=2
        if choose==2:
            mode=3
        print(choose,mode)
    if mode==1:
        for i in range(len(receptekl)):
            print(f"{i};{receptekl[i][0]}")
        print(f"{i+1};új")
        print("irja be a módositani kivánt étel számát!")
        etel=int(input(">"))

        print(f"{receptekl[etel][0]}\nhozzávalók:")
        for i in receptekl[etel][1:]:
            print(i,end=" ")
        
        print(f"\nár: {menul[etel][1]}.-")
    if mode==2:
        print("raktár")
    if mode==3:
        print("rendelés")
    if mode==4:
        print("étlap")
    if mode==5:
        print("receptek")