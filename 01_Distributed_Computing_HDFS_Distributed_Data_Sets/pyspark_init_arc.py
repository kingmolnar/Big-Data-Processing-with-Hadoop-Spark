#
# This configuration works for Spark on arc.insight.gsu.edu
#
import os, sys
# set OS environment variable
os.environ["SPARK_HOME"] = '/usr/hdp/2.4.2.0-258/spark'
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
    conf.setMaster('yarn-client')
    conf.set('spark.ui.port', '63729')
    sc = SparkContext(conf=conf)
    print "Launched Spark version %s with ID %s" % (sc.version, sc.applicationId)
    print "http://arc.insight.gsu.edu:8088/cluster/app/%s"% (sc.applicationId)
