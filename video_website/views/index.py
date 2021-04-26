from tornado.web import RequestHandler

'''
首页视图
作者：刘源
日期：2021年4月19日
'''

# 首页
class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write('good study')
    def post(self, *args, **kwargs):
        self.write('ggg')