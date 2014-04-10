title: Python for Social Scientists
author:
  name: Renee Chu
  twitter: "@reneighbor"
  url: https://www.surveymonkey.com/s/pycon2014_tutorials
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
### My background

* Econ major, liberal arts college
* No coding at school
* Sales and support in tech
* Learning coding through workshops

--
### Advice I received:

Pick a project you're passionate about

Your project can be answering question X with data

--
### Hacking on data is:

* Interesting
* Widely available
* Easier setup than web

--
### Answer some interesting questions:

Should development resources be spent on family planning or fighting disease?

<iframe width="560" height="315" src="http://www.tubechop.com/watch/2507136" frameborder="0" allowfullscreen></iframe>

--
### Answer some interesting questions:

Who has more cellphones per capita:
* Finland
* United States

--
Cellphones per 100 people
![Alt Text](images/finland_us_cellphones.png)

--
### Answer some interesting questions:

Who has more cellphones per capita:
* Finland
* United States
* El Salvador

--
Cellphones per 100 people
![Alt Text](images/el_salvador_finland_us_cellphones.png)

--
### Today we're going to:

1. Import CSV data into Python
2. Find a MatPlotLib example
3. Pipe our CSV data into MatPlotLib


--
# 1. Import CSV data into Python

--
### Get started:

In your folder for personal projects:

git clone https://github.com/reneighbor/python-for-social-scientists.git


--
# What's here?

python_for_social_scientists/
	data/
		fertility.csv
		childhood_deaths.csv
	read_data.py
	chart_csv.py

--
### Where did the data come from?

* Search "World Bank Indicators"

* data.worldbank.org/indicator

--
### Running a dead-simple program

* Open up the folder
* Open up "read_data.py"
* Type:


	print "Hello world"


--
### Find your new file in your terminal

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
# 2. Find a MatPlotLib example

--
### Find something to copy

http://matplotlib.org/gallery.html


![Alt Text](images/barchart_demo.png)

--
### Examine the code-- What do we know?

* First half is drawing the rects, second is labels
* Values the list

--
### Run the sample code

* Create a new file "mens_womens.py" inside python_for_social_scientists
* In your terminal run "python mens_womens.py"
* Do you get the chart?
* Edit the values for "menMeans" and "womensMeans". Do you see a change?

--
### MatPlotLib Bar chart simplified

* Look at basic_chart.py

--
### In your terminal:

	python basic_chart.py

--
### In your text editor:

How do we get the other countries data?
* In basic_chart.py add 2 series, saudi_arabia_data and usa_data
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


--
Break

--
### Share what you've written


--
### Comparing 2 countries
* How would you edit chart_csv to graph multiple countries?

--
### Comparing 2 countries
* run extractData() on 2 other countries
* comment out the rectangle-drawing for those countries

--
### Comparing 2 indicators

What do we need to do to compare mortality against fertility?

--
### Comparing 2 indicators

What do we need to do to compare mortality against fertility?
* Take in 2 CSV readers
* Take in only one country
* rename "rects" to be indicators instead of countries

--
### From Github:

programming_for_social_scientists compare_indicators_starter.py

* Re-arranged to accomediate two comparison-drawing functions and a main()

--
### Give it a try

--
### Share what you've written


--
### What we've done:

* Imported a CSV and turned it into a dict
* Went to MatPlotLib and found a bar chart to borrow
* Drew a series comparing countries from one CSV
* Drew a series comparing indicators from two CSVs

--
### Your Turn

* Pick a data set that interests you. 
* Write code to visualize it. 
* Teach us something!
