#!/usr/bin/python3
# -*- coding: utf-8 -*-

import glob # Unix style pathname pattern expansion
import os # Miscellaneous operating system interfaces
 
# Directory where you have the GOES-16 Files
dirname = '/home/cendas/'
 
# Put all file names on the directory in a list
G16_images = []
for filename in sorted(glob.glob(dirname+'OR_ABI-L2-CMI*.nc')):
 G16_images.append(filename)
 
# If the log file doesn't exist yet, create one
file = open('/home/cendas/GOES16-Files/GOES16-Output/Full_Disk_Projections/G16_Log.txt', 'a')
file.close()
 
file = open('/home/cendas/GOES16-Files/GOES16-Output/South_America_Projections/G16_Log.txt', 'a')
file.close()

file = open('/home/cendas/GOES16-Files/GOES16-Output/RJ_Projections/G16_Log.txt', 'a')
file.close()


# Put all file names on the log in a list
logFullDisk = []
with open('/home/cendas/GOES16-Files/GOES16-Output/Full_Disk_Projections/G16_Log.txt') as file1:
 logFullDisk = file1.readlines()

logSouthAmerica = []
with open('/home/cendas/GOES16-Files/GOES16-Output/South_America_Projections/G16_Log.txt') as file2:
 logSouthAmerica = file2.readlines()

logRJ = []
with open('/home/cendas/GOES16-Files/GOES16-Output/RJ_Projections/G16_Log.txt') as file3:
 logRJ = file3.readlines()



# Remove the line feed
logFullDisk  = [x.strip() for x in logFullDisk ]
logSouthAmerica = [x.strip() for x in logSouthAmerica]
logRJ = [x.strip() for x in logRJ]



# Compare the directory list with the file list
# Loop through all files in the directory
for x in G16_images:
 # If a file is not on the log, process it
 
 if x not in logFullDisk:
  #os.system("python3 " + "\"/home/VLAB/Tutorials/process_goes-16.py\"" + " " + "\"" + x.replace('\\','\\\\') + "\"")
  print(x)
  os.system("/home/cendas/miniconda3/envs/DataEnv/bin/python3 " + "\"/home/cendas/GOES16-Files/GOES16-Scripts/Scripts/process_goes-16_Full_Disk_Projection.py\"" + " " + "\"" + x.replace('\\','\\\\') + "\"")

 if x not in logSouthAmerica:
  os.system("/home/cendas/miniconda3/envs/DataEnv/bin/python3 " + "\"/home/cendas/GOES16-Files/GOES16-Scripts/Scripts/process_goes-16_South_America_Projection.py\"" + " " + "\"" + x.replace('\\','\\\\') + "\"")
 
 if x not in logRJ:
  os.system("/home/cendas/miniconda3/envs/DataEnv/bin/python3 " + "\"/home/cendas/GOES16-Files/GOES16-Scripts/Scripts/process_goes-16_RJ_Projection.py\"" + " " + "\"" + x.replace('\\','\\\\') + "\"")

