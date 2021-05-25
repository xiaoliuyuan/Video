# -*- coding: utf-8 -*

import os

# 固定参数
options = {
    "port": 8661
}
BASE_DIRS = os.path.dirname(__file__)
# 配置
settings = {
    "debug": False,
    'static_path': os.path.join(BASE_DIRS, "static"),
    'template_path': os.path.join(BASE_DIRS, 'template'),
}
# 数据库配置
mysql = {
            "host": "localhost",
            "user": "root",
            'passwd': "root",
            'dbName': 'test',
}