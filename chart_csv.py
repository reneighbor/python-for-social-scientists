import csv
import matplotlib.pyplot as plt
import numpy


def main():

	csvfile = open('data/cellphones.csv', 'rU')

	reader = csv.DictReader(csvfile)


	for row in reader:

		if row['Country Name'] == 'Finland':
			finland_data = extractData(row)


	# overriding the results of extractData() for now
	finland_data = [50, 35, 30, 35, 27]


	fig = plt.figure()
	ax = fig.add_subplot(111)

	finland_index = numpy.arange(len(finland_data))
	width = 0.35

	rects_finland = ax.bar(finland_index, finland_data, width, color="r")
	# rects_saudi_arabia = ax.bar(finland_index+width, saudi_arabia_data.values(), width, color="g")
	# rects_usa = ax.bar(finland_index+2*width, usa_data.values(), width, color="y")

	# ax.legend( (rects_finland[0], rects_saudi_arabia[0], rects_usa[0]), ('Finland', 'United States', 'Saudi Arabia') )

	plt.show()

	return


# Fill this in
def extractData(row):
	data = {}

	for key, value in row.iteritems():
		data[key] = "FOO"
		
	return data


main()

