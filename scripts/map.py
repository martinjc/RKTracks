from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as numpy

m = Basemap(projection='merc', lat_0=51.475, lon_0=-3.17, resolution='f', area_thresh=0.001, llcrnrlon=-3.275, llcrnrlat=51.43, urcrnrlon=-3.125, urcrnrlat=51.51)
m.drawcoastlines()
m.drawcountries()
m.fillcontinents(color='gray')
m.drawmapboundary()

plt.show()