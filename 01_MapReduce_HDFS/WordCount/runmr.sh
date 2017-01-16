#!/bin/bash
WD=`pwd`

yarn jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar \
	-input $1 \
	-output /home/$USER/streamout \
	-mapper $WD/mapper.py \
	-reducer $WD/reducer.py

