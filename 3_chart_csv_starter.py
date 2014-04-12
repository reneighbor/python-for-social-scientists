import csv
import collections
import matplotlib.pyplot as plt
import numpy

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


	# erase this after extractData() is complete
	finland_data = [70, 35, 30, 20, 40]
	el_salvador_data = [70, 35, 30, 20, 40]
	usa_data = [70, 35, 30, 20, 40]

	fig = plt.figure()
	ax = fig.add_subplot(111)

	finland_index = numpy.arange(len(finland_data))
	width = 0.35

	rects_finland = ax.bar(finland_index, finland_data, width, color="r")
	rects_el_salvador = ax.bar(finland_index+width, el_salvador_data, width, color="g")
	rects_usa = ax.bar(finland_index+2*width, usa_data, width, color="y")

	ax.legend( (rects_finland[0], rects_el_salvador[0], rects_usa[0]), ('Finland', 'El Salvador', 'United States') )

	plt.show()

	return


def extractData(row):

	data = {}

	for key, value in row.iteritems():
		# Fill this in
		data[key] = "FOO"
	
	return collections.OrderedDict(sorted(data.items()))


main()

