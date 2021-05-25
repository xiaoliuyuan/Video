# -*- coding: utf-8 -*
from tornado import ioloop, httpserver
from video_website import config
from video_website.application import Urls



# APP启动入口
if __name__ == '__main__':
    APP = Urls()
    http_index = httpserver.HTTPServer(APP)
    http_index.bind(config.options['port'])
    http_index.start(1)
    ioloop.IOLoop.current().start()