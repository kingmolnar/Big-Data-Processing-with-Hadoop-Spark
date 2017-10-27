"""
Load packages and create context objects...
"""
import os
import platform
import sys
if not 'sc' in vars():
    sys.path.append('/usr/hdp/2.4.2.0-258/spark/python')
    os.environ["SPARK_HOME"] = '/usr/hdp/2.4.2.0-258/spark'
    os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages com.databricks:spark-csv_2.11:1.2.0 pyspark-shell'
    import py4j
    import pyspark
    from pyspark.context import SparkContext, SparkConf
    from pyspark.sql import SQLContext, HiveContext
    from pyspark.storagelevel import StorageLevel
    sc = SparkContext()
    import atexit
    atexit.register(lambda: sc.stop())
    print("""Welcome to
          ____              __
         / __/__  ___ _____/ /__
        _\ \/ _ \/ _ `/ __/  '_/
       /__ / .__/\_,_/_/ /_/\_\   version %s
          /_/
    """ % sc.version)
else:
    print("""Already running
          ____              __
         / __/__  ___ _____/ /__
        _\ \/ _ \/ _ `/ __/  '_/
       /__ / .__/\_,_/_/ /_/\_\   version %s
          /_/
    """ % sc.version)

if not 'sqlCtx' in vars():
    sqlCtx = SQLContext(sc)
print 'Spark Context available as `sc`'
print 'Spark SQL Context (%s) available as `sqlCtx`'%str(type(sqlCtx))
print "Monitor this application at http://arc.insight.gsu.edu:8088/proxy/"+sc.applicationId

