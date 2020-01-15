#!/bin/bash
export WORK='/home/cendas/GOES16-Files/Output/RJ/Projections/CH13/'

echo $WORK

cd $WORK

ls -t | tail -n +11 | xargs rm --