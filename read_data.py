import csv

csvfile = open('data/cellphones.csv', 'rU')
reader = csv.DictReader(csvfile)

for row in reader:
    if row['Country Name'] == "Finland":
        print row