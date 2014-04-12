import csv
import matplotlib.pyplot as plt
import numpy
from collections import OrderedDict


def main():

	csvfile = open('data/childhood_deaths.csv', 'rU')
	reader = csv.DictReader(csvfile)

	csvfile2 = open('data/fertility.csv', 'rU')
	reader2 = csv.DictReader(csvfile2)

	compareIndicators(reader, reader2, "El Salvador")

	return

def compareIndicators(reader1, reader2, country_name):

	for row in reader1:
		if row['Country Name'] == country_name:
			data1 = extractData(row)

	for row in reader2:
		if row['Country Name'] == country_name:
			data2 = extractData(row)

	fig = plt.figure()
	ax = fig.add_subplot(111, xlabel="Year")

	index = numpy.arange(len(data1))
	width = 0.35

	series1 = ax.bar(index, data1.values(), width, color="r")
	series2 = ax.bar(index+width, data2.values(), width, color="y")

	ax.set_xticklabels(range(1960, 2013), rotation="vertical")
	ax.set_xticks(index+width)

	ax.legend( (series1[0], series2[0]), ("Mortality rate, under-5 (per 1,000 live births)", "Births per woman"))
	plt.show()

	return


def compareCountries(reader, country_name1, country_name2 = None, country_name3 = None): 

	for row in reader:

		if row['Country Name'] == country_name1:
			data1 = extractData(row)
		if row['Country Name'] == country_name2:
			data2 = extractData(row)
		if row['Country Name'] == country_name3:
			data3 = extractData(row)

	fig = plt.figure()
	ax = fig.add_subplot(111)

	index = numpy.arange(len(data1))
	width = 0.35

	series1 = ax.bar(index, data1.values(), width, color="r")
	series2 = ax.bar(index+width, data2.values(), width, color="y")
	series3 = ax.bar(index+2*width, data3.values(), width)

	ax.legend( (series1[0], series2[0], series3[0]), (country_name1, country_name2, country_name3))
	ax.set_xticklabels(range(1960, 2013), rotation="vertical")
	ax.set_xticks(index+width)

	plt.show()

	return


## Returns data as years-to-values only, stripping out country name, acronym, etc

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

		
	return OrderedDict(sorted(data.items()))
 

main()
