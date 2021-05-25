# -*-  conding: utf-8 -*-

# Author: Linyuan
# Datetime : 2021年5月25日
# software: PyCharm
from tornado.web import Application
from video_website.views import index
from video_website.views import play_video
from video_website.views import ceshi
from video_website import config
from video_website import Db

# 路由系统
class Urls(Application):
    def __init__(self):
        App_Urls = {
            (r'/', index.IndexHandler),
            (r'/play_video', play_video.Play_Vide_Handler),
            (r'/ceshi', ceshi.Ceshi)
        }
        super(Urls, self).__init__(App_Urls, **config.settings)
        self.db = Db.DataBase(config.mysql['host'], config.mysql['user'], config.mysql['passwd'],
    config.mysql['dbName'])
