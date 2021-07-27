#! /usr/bin/python3

from pylab import *
from scipy import special                                                                                                   

print(style.available)

for i in style.available:
	
	rcParams.update(rcParamsDefault)

	# first select the style sheet
	style.use(i)

	# create a new figure
	fig = figure()


	ax1 = subplot(111)

	x = linspace(0, 6 * pi, 100)

	for y in range(6):
		ax1.plot(
		    x,
		    special.jv(y, x),
		    label=r'$J_{} \left( x \right)$'.format(y)
		    )

	# put a label on the y axis
	ax1.set_ylabel(r'Function')
	ax1.set_xlabel(r'Input $x$')

	# adjust the scale of the axis
	#xscale('log')
	#yscale('log')

	# adjust the showed ranges
	# ax1.set_ylim( , )

	ax1.legend(ncol=2)

	# fig.tight_layout(pad=.1)


	fig.savefig(
	    'style_%s.png'%(i)
	)

	# clear figure
	fig.clf()
