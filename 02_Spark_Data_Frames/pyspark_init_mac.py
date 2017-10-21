#
# This configuration works for Spark on macOS using homebrew
#
import os, sys
# set OS environment variable
os.environ["SPARK_HOME"] = '/usr/local/Cellar/apache-spark/2.2.0/libexec'
# add Spark library to Python
sys.path.insert(0, os.path.join(os.environ["SPARK_HOME"], 'python'))

# import package
import pyspark
from pyspark.context import SparkContext, SparkConf

import atexit
def stop_my_spark():
    sc.stop()
    del(sc)

# Register exit    
atexit.register(stop_my_spark)

# Configure and start Spark ... but only once.
if not 'sc' in globals():
    conf = SparkConf()
    conf.setAppName('MyFirstSpark') ## you may want to change this
    conf.setMaster('local[2]')
    sc = SparkContext(conf=conf)
    print "Launched Spark version %s with ID %s" % (sc.version, sc.applicationId)

