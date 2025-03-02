import csv
import matplotlib.pyplot as plt
from collections import Counter
import json

with open('books_1.Best_Books_Ever.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)
    data = list(reader)

totalPages = 0
booksSkipped = 0

#Burde utvides for å ekskludere lydbøker o.l.
for book in data:
    try:
        totalPages += int(book[12])
    except ValueError:
        booksSkipped += 1

averagePagecount = int(totalPages/(len(data)-booksSkipped))
print(f"Gjennomsnittlig sidetall: {averagePagecount}", "\n")


#Samler antall bøker for hver mengde sider i en ordbok
pageCounts = {
    "zeroToTen": 0, "tenToHundred": 0, "HundredToTwo": 0, "TwoToThree": 0,
    "ThreeToFour": 0, "FourToFive": 0, "FiveToSix": 0, "SixToSeven": 0,
    "SevenToEight": 0, "EightToNine": 0, "NineToK": 0, "ThousandPlus": 0
}

#Bestemmer hvilken kategori med sidetall en bok tilhører
def findCategory(pages):
    if pages <= 10:
        return "zeroToTen"
    elif pages <= 100:
        return "tenToHundred"
    elif pages <= 200:
        return "HundredToTwo"
    elif pages <= 300:
        return "TwoToThree"
    elif pages <= 400:
        return "ThreeToFour"
    elif pages <= 500:
        return "FourToFive"
    elif pages <= 600:
        return "FiveToSix"
    elif pages <= 700:
        return "SixToSeven"
    elif pages <= 800:
        return "SevenToEight"
    elif pages <= 900:
        return "EightToNine"
    elif pages <= 1000:
        return "NineToK"
    else:
        return "ThousandPlus"
    
#Sorterer alle bøkene i datasettet inn i ordboken med findCategory funksjonen
for book in data:
    try:
        pages = int(book[12])
        category = findCategory(pages)
        pageCounts[category] += 1
    except ValueError:
        pass

names = ["0-10", "10-100", "100-200", "200-300", "300-400", "400-500", "500-600", "600-700", "700-800", "800-900", "900-1000", "1000+"]
values = [pageCounts["zeroToTen"], pageCounts["tenToHundred"], pageCounts["HundredToTwo"], pageCounts["TwoToThree"], pageCounts["ThreeToFour"], pageCounts["FourToFive"], pageCounts["FiveToSix"], pageCounts["SixToSeven"], pageCounts["SevenToEight"], pageCounts["EightToNine"], pageCounts["NineToK"], pageCounts["ThousandPlus"]]

#Legg in prosent på y aksen til høyre?
plt.figure(figsize=(12,5))
plt.bar(names, values)
plt.xlabel("Sider")
plt.ylabel("Bøker")
plt.title("Bøker fordelt etter antall sider")

#Forhold mellom ratings og num ratings
x = []
y = []

for book in data:
    try:
        float(book[4])
        float(book[17])
    except ValueError:
        continue
    #Jeg har begrenset figuren til å bare inkludere bøker med mindre enn 1 million ratings, fordi størsteparten av figuren blir en liten klump hvis man inkludererer de med mer. 
    #Det vil kanskje være akuelt å kutte dette ned enda mer, f.eks. til 0.5 millioner, for å bedre kunne se forholdet. 
    if float(book[17]) < 1000000:
        x.append(float(book[4]))
        y.append(float(book[17]))

plt.figure()
plt.scatter(x, y, s=5, alpha=0.2)
plt.ylabel("Antall ratings i millioner")
plt.xlabel("Rating i stjerner")
plt.title("Forhold mellom antall ratings og gjennomsnittlig rating")


sjangre = []

#fordi sjangre i datasettet er formattert "'xxxx', 'xxxxx', 'xxxx'", må jeg først gjøre dette om til lister jeg kan telle meg gjennom

for book in data:
    sjanger = book[8]

    if sjanger.strip(): #Sjekker at boken har sjangre
        formattertsjanger = sjanger.replace("'", '"') #Bytter ut apostrofer med hermetegn
        sjangre.append(json.loads(formattertsjanger)) 

flat_sjangre = [genre for sublist in sjangre for genre in sublist] #Sjangre er nå en liste av lister, dette gjør den om til én stor liste.

#Bruker det counter fra det innebygde biblioteket collections, som har funksjonalitet for å telle forekomster i en liste
#Jeg kunne alternativt gått gjennom listen og lagt til i en ordbok, for så å sortere etter høyeste forekomst
forekomst = Counter(flat_sjangre)
top10 = forekomst.most_common(10) #Most common er også fra collections, og erstatter manuell sortering

print("Sjanger           ", "Forekomst","\n")
for sjanger, forekomst in top10:
    print(f"{sjanger:20} {forekomst}") #Setter av 20 karakterer til sjanger, slik at output ser bedre ut


språk = {}

for book in data: 
    language = book[6]
    if language in språk.keys():
        språk[language] += 1
    else:
        språk[language] = 1

del språk["English"], språk[""] #Sletter språk og verdi for engelsk og bøker uten spesifisert språk. Engelsk fordi det er mer interessant å se på hvilke ikke-engelske bøker som er på listen.

språkliste = list(språk.items())
#Bruker sorted funksjonen for å sortere dem etter forekomst, slik at kakediagram ser ryddig ut.
#Jeg kunne evt. gjort noe mer manuelt enn å bruke sorted-funksjonen, ved å skrive en egen sorteringsalgoritme
sortert = sorted(språkliste, key=lambda x: x[1], reverse=True) 


#Sorterer språk og forekomst inn i lister jeg kan bruke til å lage kakediagrammet
data = []
labels = []

for pairs in sortert:
    labels.append(pairs[0])
    data.append(pairs[1])

labels[10:] = [""]*len(labels[10:]) #Fjerner navn på språk etter de 10 største, slik at navnene ikke overlapper i diagrammet.
plt.figure(figsize=(7,7))
plt.title("De mest vanlige språkene, ekskludert engelsk")
plt.pie(data, labels=labels)
plt.show()  
