import os
import gpxpy
import gpxpy.gpx

import matplotlib
import matplotlib.pyplot as plt

cwd = os.getcwd()
data_dir = os.path.join(cwd, 'data')

kmlfile = open('progress.kml', 'w')
kmlfile.write('<?xml version="1.0" encoding="UTF-8"?>\n<kml xmlns="http://www.opengis.net/kml/2.2">\n<Document>')
kmlfile.write('<Style id="purpleLine">\n<LineStyle>\n<color>50781E78</color>\n<width>5</width>\n</LineStyle>\n<PolyStyle>\n<color>7f00ff00</color>\n</PolyStyle>\n</Style>')
for f in os.listdir(data_dir):
    if f.endswith('.gpx'):

        gpx_f = os.path.join(data_dir, f)
        
        with open(gpx_f) as gpx_file:

            print gpx_f
            
            gpx_data = gpxpy.parse(gpx_file)
            #if not gpx_data.tracks[0].name.find('Running') == -1:
            kmlfile.write('<Placemark>\n<styleUrl>#purpleLine</styleUrl>\n<LineString>\n<coordinates>')
            points = gpx_data.get_points_data()
            x = [p.point.latitude for p in points if p.point.latitude < 51.7 and p.point.latitude > 51.4 and p.point.longitude < -3 and p.point.longitude > -3.4]
            y = [p.point.longitude for p in points if p.point.latitude < 51.7 and p.point.latitude > 51.4 and p.point.longitude < -3 and p.point.longitude > -3.4]
            z = [p.point.elevation for p in points if p.point.latitude < 51.7 and p.point.latitude > 51.4 and p.point.longitude < -3 and p.point.longitude > -3.4]
            for p in points:
                kmlfile.write('%.8f,%.8f\n' % (p.point.longitude, p.point.latitude))
            kmlfile.write('</coordinates>\n</LineString>\n</Placemark>')

kmlfile.write('</Document></kml>')
kmlfile.close()