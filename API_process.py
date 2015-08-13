#coding:utf-8
__author__ = 'chexiaoyu'

import spider_class
import urllib2
import urllib
import json
import re
import requests


class API_process:


    def __init__(self,access_token):
        self.access_token = access_token
        self.url = 'http://dev02.haizhi.com:19977/'


    def Get_access_token(self):
        dir = 'api/opends_token/gen'
        payload = {"access_token":self.access_token}
        r = requests.post(self.url+dir,data = payload)
        js = json.loads(r.text)
        self.access_token = js["result"]["access_token"]


    def Create_database(self,database_name):
        dir = 'api/ds/create'
        payload = {"access_token":self.access_token, "name":database_name,"type":"opends"}
        r = requests.post(self.url+dir,data = payload)
        js = json.loads(r.text)
        if js["status"] == "0":
             print "数据库创建成功！"
        else:
             print js["errstr"]


    def Show_database(self):
        dir = 'api/ds/list'
        payload = {"access_token":self.access_token}
        r = requests.post(self.url+dir,data = payload)
        print r.text

    def Get_ds_id(self):
        dir = 'api/ds/list'
        payload = {"access_token":self.access_token}
        r = requests.post(self.url+dir,data = payload).json()
        for i in r["result"]["data_source"]:
            if i["name"] == "Cnblogs":
                return i["ds_id"]


#error

    def Del_database(self,ds_id):
        dir = 'api/ds/delete'
        payload = {"access_token":self.access_token,"ds_id":ds_id}
        r = requests.post(self.url+dir,data=payload)
        js = json.loads(r.text)
        if js["status"] == "0":
            print "数据库删除成功！"
        else:
            print js["errstr"]

    #返回值为table id
    def Create_table(self,ds_id,tb_name):
        dir = 'api/tb/create'
        params = {'access_token':self.access_token}
        payload = {
        #    "access_token":self.access_token,
            "ds_id":ds_id,
            "name":tb_name,
            "schema":[
                {"name":"Recommend","type":"number","comment":""},
                {"name":"Title","type":"string","comment":""},
                {"name":"Author","type":"string","comment":""},
                {"name":"Date","type":"date","comment":""},
                {"name":"Comment","type":"number","comment":""},
                {"name":"Reading","type":"number","comment":""}

            ],
        #    "uniq_key":[
        #
        #    ]
        }
        r = requests.post(self.url+dir,params=params,data = json.dumps(payload))
        js = json.loads(r.text)
        if js["errstr"] != "0":
            print js["errstr"]
        else:
            print "创建数据表成功！"
        return js["result"]["tb_id"]

    def Insert_table(self,tb_id,fields,data):
        dir = 'api/tb/insert'
        params = {
            "access_token":self.access_token,
            "tb_id":tb_id,
            "fields":json.dumps(fields)
        }
        r = requests.post(self.url+dir,params=params,data = json.dumps(data)).json()
        if r["status"] == "0":
            print r["result"]
        else:
            print r["errstr"]

    def Merge_table(self,tb_id):
        dir = 'api/tb/merge'
        params = {
            "access_token":self.access_token,
            "tb_id":tb_id,
            "fast":"1"
        }
        r = requests.post(self.url+dir,data=params).json()
        if r["status"] == "0":
            print "合并完成"
        else:
            print r["errstr"]

    def Clean_table(self,tb_id):
        dir = 'api/tb/clean'
        params = {
            "access_token":self.access_token,
            "tb_id":tb_id
        }
        r = requests.post(self.url+dir,data = params).json()
        if r["status"] == "0":
            print "清空数据表！"
        else:
            print r["errstr"]



#   def Create_table(self):
#        dir = 'api/tb/create'



# access_token = "0a27d480339ebe12e8f0f09f1bcf0d97"
# process = API_process(access_token)
# process.Get_access_token()
# process.Create_database("test3")
# process.Show_database()
#
# #process.Del_database('ds_57a9a9d9529843f3971745e28e624bfa')
#
# tb_id = process.Create_table('ds_759475e5feb24ec3afc69a98988cda14','table8')
# process.Insert_table(tb_id,["1","2"],[["1","2"]])
# process.Merge_table(tb_id)
#
# #print process.access_token
# #print process.Get_access_token(access_token)
