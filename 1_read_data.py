import csv

csvfile = open('data/childhood_deaths.csv', 'rU')
reader = csv.DictReader(csvfile)

for row in reader:
    print row