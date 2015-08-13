__author__ = 'chexiaoyu'

import json
from spider_class import Spider

class Con_json:

    def __init__(self):
        self.stories = None
        self.str_json = None

    def convert(self, spider):
        self.stories = spider.stories
        self.str_json = json.dumps(self.stories)
        #print self.str_json
        return self.str_json
        #print self.stories
        # for item in self.stories:
        #     print item


