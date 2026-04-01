menuf=open("menu.csv", "r+")               #a "menuf" a menu fájlt jelenti, maga a fájl, akármi művelet nélkül, hogy lehessen bele írni.
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
    raktars.update({i.split(";")[0]:int(i.split(";")[1])})

class UjEtel:
    def __init__(self):
        pass
mode=0
##0: fo"menu"
##1: e'telek
##2: rakta'r
##3: rendele's
##4: e'tlap
##5: receptek
rendeles=[]
while True:
    if mode==0: ##főmenü
        choose=int(input("0;etelek\n1;raktar\n2;rendeles\n3;asztalok\nirja be a kivánt művelet melletti számot!\n>"))
        if choose==0:
            mode=1
        if choose==1:
            mode=2
        if choose==2:
            mode=3
        if choose==3:
            mode=4
        print(choose,mode)
    if mode==1: ##ételek
        for i in range(len(receptekl)):
            print(f"{i};{receptekl[i][0]}")
        print(f"{i+1};új")
        print("irja be a módositani kivánt étel számát!")
        try:
            etel=int(input(">"))
            print(f"{receptekl[etel][0]}\nhozzávalók:")
            for i in receptekl[etel][1:]:
                print(i,end=" ")
            print(f"\nár: {menul[etel][1]}.-")
            berakjae=str(input("Be akarja tenni a rendelésbe?(y=igen/n=nem)\n>"))
            if berakjae=="y":
                rendeles.append(etel)
            else:
                mode=0
        except IndexError:
            uj=UjEtel
            uj.nev=(str(input("Mi legyen a neve? (kisbetűvel, egyben)")))
            uj.ar=(int(input("Mennyibe (ft) kerüljön?")))
            dict={}
            inputstr="a"
            intput=0
            print("Adja meg az étel hozzávalóit és mennyiségeit! Ha készen van, adjon névnek üreset!")
            while inputstr!="":
                dict.update({inputstr:intput})
                inputstr=""
                inputstr=input("Hozzávaló neve:\n>")
                if inputstr!="":
                    intput=int(input("Hozzávaló darabszáma:\n>"))
            dict.pop("a")
            dictstr=str(dict)
            dictstr=dictstr.replace("{","")
            dictstr=dictstr.replace("}","")
            dictstr=dictstr.replace("'","")
            dictstr=dictstr.replace(":","-")
            dictstr=dictstr.replace(",",";")
            dictstr=dictstr.replace(" ","")
            recept=f"\n{uj.nev};{dictstr}"
            receptekf.write(recept)
            menu=f"\n{uj.nev};{uj.ar}"
            menuf.write(menu)
        mode=0
    if mode==2: ##raktár
        x=0
        print("raktár")
        for i in raktarl:
            print(raktarl[x])
            x += 1
        d=str(input("Miből érkezett: "))
        r=int(input("Mennyi:"))
        raktars[d]+=r
        raktarfuj=str(raktars)
        raktarfuj=raktarfuj.strip("{")
        raktarfuj=raktarfuj.strip("}")
        raktarfuj=raktarfuj.replace(", ","\n")
        raktarfuj=raktarfuj.replace(":",";")
        raktarfuj=raktarfuj.replace("'","")
        raktarfuj=raktarfuj.replace(" ","")
        raktarf=open("raktar.csv", "w+", encoding="utf-8")
        raktarf.write(raktarfuj)
        raktarf.close
        mode=0
    if mode==3: ##rendelés
        for i in vasarlasokl:
            print(f"asztal {i[0]}: ",end="")
            for l in i[1:]:
                print(f"{l} ",end="")
            print("")
        if len(rendeles)!=0:
            rendeles=rendeles
            print("Aktív rendelés: ",end="")
            for i in rendeles:
                print(f"{menul[i][0]} ",end="")
        else:
            print("Aktív rendelés nincs.")
    if mode==4: ##asztalok
        print("asztalok")