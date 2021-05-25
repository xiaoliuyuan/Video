# -*-  conding: utf-8 -*-

# Author:
# Datetime :
# software: PyCharm

from tornado.web import RequestHandler
# 首页
class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write('good study')
    def post(self, *args, **kwargs):
        self.write('ggg')