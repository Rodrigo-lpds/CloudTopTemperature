#!/bin/bash

FILES=/home/cendas/GOES16-Files/Samples/OR_ABI-L2-CMIPF-M*.nc
count=0
for f in $FILES
do
  #echo "Processing $f file..."
  #count=`expr $count + 1`
  # take action on each file. $f store current file name
  #CH_NUM= 
  #echo ${f:53:2}	
  #echo "$CH_NUM"
  mv  $f /home/cendas/GOES16-Files/Samples/CH${f:53:2}/
done
#echo "$count"
