title: Python for Social Scientists
author:
  name: Renee Chu
  twitter: "@reneighbor"
output: slides.html
controls: true


--

### Prereqs:

* python
* matplotlib
* numpy
* Sublime editor


--
# Python for Social Scientists

## Tutorial, PyCon 2014 Montreal

--
### Survey of programming levels in the audience

--
### Smart non-programmers who want to code

Lazy Sunday reading the New York Times

![Alt Text](images/reading.png)

--
### Advice given to new programmers: 

Pick a project you're passionate about

--
### Your project can be answering question X with data

Girls-to-boys school attendance ratios (primary and secondary)
* United States
* El Salvador
* Pakistan

How do they compare?

--
Girls-to-boys school attendance ratios (primary and secondary)
![Alt Text](images/girls_boys_schooling.png)

--
### Sidenote: Saudi Arabia

Girls-to-boys school attendance ratios (primary and secondary)
![Alt Text](images/girls_boys_saudi.png)

--
### Your project can be answering question X with data

Should development resources be spent on health, or on family planning?

--
### Sometimes data can provide an answer...

--
Childhood deaths, children per woman in El Salvador
![Alt Text](images/el_salvador_births_childhood_deaths.png)

--
Childhood deaths, children per woman in Bangladesh
![Alt Text](images/bangladesh_births_childhood_deaths.png)

--
### Observations aren't always consistent

--
Childhood deaths, children per woman in Nigeria
![Alt Text](images/nigeria_births_childhood_deaths.png)

--
Childhood deaths, children per woman in Estonia
![Alt Text](images/estonia_births_childhood_deaths.png)


--
### Hacking on data is:

* Interesting
* Widely available
* Easier setup than web

--
### Smart non-programmers who *do* code

Lazy Sunday hacking on data

![Alt Text](images/reading.png)

--
### Today:

1. Aquire our data
1. Manipulate it with python
1. Create interesting visualizations


--
# 1. Acquire our data

--
### World Bank Indicators

* Search "World Bank Indicators"

* data.worldbank.org/indicator


--
### World Bank Indicators

* What is one thing you can see from the data?
* Delete non-column rows on the top, save to Desktop
* Save it as "cellphones.csv"

--
# 2. Manipulate it with Python

--
### Follow these steps:
* Make a new folder "python-for-social-scientists"
* Make a new file inside called "read_data.py"
* In the file type:

	
	print "Hello World"

--
### Find your new file in your terminal

* Where is your folder saved?
* Open up terminal:


	cd Projects/personal-projects/programming-for-social-scientists
	python read_data.py

* You should see "Hello World" spit back at you

--
### Follow these steps:

[Erase the print statement]

	import csv

* libraries are imported

--
### Follow these steps:

	import csv

	csvfile = open('cellphones.csv', 'rU')

* open() is a function

--
### Follow these steps:

	import csv

	csvfile = open('cellphones.csv', 'rU')
	reader = csv.DictReader(csvfile)

* DictReader lets you treat the csv file like a dictionary

--
### This is a Python dictionary

	{
		'Country Code': 'FIN', 
		'Country Name': 'Finland', 
		'2007': '114.924474', 
		'2008': '128.4719884',
		'2009': '144.1530224'
	}

--
### Follow these steps:

	import csv

	csvfile = open('cellphones', 'rU')
	reader = csv.DictReader(csvfile)

	for row in reader:
		print row

--
### Follow these steps:

Run it! In your terminal:

	cd Projects/personal-projects/programming-for-social-scientists
	python read_data.py


--
### Follow these steps:

	import csv

	csvfile = open('cellphones', 'rU')
	reader = csv.DictReader(csvfile)

	for row in reader:
		if row['Country Name'] == "Finland":
			print row


--
### Any questions?

--
### What are some things we observe about the output?

--
### What are some things we observe about the output?
* Not sorted
* Data in strings
* Every row

--
# 3. Create interesting visualizations

--
### Find something to copy

http://matplotlib.org/gallery.html


![Alt Text](images/barchart_demo.png)



--
### Examine the code-- What do we know?
http://matplotlib.org/examples/api/barchart_demo.html

--
### Examine the code-- What do we know?

* First half is drawing the rects, second is labels
* Values the list

--
### MatPlotLib Bar chart simplified

* Go to https://github.com/reneighbor/python-for-social-scientists
* Make a new file in your folder, basic_chart.py
* copy the contents of basic_chart.py

--
### In your terminal:

	python basic_chart.py

--
### In your text editor:

How do we get the other countries data?
* In basic_chart.py 2 series, saudi_arabia_data and usa_data
* Uncomment the commented-out lines
* Run it again

--
### Piping in the CSV data

* open chart-csv.py
* What needs to be done in order to extract data?

--
### Piping in the CSV data

What needs to be done in order to extract data?
* Turn data from strings into ints
* Stip out county names
* Sort by year

--
### Give it a try

* Sorted by year
* Values as numbers, not strings
* Years as numbers, not strings
* Values only (list, not a dict)


