import numpy as np
import pyfits
import astropy
import matplotlib.pylab as plt

import numpy as np
import matplotlib.pylab as plt
from matplotlib.gridspec import GridSpec
from matplotlib.ticker import MaxNLocator
from matplotlib.ticker import ScalarFormatter
import matplotlib.ticker as ticker
import pyfits
import sys
sys.path.append("/usr/local/bin/")

import matplotlib
matplotlib.rcParams['axes.linewidth'] = 0.5
from astropy.io import fits






galaxy = "PTF11qnr"
data = pyfits.getdata("../MUSE/AMUSING_dataproducts/%s.SSP.cube.fits.gz"%galaxy)
tessela = data[1]
V = np.log10(data[0])

tessela[tessela == 0] = np.nan


fig=plt.figure(figsize=(4,2))
grid = plt.GridSpec(1, 2, top=0.999,right=0.995,left=0.1, bottom = 0.2)
ax = fig.add_subplot(grid[0,0])
ax1 = fig.add_subplot(grid[0,1])





ax.imshow(V,origin = "l",vmin = -3.5, vmax = -0.8, cmap = "binary", aspect = "auto")
ax1.imshow(tessela,origin = "l", cmap = "gist_earth", aspect = "auto")



ax.set_xlabel("pixels", fontsize=8)#,labelpad = 0)
ax.set_ylabel("pixels", fontsize=8)#,labelpad = 0)
plt.setp(ax.get_yticklabels(), rotation='vertical', fontsize=8)
plt.setp(ax.get_xticklabels(), fontsize=8)



ax1.set_xlabel("pixels", fontsize=8)#,labelpad = 0)
plt.setp(ax1.get_yticklabels(), rotation='vertical', fontsize=8)
plt.setp(ax1.get_xticklabels(), fontsize=8)


#plt.grid(True,color="w")
ax.set_facecolor('#e8ebf2')
ax1.set_facecolor('#e8ebf2')
plt.tight_layout()
plt.savefig("./figures/tessela.pdf")
#plt.show()
