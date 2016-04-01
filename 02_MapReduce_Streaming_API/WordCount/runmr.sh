#!/bin/bash

yarn jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar \
	-input $1 \
	-output /home/pmolnar/streamout \
	-mapper ./mapper.py \
	-reducer ./reducer.py

