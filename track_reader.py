import os
import gpxpy
import gpxpy.gpx

import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

cwd = os.getcwd()
data_dir = os.path.join(cwd, 'data')

m = Basemap(projection='merc', lat_0=51.475, lon_0=-3.17, resolution='f', llcrnrlon=-3.275, llcrnrlat=51.43, urcrnrlon=-3.125, urcrnrlat=51.51)
m.drawcoastlines()
m.drawcountries()
m.fillcontinents(color='gray')
m.drawmapboundary()

kmlfile = open('progress.kml', 'w')
kmlfile.write('<?xml version="1.0" encoding="UTF-8"?>\n<kml xmlns="http://www.opengis.net/kml/2.2">\n<Document>')
kmlfile.write('<Style id="yellowLineGreenPoly">\n<LineStyle>\n<color>7f00ffff</color>\n<width>1</width>\n</LineStyle>\n<PolyStyle>\n<color>7f00ff00</color>\n</PolyStyle>\n</Style>')
for f in os.listdir(data_dir):
    if f.endswith('.gpx'):

        gpx_f = os.path.join(data_dir, f)
        
        with open(gpx_f) as gpx_file:
            
            gpx_data = gpxpy.parse(gpx_file)
            #if not gpx_data.tracks[0].name.find('Running') == -1:
            kmlfile.write('<Placemark>\n<styleUrl>#yellowLineGreenPoly</styleUrl>\n<LineString>\n<coordinates>')
            points = gpx_data.get_points_data()
            x = [p.point.latitude for p in points if p.point.latitude < 51.7 and p.point.latitude > 51.4 and p.point.longitude < -3 and p.point.longitude > -3.4]
            y = [p.point.longitude for p in points if p.point.latitude < 51.7 and p.point.latitude > 51.4 and p.point.longitude < -3 and p.point.longitude > -3.4]
            z = [p.point.elevation for p in points if p.point.latitude < 51.7 and p.point.latitude > 51.4 and p.point.longitude < -3 and p.point.longitude > -3.4]
            for p in points:
                kmlfile.write('%.8f,%.8f\n' % (p.point.longitude, p.point.latitude))
            x,y = m(x, y)
            m.plot(x,y)

            kmlfile.write('</coordinates>\n</LineString>\n</Placemark>')

kmlfile.write('</Document></kml>')
kmlfile.close()

plt.show()


