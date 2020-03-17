#!/usr/bin/python3
# -*- coding: utf-8 -*-

import glob # Unix style pathname pattern expansion
import os # Miscellaneous operating system interfaces
 
# Directory where you have the GOES-16 Files
dirname = '/home/cendas/GOES16-Files/Samples/'
 
# Put all file names on the directory in a list
G16_images = []
for filename in sorted(glob.glob(dirname+'OR_ABI-L2-CMIPF-M6C01*.nc')):
  G16_images.append(filename)
for filename in sorted(glob.glob(dirname+'OR_ABI-L2-CMIPF-M6C02*.nc')):
  G16_images.append(filename)
for filename in sorted(glob.glob(dirname+'OR_ABI-L2-CMIPF-M6C03*.nc')):
  G16_images.append(filename)

singular = []
for item in G16_images:
  Id=item.split('_')[3][1:]
  if Id not in singular:
    singular.append(Id)
for posi in range(len(singular)):    
  for count in range(len(G16_images)):
    if G16_images[count].find(singular[posi]) != -1:
      print(G16_images[count])
  print()  
# If the log file doesn't exist yet, create one
#file = open('/home/cendas/GOES16-Files/Output/RJ/G16_Log.txt', 'a')
#file.close()


# Put all file names on the log in a list
#logRJ = []
#with open('/home/cendas/GOES16-Files/Output/RJ/G16_Log.txt') as file:
# logRJ = file.readlines()


# Remove the line feed
#logRJ = [x.strip() for x in logRJ]



# Compare the directory list with the file list
# Loop through all files in the directory
#for x in G16_images:
 # If a file is not on the log, process it
# if x not in logRJ:
#  os.system("/home/cendas/miniconda3/envs/DataEnv/bin/python3 " + "\"/home/cendas/GOES16-Files/CodeProcess/PythonScripts/process_goes-16_RJ_Projection.py\"" + " " + "\"" + x.replace('\\','\\\\') + "\"")
  #os.system("/home/cendas/miniconda3/envs/DataEnv/bin/python3 " + "\"/home/cendas/GOES16-Files/CodeProcess/PythonScripts/TemperatureDataToGeojsonRJ.py\"" + " " + "\"" + x.replace('\\','\\\\') + "\"")