import csv
import matplotlib.pyplot as plt

with open('books_1.Best_Books_Ever.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)
    data = list(reader)

print(len(data))
