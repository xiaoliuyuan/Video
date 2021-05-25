# -*- coding: utf-8 -*
# 播放视频视图
# 作者：刘源
# 日期：2021年4月19日


from tornado.web import RequestHandler

# 首页
class Play_Vide_Handler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write('PLay video 11')
    def post(self, *args, **kwargs):
        self.write('ggg')





