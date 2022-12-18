import csv

words = []
with open('wordlist.csv') as f:
    data = csv.reader(f)
    for row in data:
        words.extend(row)


