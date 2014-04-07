import csv
import matplotlib.pyplot as plt
import numpy

csvfile = open('data/cellphones.csv', 'rU')

reader = csv.DictReader(csvfile)



def extractData(row):
	data = {}
	for key, value in row.iteritems():
		if not key.isdigit():
			continue
		if int(key) not in range(1960, 2013):
			continue
		if value is '':
			value = 0
		data[int(key)] = float(value)

		
	return data




for row in reader:

	if row['Country Name'] == 'Finland':
		finland_data = extractData(row)
	if row['Country Name'] == 'Saudi Arabia':
		saudi_arabia_data = extractData(row)
	if row['Country Name'] == 'United States':
		usa_data = extractData(row)



fig = plt.figure()
ax = fig.add_subplot(111)

finland_index = numpy.arange(len(finland_data))
width = 0.35

rects_finland = ax.bar(finland_index, finland_data.values(), width, color="r")
rects_saudi_arabia = ax.bar(finland_index+width, saudi_arabia_data.values(), width, color="g")
rects_usa = ax.bar(finland_index+2*width, usa_data.values(), width, color="y")

ax.legend( (rects_finland[0], rects_saudi_arabia[0], rects_usa[0]), ('Finland', 'United States', 'Saudi Arabia') )

plt.show()

