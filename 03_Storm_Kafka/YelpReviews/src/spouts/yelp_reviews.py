import os, sys,datetime
import json
from time import sleep

from streamparse import Spout

REVIEW='/home/data/yelp/yelp_dataset_challenge_academic_dataset/yelp_academic_dataset_review.json'

class YelpReviewSpout(Spout):
    outputs = ['date', 'stars', 'text', 'user_id', 'business_id']

    def initialize(self, stormconf, context):
        """
        open review.json file, and store file connection in object
        """
        self.f = open(REVIEW, 'r')
        
    def next_tuple(self):
        """
         read line, strip, decode json, and emit review text, date, and star rating
        """
        line = self.f.readline().strip()
        rec = json.loads(line)
        self.logger.info("review '''{}'''[pid={}]".format(rec['text'][0:20], self.pid))
        self.emit([rec['date'], rec['stars'], rec['text'], rec['user_id'], rec['business_id']])
        sleep(1.0)   ## sleep a second
