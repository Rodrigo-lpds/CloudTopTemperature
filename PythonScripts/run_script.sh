#!/bin/bash
source /home/cendas/miniconda3/bin/activate DataEnv

/home/cendas/miniconda3/envs/DataEnv/bin/python3 /home/cendas/GOES16-Files/CodeProcess/PythonScripts/monitorRJ.py
printf "\nAs projecoes centradas no Rio de Janeiro estao atualizadas\n\n"

export WORK='/home/cendas/GOES16-Files/Output/RJ/Projections/CH13/'

cd $WORK

ls -t | tail -n +11 | xargs rm --

/home/cendas/miniconda3/envs/DataEnv/bin/python3 /home/cendas/GOES16-Files/CodeProcess/PythonScripts/monitorSouthAmerica.py

printf "\nAs projecoes Sulamericanas estao atualizadas\n\n" 

export WORK='/home/cendas/GOES16-Files/Output/South_America/Projections/CH13/'

cd $WORK

ls -t | tail -n +11 | xargs rm --