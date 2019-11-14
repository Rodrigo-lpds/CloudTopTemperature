# Required libraries ==================================================================================
import numpy as np                                      # Import the Numpy package
from remap import remap                                 # Import the Remap function  
from netCDF4 import Dataset                             # Import the NetCDF Python interface
import datetime # Library to convert julian day to dd-mm-yyyy
import sys # Import the "system specific parameters and functions" module
from pathlib import Path
#======================================================================================================
# Load the Data =======================================================================================
# Path to the GOES-16 image file
path = sys.argv[1]
# Getting information from the file name ==============================================================
# Search for the GOES-16 channel in the file name
bandSetted = False
bands = ['M6C','M3C'] 
bandLenghts = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16']

mode = 0
while not bandSetted: 
    Band = (path[path.find(bands[mode])+3:path.find("_G16")])
    
    if (Band not in bandLenghts):    
        mode +=1  
    else:
        bandSetted = True  
# Search for the Scan start in the file name
Start = (path[path.find("_s")+2:path.find("_e")]) 

# Create a GOES-16 Bands string array
year = int(Start[0:4])
dayjulian = int(Start[4:7]) - 1 # Subtract 1 because the year starts at "0"
dayconventional = datetime.datetime(year,1,1) + datetime.timedelta(dayjulian) # Convert from julian to conventional
date = dayconventional.strftime('%d-%b-%Y') # Format the date according to the strftime directives
timeScan = Start [7:9] + ":" + Start [9:11] + ":" + Start [11:13] + " UTC" # Time of the Start of the Scan
time_saved = timeScan.replace(':','_')


my_file = Path("/home/cendas/GOES16-Files/Output/RJ/GeoJsonTemperature/"+ date + '_' + time_saved + ".geojson")
if my_file.is_file() or int(Band) != 13: 
    pass

else:

    # Open the file using the NetCDF4 library
    nc = Dataset(path)
     
    # Get the latitude and longitude image bounds
    geo_extent = nc.variables['geospatial_lat_lon_extent']
    min_lon = float(geo_extent.geospatial_westbound_longitude)
    max_lon = float(geo_extent.geospatial_eastbound_longitude)
    min_lat = float(geo_extent.geospatial_southbound_latitude)
    max_lat = float(geo_extent.geospatial_northbound_latitude)
     
    # Choose the visualization extent (min lon, min lat, max lon, max lat)
    # Rio de Janeiro
    extent = [-55, -35.0, -30.0, -10.0]
 
     
    # Choose the image resolution (the higher the number the faster the processing is)
    resolution = 2 # Two kilometer 
     
    # Calculate the image extent required for the reprojection
    H = nc.variables['goes_imager_projection'].perspective_point_height
    x1 = nc.variables['x_image_bounds'][0] * H 
    x2 = nc.variables['x_image_bounds'][1] * H 
    y1 = nc.variables['y_image_bounds'][1] * H 
    y2 = nc.variables['y_image_bounds'][0] * H 
    
    # Call the reprojection funcion
    grid = remap(path, extent, resolution, x1, y1, x2, y2)
    
    # Read the data returned by the function 
    if int(Band) <= 6:
        data = grid.ReadAsArray()
    else:
        # If it is an IR channel subtract 273.15 to convert to ° Celsius
        data = grid.ReadAsArray() - 273.15
        # Make pixels outside the footprint invisible
        data[data <= -180] = np.nan
    
    #data is a grid with all temperatures 
        
    countId = 0
    long_factor = abs(extent[2] - extent[0]) / data.shape[1]
    lat_factor = abs(extent[3] - extent[1]) /data.shape[0]
    
    
       
    f = open("/home/cendas/GOES16-Files/Output/RJ/GeoJsonTemperature/"+date + '_' + time_saved + ".geojson", "w")
    f.write("{\n")
    f.write("\"type\": \"FeatureCollection\",\n")
    f.write("\"features\":\n")
    f.write("   [\n")
    
    for yPixelAxis in range (0,data.shape[0],1):
        for xPixelAxis in range (0,data.shape[1],1):
            if countId ==  (data.shape[0] * data.shape[1]) - 1: #If reaches to the last data doesn't put the comma                                                                                                #Longitude                                           #Latitude
                 f.write("{ \"type\": \"Feature\", \"properties\": { \"id\": \""+ str(countId) +"\",\"temperature\":" + str(data[yPixelAxis][xPixelAxis]) +" }, \"geometry\": { \"type\": \"Point\", \"coordinates\": [" + str(extent[0] + ((xPixelAxis + 1) * long_factor)) + "," +str(extent[3] - ((yPixelAxis + 1) * lat_factor))+"] } }\n")        
            else:
               f.write("{ \"type\": \"Feature\", \"properties\": { \"id\": \""+ str(countId) +"\",\"temperature\":" + str(data[yPixelAxis][xPixelAxis]) +" }, \"geometry\": { \"type\": \"Point\", \"coordinates\": [" + str(extent[0] + ((xPixelAxis + 1) * long_factor)) + "," +str(extent[3] - ((yPixelAxis + 1) * lat_factor))+"] } },\n")        
            countId +=1
    
    f.write("   ]\n")
    f.write("}\n")
    f.close()
