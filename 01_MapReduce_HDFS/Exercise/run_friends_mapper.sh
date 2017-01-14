#!/bin/bash
WD=/home/pmolnar/Workshops/IntroHadoop/01_MapReduce_HDFS/Exercise
OUTPUT=/user/$USER/output/yelp_friends
hdfs dfs -rm -r -f -skipTrash $OUTPUT

INPUT=/user/$USER/data/yelp/yelp_academic_dataset_user.json
yarn \
    jar /usr/hdp/2.4.2.0-258/hadoop-mapreduce/hadoop-streaming-2.7.1.2.4.2.0-258.jar \
    -mapper "$WD/friends_mapper.py" \
    -input $INPUT \
    -output $OUTPUT