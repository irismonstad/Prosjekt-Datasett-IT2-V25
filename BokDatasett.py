import csv

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

averagePagecount = float(pagecount/(len(data)-skipped))
print(averagePagecount)
