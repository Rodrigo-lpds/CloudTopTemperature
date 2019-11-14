#!/usr/bin/python3
# -*- coding: utf-8 -*-

import glob # Unix style pathname pattern expansion
import os # Miscellaneous operating system interfaces
 
# Directory where you have the GOES-16 Files
dirname = '/home/cendas/GOES16-Files/Samples/'
 
# Put all file names on the directory in a list
G16_images = []
for filename in sorted(glob.glob(dirname+'OR_ABI-L2-CMI*.nc')):
 G16_images.append(filename)
 
# If the log file doesn't exist yet, create one
file = open('/home/cendas/GOES16-Files/Output/Full_Disk/G16_Log.txt', 'a')
file.close()

# Put all file names on the log in a list
logFullDisk = []
with open('/home/cendas/GOES16-Files/Output/Full_Disk/G16_Log.txt') as file1:
 logFullDisk = file1.readlines()


# Remove the line feed
logFullDisk  = [x.strip() for x in logFullDisk ]



# Compare the directory list with the file list
# Loop through all files in the directory
for x in G16_images:
 if x not in logFullDisk:
  os.system("/home/cendas/miniconda3/envs/DataEnv/bin/python3 " + "\"/home/cendas/GOES16-Files/CodeProcess/PythonScripts/process_goes-16_Full_Disk_Projection.py\"" + " " + "\"" + x.replace('\\','\\\\') + "\"")
  os.system("/home/cendas/miniconda3/envs/DataEnv/bin/python3 " + "\"/home/cendas/GOES16-Files/CodeProcess/PythonScripts/TemperatureDataToGeojsonFD.py\"" + " " + "\"" + x.replace('\\','\\\\') + "\"")

