#! /usr/bin/python3

import os
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy import special                                                                                                   

print(plt.style.available)

GRAPHICS_DIR = './figures'
os.makedirs(GRAPHICS_DIR, exist_ok=True)

for i in plt.style.available:
	
	mpl.rcParams.update(mpl.rcParamsDefault)

	# first select the style sheet
	plt.style.use(i)

	# create a new figure
	fig = plt.figure()

	ax1 = plt.subplot(111)

	x = np.linspace(0, 6 * np.pi, 100)

	for y in range(6):
		ax1.plot(
		    x,
		    special.jv(y, x),
		    label=r'$J_{} \left( x \right)$'.format(y)
		    )

	# put a label on the y axis
	ax1.set_ylabel(r'Function')
	ax1.set_xlabel(r'Input $x$')

	ax1.legend(ncol=2)

	# fig.tight_layout(pad=.1)
	fig.savefig(GRAPHICS_DIR + '/style_%s.png'%(i))

	# clear figure
	fig.clf()
