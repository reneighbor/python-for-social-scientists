import matplotlib.pyplot as plt
import numpy


finland_data = [40, 35, 30, 35, 27]


finland_index = numpy.arange(len(finland))

fig = plt.figure()
ax = fig.add_subplot(111)


width = 0.35

rects_finland = ax.bar(finland_index, finland, width, color="r")
# rects_saudi_arabia = ax.bar(finland_index+width, saudi_arabia_data, width, color="g")
# rects_usa = ax.bar(finland_index+2*width, usa_data, width, color="y")

ax.legend((rects_finland[0], rects_saudi_arabia[0], rects_usa[0]), ('Finland', 'United States', 'Saudi Arabia'))

plt.show()

