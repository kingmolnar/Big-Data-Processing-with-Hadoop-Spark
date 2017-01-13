# Session 1: MapReduce, HDFS

## Outline

1. Overview of parallel distributed programming
2. UNIX Refresher
    1. Pipes `cat $F | sort | uniq -c | sort -rn | head -20`
    2. File-system commands
    3. "useful commands"
    4. Daemons, processes and services
3. Welcome to the Hadoop family
3. Hadoop File-system
4. MapReduce (streaming API)
5. Yelp! dataset


## Overview of parallel distributed programming
- https://github.com/kingmolnar/IntroHadoop/raw/master/IntroductionParallelDistributedProgramming.pptx

## UNIX Refresher

### Useful commands

'cut', 'tr', 'awk', 'sed', 'sort', 'uniq', and 'jq'

### References
- http://www.gregreda.com/2013/07/15/unix-commands-for-data-science/
- http://jeroenjanssens.com/2013/09/19/seven-command-line-tools-for-data-science.html

## Hadoop File-system
http://arc.insight.gsu.edu/~pmolnar/HDFS%20Cheat%20Sheet.html


## Map-Reduce Streaming API
https://raw.githubusercontent.com/kingmolnar/IntroHadoop/master/01_MapReduce_HDFS/MapReduce_Streaming_API.pptx

The Map-Reduce Streaming API provides a convenient way to perform parallel computing by utilizing familiar programming concepts and languages. The MR Streaming API manages data distribution, load balancing, and communication between the processes, which read from standard input and write to standard output.

Programs can be tested outside the Hadoop environment using the basic UNIX pipe mechanism:

`cat input.dat | mapper.py | sort | combiner.py | reduce.py > output.dat`

We will explore how various algorithms can be implemented under the Map-Reduce concept.


### Examples
1. Word Count
2. Twitter ETL
3. Collating, Sorting, Filtering
4. Table Joins




### Data
More data can be found here:
1. Twitter 2012 Presidential Election https://datahub.io/dataset/twitter-2012-presidential-election
2. De Bello Gallico http://www.gutenberg.org/files/218/218.
3. Enron Email Data Set http://www.edrm.net/resources/data-sets/edrm-enron-email-data-set


### References
1. MR Examples in Perl https://metacpan.org/pod/Hadoop::Streaming
2. MapReduce Patterns, Algorithms, and Use Cases https://highlyscalable.wordpress.com/2012/02/01/mapreduce-patterns/
3. Joins with Map Reduce https://chamibuddhika.wordpress.com/2012/02/26/joins-with-map-reduce/
4. Writing an Hadoop MapReduce Program in Python http://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/
5. Python implementation of binary regularized logistic regression with stochastic gradient descent, packaged as scripts for use with Hadoop streaming https://github.com/elsevierlabs/logistic-regression-sgd-mapreduce
6. MapReduce for Statistical NLP/Machine Learning http://www.cs.columbia.edu/~smaskey/CS6998-0412/slides/week7_statnlp_web.pdf


## Yelp!
- https://www.yelp.com/dataset_challenge/dataset
    (http://arc.insight.gsu.edu/~pmolnar/Yelp%20Dataset%20Challenge%20-%20Yelp.html)
- https://github.com/Yelp/dataset-examples
- on cluster in `/home/data/yelp/` and `hdfs://data/yelp/`
