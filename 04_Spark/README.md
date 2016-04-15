# Introduction to Apache Spark

Apache Spark provides a programming paradigm centered on a data structure called the *resilient distributed dataset* (RDD), a read-only multiset of data items distributed over a cluster of machines, that is maintained in a fault-tolerant way.

It extends the MapReduce cluster computing paradigm, which is somewhat limited to linear data-flow structures. In addition Spark's RDDs reside in the main memory, thereby reducing the amount of disk access.

## Programming Languages
Spark works with Python, R, Scala, Java. Eventually it might support even more programming languages. Unlike the Map Reduce Streaming API programs in any language have to utilize libraries to access and manipulate RDDs.

## Environment
Spark can run on a (multi-core) single computer or on a distributed compute cluster, where it usually takes advantage of the Hadoop infrastructure. This allows to develop and run programs on a laptop, and then run them with scaled-up data sets on a cluster.

Spark is already installed on the Hortonworks Virtual machine. Instructions to install Spark on a personal computer are posted here:
1. http://genomegeek.blogspot.com/2014/11/how-to-install-apache-spark-on-mac-os-x.html
2. https://edumine.wordpress.com/2015/06/11/how-to-install-apache-spark-on-a-windows-7-environment/


## Resources
1. https://spark.apache.org/docs/latest/programming-guide.html
2. [Spark for Python Developers by Amit Nandi (2015)](http://it-ebooks.info/book/6809/)
3. [Machine Learning with Spark by Nick Pentreath (2015)](http://it-ebooks.info/book/5655/)
4. [Paralle Programming with Spark by Matei Zaharia
 (Presentation)](http://ampcamp.berkeley.edu/wp-content/uploads/2013/02/Parallel-Programming-With-Spark-Matei-Zaharia-Strata-2013.pptx)

## Examples
1. Word Count
2. Movie Lens data
3. Page Rank
