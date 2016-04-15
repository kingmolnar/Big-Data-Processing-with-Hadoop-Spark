#!/usr/bin/env pyspark
## from http://ampcamp.berkeley.edu/wp-content/uploads/2013/02/Parallel-Programming-With-Spark-Matei-Zaharia-Strata-2013.pptx

import sys
from pyspark import SparkContext

NUM_ITERATIONS=10

if __name__ == "__main__":
    sc = SparkContext( "local", "PageRank", sys.argv[0], None)
    links = # RDD of (url, neighbors) pairs
    ranks = # RDD of (url, rank) pairs

    for i in range(NUM_ITERATIONS):
        def compute_contribs(pair):
            [url, [links, rank]] = pair  # split key-value pair
            return [(dest, rank/len(links)) for dest in links]

        contribs = links.join(ranks).flatMap(compute_contribs)
        ranks = contribs.reduceByKey(lambda x, y: x + y) \
                        .mapValues(lambda x: 0.15 + 0.85 * x)

    ranks.saveAsTextFile(...)
