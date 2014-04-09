import matplotlib.pyplot as plt
import numpy


finland_data = [50, 35, 30, 35, 27]

finland_index = numpy.arange(len(finland_data))

fig = plt.figure()
ax = fig.add_subplot(111)


width = 0.35

rects_finland = ax.bar(finland_index, finland_data, width)
# rects_el_salvador = ax.bar(finland_index+width, el_salvador_data, width, color="g")
# rects_usa = ax.bar(finland_index+2*width, usa_data, width, color="y")

# ax.legend((rects_finland[0], rects_el_salvador[0], rects_usa[0]), ('Finland', 'United States', 'El Salvador'))

plt.show()

