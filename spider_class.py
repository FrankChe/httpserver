#coding:utf-8
__author__ = 'chexiaoyu'


import urllib
import urllib2
import re
import thread
import time

class Spider:

    def __init__(self):
        self.pageIndex = 1
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        #初始化headers
        self.headers = { 'User-Agent' : self.user_agent }
        #存放文章内容的变量，每一个元素是每一页的文章内容
        self.stories = []
        self.pattern = None

    def getPage(self,pageIndex):
        """传入某一页索引获得页面代码"""
        try:
            values = {"CategoryId": "808","CategoryType": "SiteHome","ItemListActionName": "PostList","ParentCategoryId": 0}
            values["PageIndex"] = pageIndex
            data = urllib.urlencode(values)
            #url = 'http://www.cnblogs.com/p' + str(pageIndex)
            url = 'http://www.cnblogs.com'
            request = urllib2.Request(url,data,headers = self.headers)
            response = urllib2.urlopen(request)
            pageCode = response.read().decode('utf-8')
            return pageCode

        except urllib2.URLError, e:
            if hasattr(e,"reason"):
                print u"连接博客园失败，错误原因",e.reason
                return None

    #传入某一页代码，返回本页的文章信息列表
    def getPageItems(self,pageIndex):
        pageCode = self.getPage(pageIndex)
        if not pageCode:
            print "页面加载失败……"
            return None
        if self.pattern == None:
            self.pattern = re.compile('<div.*?post_item">.*?<span.*?diggnum".*?">(.*?)</span>.*?<div.*?post_item_body">.*?<h3.*?_blank">(.*?)</a>.*?<div.*?post_item_foot">' +
                         '.*?<a.*?">(.*?)</a>.*?(\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}).*?<span.*?<a.*?">[\s\S]*?\((.*?)\)</a>.*?<span.*?<a.*?">[\s\S]*?\((.*?)\)</a>',re.S)
            #self.pattern = re.compile('<div.*?post_item">.*?<span.*?diggnum".*?">(\d*)</span>.*?<div.*?post_item_body">.*?<h3.*?_blank">(.*?)</a>.*?<div.*?post_item_foot">' +
            #             '.*?<a.*?">(.*?)</a>.*?(\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}).*?<span.*?<a.*?">[\s\S]*?\((\d*)\)</a>.*?<span.*?<a.*?">[\s\S]*?\((\d*)\)</a>',re.S)
        items = re.findall(self.pattern,pageCode)
        pageStories = []
        #用来存储正则表达式匹配的信息
        for item in items:
            pageStories.append([item[0].strip(),item[1].strip(),item[2].strip(),item[3].strip()+':00',item[4].strip(),item[5].strip()])

        return pageStories

    #加载页面，提取内容，加入到列表中
    def loadPage(self,pageIndex):
        while self.pageIndex <= pageIndex:
            pageStories = self.getPageItems(self.pageIndex)
            self.stories.extend(pageStories)
            self.pageIndex += 1
        return self.stories



    #开始方法
    def start(self):
        page = 100
        self.loadPage(page)
        #for item in self.stories:
        #    print item[0],item[1],item[2],item[3],item[4],item[5]


#spider = Spider()
#spider.start()

