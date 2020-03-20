#!/usr/bin/python3
# -*- coding: utf-8 -*-

import glob # Unix style pathname pattern expansion
import os # Miscellaneous operating system interfaces
 
# Directory where you have the GOES-16 Files
dirname = '/home/cendas/GOES16-Files/CodeProcess/PythonScripts/samples/'
 
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
      #print(G16_images[count])
      pass
  #print()  
#print(G16_images)sss

# If the log file doesn't exist yet, create one
file = open('/home/cendas/GOES16-Files/CodeProcess/PythonScripts/TrueColor.txt', 'a')
file.close()


# Put all file names on the log in a list
logTrueColor = []
with open('/home/cendas/GOES16-Files/CodeProcess/PythonScripts/TrueColor.txt') as file:
  logTrueColor = file.readlines()


# Remove the line feed
logTrueColor = [x.strip() for x in logTrueColor]
#print(logTrueColor)

ch01 = ""
ch02 = ""
ch03 = ""

validateCH = []
pace = int((len(G16_images))/3)
G16_images =  sorted(G16_images)
for x in range (int(len(G16_images)/3)):
  validateCH01 = False
  validateCH02 = False
  validateCH03 = False
  
  ch01 = G16_images[x]  
  ch02 = G16_images[x + pace]
  ch03 = G16_images[x + 2*pace]
  
  print(logTrueColor.count (ch01))
  print(logTrueColor.count (ch02))
  print(logTrueColor.count (ch03))
  
  if logTrueColor.count (ch01) == 0:
    validateCH01 = True
  if logTrueColor.count (ch02) == 0:
    validateCH02 = True
  if logTrueColor.count (ch03) == 0:
    validateCH03 = True
  if (validateCH01 and validateCH02 and validateCH03):
    validateCH.append (ch01)
    validateCH.append (ch02)
    validateCH.append (ch03)

#print (G16_images)
print()
#print (logTrueColor)  
#print()    
print (validateCH)   
    
  
# Compare the directory list with the file list
# Loop through all files in the directory

#for x in G16_images:
 # If a file is not on the log, process it
# if x not in logRJ:
#  os.system("/home/cendas/miniconda3/envs/DataEnv/bin/python3 " + "\"/home/cendas/GOES16-Files/CodeProcess/PythonScripts/process_goes-16_RJ_Projection.py\"" + " " + "\"" + x.replace('\\','\\\\') + "\"")
  #os.system("/home/cendas/miniconda3/envs/DataEnv/bin/python3 " + "\"/home/cendas/GOES16-Files/CodeProcess/PythonScripts/TemperatureDataToGeojsonRJ.py\"" + " " + "\"" + x.replace('\\','\\\\') + "\"")
  
#for x in range (int(len(logTrueColor)/3)): #De 3 em 3
  
#  os.system("/home/cendas/miniconda3/envs/DataEnv/bin/python3 " + "\"/home/cendas/GOES16-Files/CodeProcess/PythonScripts/trueColorRJ.py\"" + " " + logTrueColor[x].replace('\\','\\\\') + " "+ logTrueColor[x+1].replace('\\','\\\\')+ " " + logTrueColor[x+2].replace('\\','\\\\'))
