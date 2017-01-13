# Exercise: UNIX, HDFS and Map-Reduce

The following are ideas to test our newly gained knowledge:

## Warm-up
1. Create a folder structure under your user directory on the HDFS, and load some data files (e.g. Yelp) from the local file-system. Split data- files into smaller chunks, and `gzip` them.
2. Extract CSV tables from Yelp or Twitter JSON files using `jq` or `python`.
3. Perform aggregations and frequency counts using UNIX command line tools and pipes.


## Walk
1. Write a Map-Reduce mapper to filter and convert rows from a single datafile, and produce a (small) CSV table. Run Map-Reduce with data on the HDFS, move the resulting CSV table onto the local file system.
2. Write a mapper and reducer to count words in Yelp reviews. Produce a list with the 200 most frequent words.

## Run
1. Join tables using Map-Reduce (use Yelp ... and incorporate JSON extraction)
2. Write a sentiment analysis script in Python, and use Map-Reduce to apply to the Yelp reviews. **Run faster:** Produce a table with 'Sentiment' and 'Rating' from Yelp reviews.
