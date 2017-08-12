"""
Yelp Review Topology
"""

from streamparse import Grouping, Topology

###from bolts.wordcount import WordCountBolt
from spouts.yelp_reviews import YelpReviewSpout

class WordCount(Topology):
    review_spout = YelpReviewSpout.spec()
    
   

