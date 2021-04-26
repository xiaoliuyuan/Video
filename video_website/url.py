from tornado.web import Application
from video_website.views import index
from video_website.views import play_video
from video_website import config
# 路由系统
class Url(Application):
    def __init__(self):
        App_Url = {
            (r'/', index.IndexHandler),
            (r'/play_video', play_video.Play_Vide_Handler)
        }
        super(Url, self).__init__(App_Url, **config.settings)
