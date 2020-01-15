#!/bin/bash
source activate DataEnv

/home/cendas/miniconda3/envs/DataEnv/bin/python3 /home/cendas/GOES16-Files/CodeProcess/PythonScripts/monitorSouthAmerica.py

printf "\nAs projecoes Sulamericanas estao atualizadas\n\n"

/home/cendas/miniconda3/envs/DataEnv/bin/python3 /home/cendas/GOES16-Files/CodeProcess/PythonScripts/monitorRJ.py
printf "\nAs projecoes centradas no Rio de Janeiro estao atualizadas\n\n"
