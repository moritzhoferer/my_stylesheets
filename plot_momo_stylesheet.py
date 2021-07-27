#! /usr/bin/python

from pylab import *
from scipy import special                                                                                                   

# first select the style sheet
style.use(['momo','wob'])

# create a new figure
fig = figure()


ax1 = subplot(111)

x = linspace(0, 6 * pi, 100)

for y in range(6):
	ax1 = plot(
	    x,
	    special.jv(y, x),
	    label=r'$J_{} \left( x \right)$'.format(y)
	    )

# put a label on the y axis
ylabel(r'Function')
xlabel(r'Input $x$')

# adjust the scale of the axis
#xscale('log')
#yscale('log')

# adjust the showed ranges
# ax1.set_ylim( , )

legend(ncol=2)

#tight_layout(pad=.2)


fig.savefig(
    'pdf_sizes.pdf'
)

# clear figure
clf()
