#Svakhet ved gjennomsnittlig sidetall: Inkluderer bøker på 0 sider og bøker som inneholder flere volum av samme serie
import csv
import matplotlib.pyplot as plt

with open('books.csv', 'r', encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)
    data = list(reader)

pagecount = 0
skipped = 0

for book in data:
    try:
        pagecount += int(book[7])
    except ValueError:
        skipped += 1

averagePagecount = int(pagecount/(len(data)-skipped))
print(f"Gjennomsnittlig sidetall: {averagePagecount}")

pageCounts = {
    "zeroToTen": 0, "tenToHundred": 0, "HundredToTwo": 0, "TwoToThree": 0,
    "ThreeToFour": 0, "FourToFive": 0, "FiveToSix": 0, "SixToSeven": 0,
    "SevenToEight": 0, "EightToNine": 0, "NineToK": 0, "ThousandPlus": 0
}

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
    
for book in data:
    try:
        pages = int(book[7])
        category = findCategory(pages)
        pageCounts[category] += 1
    except ValueError:
        pass

names = ["0-10", "10-100", "100-200", "200-300", "300-400", "400-500", "500-600", "600-700", "700-800", "800-900", "900-1000", "1000+"]
values = [pageCounts["zeroToTen"], pageCounts["tenToHundred"], pageCounts["HundredToTwo"], pageCounts["TwoToThree"], pageCounts["ThreeToFour"], pageCounts["FourToFive"], pageCounts["FiveToSix"], pageCounts["SixToSeven"], pageCounts["SevenToEight"], pageCounts["EightToNine"], pageCounts["NineToK"], pageCounts["ThousandPlus"]]

plt.figure()
plt.bar(names, values)
plt.xlabel("Sidetall")
plt.ylabel("Bøker")
plt.title("Bøker fordelt etter sidetall")
plt.show()