import csv
import matplotlib.pyplot as plt
import numpy
import collections

def main():

	csvfile = open('data/childhood_deaths.csv', 'rU')

	reader = csv.DictReader(csvfile)


	for row in reader:

		if row['Country Name'] == 'Finland':
			finland_data = extractData(row)

		elif row['Country Name'] == 'El Salvador':
			el_salvador_data = extractData(row)

		elif row['Country Name'] == 'United States':
			usa_data = extractData(row)

	fig = plt.figure()
	ax = fig.add_subplot(111)

	finland_index = numpy.arange(len(finland_data))
	width = 0.35

	rects_finland = ax.bar(finland_index, finland_data.values(), width, color="r")
	rects_el_salvador = ax.bar(finland_index+width, el_salvador_data.values(), width, color="g")
	rects_usa = ax.bar(finland_index+2*width, usa_data.values(), width, color="y")

	ax.legend( (rects_finland[0], rects_el_salvador[0], rects_usa[0]), ('Finland', 'El Salvador', 'United States') )

	plt.show()

	return


def extractData(row):
	data = {}
	

	for key, value in row.iteritems():
		if len(key.strip()) == 4:
			new_val = 0
			if len(value.strip()) > 0:
				new_val = float(value)

			data[key] = new_val
	
	ordered_row = collections.OrderedDict(sorted(data.items()))

	print ordered_row
	return ordered_row


main()

