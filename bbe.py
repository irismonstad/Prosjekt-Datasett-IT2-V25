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
