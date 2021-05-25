# -*-  conding: utf-8 -*-

# Author: 
# Datetime : 
# software: PyCharm

from tornado.web import RequestHandler

class Ceshi(RequestHandler):
    def get(self, *args, **kwargs):
        STU = self.application.db.get_obj('select * from stu', 'stu')




