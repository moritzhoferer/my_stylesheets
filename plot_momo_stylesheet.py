#! /usr/bin/python3

import os
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from scipy import special                                                                                                   

# first select the style sheet
plt.style.use(['momo','wob'])

GRAPHICS_DIR = './figures'
os.makedirs(GRAPHICS_DIR, exist_ok=True)

# create a new figure
fig = plt.figure()

ax1 = plt.subplot(111)

x = np.linspace(0, 6 * np.pi, 100)

for y in range(6):
	ax1 = plt.plot(
	    x,
	    special.jv(y, x),
	    label=r'$J_{} \left( x \right)$'.format(y)
	    )

# put a label on the y axis
plt.ylabel(r'Function')
plt.xlabel(r'Input $x$')

plt.legend(ncol=2)

# fig.tight_layout(pad=.2)
fig.savefig(GRAPHICS_DIR + '/pdf_sizes.pdf')

# clear figure
plt.clf()
