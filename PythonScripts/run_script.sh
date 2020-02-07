#!/bin/bash
source /home/cendas/miniconda3/bin/activate DataEnv

CHANNELS=('CH01' 'CH02' 'CH03' 'CH04' 'CH05' 'CH06' 'CH07' 'CH08' 'CH09' 'CH10' 'CH11' 'CH12' 'CH13' 'CH14' 'CH15' 'CH16')
qtdCH=${#CHANNELS[@]}

/home/cendas/miniconda3/envs/DataEnv/bin/python3 /home/cendas/GOES16-Files/CodeProcess/PythonScripts/monitorRJ.py
printf "\nAs projecoes centradas no Rio de Janeiro estao atualizadas\n\n"

#Deixa apenas 10 projecoes/imagens no diretorio
for ((Channel=0; Channel< qtdCH; Channel++)) do
export WORK='/home/cendas/GOES16-Files/Output/RJ/Projections/'${CHANNELS[$Channel]}'/'
cd $WORK

ls -t | tail -n +11 | xargs rm 

done


/home/cendas/miniconda3/envs/DataEnv/bin/python3 /home/cendas/GOES16-Files/CodeProcess/PythonScripts/monitorSouthAmerica.py

printf "\nAs projecoes Sulamericanas estao atualizadas\n\n" 

#Deixa apenas 10 projecoes/imagens no diretorio
for ((Channel=0; Channel< qtdCH; Channel++)) do
export WORK='/home/cendas/GOES16-Files/Output/South_America/Projections/'${CHANNELS[$Channel]}'/'

cd $WORK

ls -t | tail -n +11 | xargs rm --

done

/home/cendas/miniconda3/envs/DataEnv/bin/python3 /home/cendas/GOES16-Files/CodeProcess/PythonScripts/monitorSistConvRJ.py

#export WORK='/home/cendas/GOES16-Files/Output/RJ/SistConvectivos/'

#cd $WORK

#ls -t | tail -n +11 | xargs rm --



#Deixa apenas os 160 arquivos NetCDF no diretorio
export WORK='/home/cendas/GOES16-Files/Samples/'
cd $WORK

ls -t | tail -n +161 | xargs rm 


