# Map-Reduce Streaming API

The Map-Reduce Streaming API provides a convenient way to perform parallel computing by utilizing familiar programming concepts and languages. The MR Streaming API manages data distribution, load balancing, and communication between the processes, which read from standard input and write to standard output.

Programs can be tested outside the Hadoop environment using the basic UNIX pipe mechanism:

`cat input.dat | mapper.py | sort | combiner.py | reduce.py > output.dat`

We will explore how various algorithms can be implemented under the Map-Reduce concept.


## Examples
1. Word Count
2. Twitter ETL
3. Collating, Sorting, Filtering
4. Table Joins




## Data
More data can be found here:
1. Twitter 2012 Presidential Election https://datahub.io/dataset/twitter-2012-presidential-election
2. De Bello Gallico http://www.gutenberg.org/files/218/218.
3. Enron Email Data Set http://www.edrm.net/resources/data-sets/edrm-enron-email-data-set




## References
1. MR Examples in Perl https://metacpan.org/pod/Hadoop::Streaming
2. MapReduce Patterns, Algorithms, and Use Cases https://highlyscalable.wordpress.com/2012/02/01/mapreduce-patterns/
3. Joins with Map Reduce https://chamibuddhika.wordpress.com/2012/02/26/joins-with-map-reduce/
4. Writing an Hadoop MapReduce Program in Python http://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/
5. Python implementation of binary regularized logistic regression with stochastic gradient descent, packaged as scripts for use with Hadoop streaming https://github.com/elsevierlabs/logistic-regression-sgd-mapreduce
6. MapReduce for Statistical NLP/Machine Learning http://www.cs.columbia.edu/~smaskey/CS6998-0412/slides/week7_statnlp_web.pdf
