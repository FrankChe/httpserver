__author__ = 'chexiaoyu'

import spider_class
import API_process
import urllib2
import urllib
import re
import requests
import json

class Operation:

    def __init__(self):
        self.page = 1
        self.stories = []
        self.fields = []
        self.api = None
        self.tb_id = None
        self.ds_id = None
        self.tb_id = None

    def get_stories(self,page):
        self.page = page
        spider = spider_class.Spider()
        self.stories = spider.loadPage(self.page)

    def set_fileds(self,fields):
        self.fields = fields

    def show_stories(self):
        print self.stories[0]

    def api_op(self):
        access_token = "0a27d480339ebe12e8f0f09f1bcf0d97"
        self.api = API_process.API_process(access_token)
        self.api.Get_access_token()
        self.api.Create_database("Cnblogs")
        self.api.Show_database()
        self.ds_id = self.api.Get_ds_id()
        self.tb_id = self.api.Create_table(self.ds_id,'Cnblogs')
        self.api.Insert_table(self.tb_id,self.fields,self.stories)
        self.api.Merge_table(self.tb_id)
        #self.api.Clean_table(self.tb_id)
        #self.api.Merge_table(self.tb_id)

        #self.api.Insert_table(self.)

    def start(self):
        page = 200
        op = Operation()
        op.get_stories(page)
        op.set_fileds(["Recommend","Title","Author","Date","Comment","Reading"])
        #op.show_stories()
        op.api_op()

# if __name__ == "__main__":
#     page = 200
#     op = Operation()
#     op.get_stories(page)
#     op.set_fileds(["Recommend","Title","Author","Date","Comment","Reading"])
#
#     #op.show_stories()
#     op.api_op()

