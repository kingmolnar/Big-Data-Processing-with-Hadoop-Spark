# Session  3
## Machine Learning with Spark
| Date | Time |
|------|------|
|  Friday, 10/27    |  1:00 - 4:00 PM       

# Spark Machine Learning Library

Spark has a rich library of machine learning algorithms. As the evolution of Spark continues different versions offer variations of implemented algorithms in two packages:
- spark.mllib contains the original API built on top of RDDs.
- spark.ml provides higher-level API built on top of DataFrames for constructing ML pipelines.

Documentation can be found at http://spark.apache.org/docs/1.6.1/mllib-guide.html for version 1.6.1. ([latest version](http://spark.apache.org/docs/latest/mllib-guide.html))

## Objective for this Session
We will explore some of Spark's machine learning features. In particular two tasks (to start with):
1. Use the star-ratings by Yelp users on restaurants to find out which businesses cater to the same crowd. Once we established a model that represents the users' preferences we can develop a similarity measure based on user ratings, and train a new model that expresses the similarity of restaurants based on their attributes.

2. Develop a document classifier on Yelp reviews. This could be based on star-ratings (or just good vs bad), or certain properties of the restaurants.


### Collaborative Filter
- [Alternating Least Squares Method for Collaborative Filtering](https://bugra.github.io/work/notes/2014-04-19/alternating-least-squares-method-for-collaborative-filtering/)
- [Matrix Factorization Techniques for Recommender Systems](http://dl.acm.org/citation.cfm?id=1608614)
- http://spark.apache.org/docs/1.6.1/mllib-collaborative-filtering.html

### Text Classification
- http://spark.apache.org/docs/1.6.1/ml-features.html#tf-idf-hashingtf-and-idf
- http://spark.apache.org/docs/1.6.1/mllib-classification-regression.html
- http://www.cs.waikato.ac.nz/~eibe/pubs/kibriya_et_al_cr.pdf
