#!/usr/bin/python3
# -*- coding: utf-8 -*-
#!/home/cendas/miniconda3/envs/DataEnv/bin/python3
#=========================# Required libraries ===========================================================
import sys # Import the "system specific parameters and functions" module
import matplotlib

import matplotlib.pyplot as plt # Import the Matplotlib package
from mpl_toolkits.basemap import Basemap # Import the Basemap toolkit&amp;amp;amp;amp;lt;/pre&amp;amp;amp;amp;gt;
import numpy as np # Import the Numpy package
from numpy.ma import masked_array
from remap import remap # Import the Remap function

from cpt_convert import loadCPT # Import the CPT convert function
from matplotlib.colors import LinearSegmentedColormap # Linear interpolation for color maps

import datetime # Library to convert julian day to dd-mm-yyyy
import time 

from matplotlib.patches import Rectangle # Library to draw rectangles on the plot
from osgeo import gdal # Add the GDAL library

matplotlib.use('Agg') # use a non-interactive backend
from netCDF4 import Dataset # Import the NetCDF Python interface
#======================================================================================================

# Load the Data =======================================================================================
# Path to the GOES-16 image file
#pathCH1 = sys.argv[1]
#pathCH2 = sys.argv[2]
#pathCH3 = sys.argv[3]
pathCH1 = '/home/cendas/PythonTest/OR_ABI-L2-CMIPF-M6C01_G16_s20200711300179_e20200711309487_c20200711309562.nc'
pathCH2 = '/home/cendas/PythonTest/OR_ABI-L2-CMIPF-M6C02_G16_s20200711300179_e20200711309487_c20200711309564.nc'
pathCH3 = '/home/cendas/PythonTest/OR_ABI-L2-CMIPF-M6C03_G16_s20200711300179_e20200711309487_c20200711309564.nc'
# Open the file using the NetCDF4 library
nc = Dataset(pathCH2)#Usar como parametro o canal2

# Get the latitude and longitude image bounds
geo_extent = nc.variables['geospatial_lat_lon_extent']
min_lon = float(geo_extent.geospatial_westbound_longitude)
max_lon = float(geo_extent.geospatial_eastbound_longitude)
min_lat = float(geo_extent.geospatial_southbound_latitude)
max_lat = float(geo_extent.geospatial_northbound_latitude)

# Choose the visualization extent (min lon, min lat, max lon, max lat)

# Rio de Janeiro as a Center of the projection
extent = [-50, -30.0, -35.0, -15.0]


# Choose the image resolution (the higher the number the faster the processing is)
resolution = 2 
# Calculate the image extent required for the reprojection
H = nc.variables['goes_imager_projection'].perspective_point_height
x1 = nc.variables['x_image_bounds'][0] * H 
x2 = nc.variables['x_image_bounds'][1] * H 
y1 = nc.variables['y_image_bounds'][1] * H 
y2 = nc.variables['y_image_bounds'][0] * H 
# Call the reprojection funcion
gridCH1 = remap(pathCH1, extent, resolution,  x1, y1, x2, y2)
gridCH2 = remap(pathCH2, extent, resolution,  x1, y1, x2, y2)
gridCH3 = remap(pathCH3, extent, resolution,  x1, y1, x2, y2)

# Read the data returned by the function
R = gridCH2.ReadAsArray()
G = gridCH3.ReadAsArray()
B = gridCH1.ReadAsArray()

# Apply range limits for each channel. RGB values must be between 0 and 1
R = np.clip(R, 0, 1)
G = np.clip(G, 0, 1)
B = np.clip(B, 0, 1)
# Apply the gamma correction
gamma = 2.2
R = np.power(R, 1/gamma)
G = np.power(G, 1/gamma)
B = np.power(B, 1/gamma)
# Calculate the "True" Green
G_true = 0.45 * R + 0.1 * G + 0.45 * B
G_true = np.clip(G_true, 0, 1)
# The final RGB array :)
RGB = np.dstack([R, G_true, B])
#====================================

# Define the size of the saved picture=================================================================
DPI = 150
fig = plt.figure(figsize=(R.shape[1]/float(DPI), R.shape[0]/float(DPI)), frameon=False, dpi=DPI)

ax = plt.Axes(fig, [0., 0., 1., 1.])
ax.set_axis_off()
fig.add_axes(ax)
ax = plt.axis('off')
#======================================================================================================

# Plot the Data =======================================================================================

# Create the basemap reference for the Rectangular Projection
bmap = Basemap(llcrnrlon=extent[0], llcrnrlat=extent[1], urcrnrlon=extent[2], urcrnrlat=extent[3], epsg=4326)

# Draw the countries and Brazilian states shapefiles
bmap.readshapefile('/home/cendas/GOES16-Files/CodeProcess/Shapefiles/BRA_adm1','BRA_adm1',linewidth=0.50,color='#000000')
#bmap.readshapefile('/home/cendas/GOES16-Files/CodeProcess/Shapefiles/ne_10m_coastline','ne_10m_0_coastline',linewidth=0.50,color='#000000')

# Draw parallels and meridians
bmap.drawparallels(np.arange(-90.0, 90.0, 5), linewidth=0.3, dashes=[4, 4], color='white', labels=[True,False,False,True], fmt='%g', labelstyle="+/-", size=10)
bmap.drawmeridians(np.arange(0.0, 360.0, 5), linewidth=0.3, dashes=[4, 4], color='white', labels=[True,False,False,True], fmt='%g', labelstyle="+/-", size=10)

bmap.imshow(RGB, origin='upper')


logo_Lamce = plt.imread("/home/cendas/GOES16-Files/CodeProcess/Logos/logo_lamce_RJ.png")
logo_Baia = plt.imread("/home/cendas/GOES16-Files/CodeProcess/Logos/baia_logo_RJ.png")


plt.figimage(logo_Lamce,  1300, 60, zorder=3, alpha = 1, origin = 'upper') 
plt.figimage(logo_Baia, 120, 60, zorder=3, alpha = 1, origin = 'upper')


# Save the result as a PNG
plt.savefig('/home/cendas/GOES16-Files/CodeProcess/PythonScripts/TrueColor.tif', dpi=DPI, pad_inches=0, transparent=True)
plt.close()
 
# Add to the log file (called "G16_Log.txt") the NetCDF file name that I just processed.

# If the file doesn't exists, it will create one.
#with open('/home/cendas/GOES16-Files/Output/RJ/G16_Log.txt', 'a') as log:
# log.write(path.replace('\\\\', '\\') + '\n')
#======================================================================================================

# Export the result to GeoTIFF
#driver = gdal.GetDriverByName('GTiff')
#driver.CreateCopy('/home/cendas/GOES16-Files/Output/RJ/ProjectionsGEOTIF/CH'+str(Band)+'/RJ_G16_C' + str(Band) + '_' + date + '_' + time_saved+'.tif', grid, 0)
#======================================================================================================
