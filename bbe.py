import csv
import matplotlib.pyplot as plt

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
print(f"Gjennomsnittlig sidetall: {averagePagecount}")


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
plt.show()


#Forhold mellom ratings og num ratings
x = []
y = []

for book in data:
    try:
        float(book[4])
        float(book[12])
    except ValueError:
        continue
    if float(book[12]) < 1000:
        x.append(float(book[4]))
        y.append(float(book[12]))

plt.figure()
plt.scatter(x, y, s=5, alpha=0.2)
plt.show()

