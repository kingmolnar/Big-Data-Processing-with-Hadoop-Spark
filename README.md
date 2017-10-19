# Big Data Processing with Hadoop/Spark
The workshop series offers a brief introduction to concepts of parallel distributed computing and the Hadoop universe. Participants will learn to navigate among the various tools, and to write programs for large scale data analysis. **Examples will be provided in Python**; knowledge of the Java programming language is not required.

We will mainly work with **Apache Spark**, however, we will also cover some of the core components of the greater Hadoop universe. In particular the distributed file system (HDFS), Yarn, Hive, Kafka, and Storm.

## Schedule

Session | Date | Time | Topic
--------|------|------|------
1| Friday, 10/20 | 1:00 - 4:00 PM | Distributed Computing, HDFS, Distributed Data Sets
2| Saturday, 10/21 | 9:00 AM - 12:00 noon | Spark Data Frames
3| Friday, 10/27 | 1:00 - 4:00 PM | Machine Learning with Spark
4| Saturday, 10/28 | 9:00 AM - 12:00 noon | Stream Processing



## Sessions

1. Participants learn about the core concepts behind Hadoop, how to manage data files on HDFS, and how to write scalable, distributed data processing programs in Python.
2. Data frames are a core building block in Spark. This session covers organizing data in structured tables, selecting columns and rows, grouping and aggregating, and joining multiple tables.
3. Spark offers a rich machine learning library. This session covers creating feature vectors from data, training various models and validating results.
4. Often data streams need to be analyzed in quasi real-time. The session introduces two ways to process streaming data: event-based and batch-based.



## Preparation
- Participants should bring their own laptop.
- Windows users should install a SSH client (for terminal connection) like http://smartty.sysprogs.com/.
- Mac and Linux users already have this capability.
In addition, a recent web-browser is required. (Mac users should install the Google-Chrome browser since there are some known issues with the Safari browser.)


## Using Spark (Hadoop) on your personal computer
- Pretty much everything in the Hadoop eco-system runs on Java. Hence, it's OS agnostics. However, to get all the components to work is still a huge undertaking.
- If you want to explore the entire Hadoop world install the pre-configured virtual machine.
- In order to just use Spark or PySpark follow the instructions for the respective systems.

### Spark on macOS
1. Install **homebrew** on your macOS computer, if you haven't done yet. Instructions at https://brew.sh
2. From the command line run:
<pre>
    $ brew install apache-spark
</pre>


### Spark on Windows 10
- Follow these instructions to get Spark and Python running on your Windows computer https://medium.com/@GalarnykMichael/install-spark-on-windows-pyspark-4498a5d8d66c

### Everything Hadoop on Virtual Machine for Windows or macOS
**These steps are only needed if you want to run Hadoop on your own computer:**
1. Install either VMWare Virtual Machine or Virtual Box on your laptop. (VMWare offers a free Workstation Player for Windows and Linux https://my.vmware.com/en/web/vmware/free#desktop_end_user_computing/vmware_workstation_player/12_0, OS X users may use VMWare Fusion https://www.vmware.com/products/fusion/fusion-evaluation.html. Oracle's VirtualBox https://www.virtualbox.org/wiki/Downloads is free for all platforms.)
2. Download the Hortonworks Sandbox for the respective virtual machine from http://hortonworks.com/products/hortonworks-sandbox/#install (it's over 9 GB, it may take a while).




## Documentation
1. [Official Apache Spark Documentation](http://spark.apache.org/docs/latest/)
