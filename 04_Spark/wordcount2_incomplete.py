# Word count on 1st Chapter of the Book using PySpark
# import regex module
import re
# import add from operator module
from operator import add
# read input file
file_in = sc.textFile('/home/an/Documents/A00_Documents/Spark4Py
20150315')
# count lines
print('number of lines in file: %s' % file_in.count())
# add up lengths of each line
chars = file_in.map(lambda s: len(s)).reduce(add)
print('number of characters in file: %s' % chars)
# Get words from the input file
words =file_in.flatMap(lambda line: re.split('\W+', line.lower().
strip()))
# words of more than 3 characters
words = words.filter(lambda x: len(x) > 3)
# set count 1 per word
words = words.map(lambda w: (w,1))
# reduce phase - sum count all the words
words = words.reduceByKey(add)
