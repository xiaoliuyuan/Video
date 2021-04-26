# -*- coding: utf-8 -*
import pymysql

# 固定参数
options = {
    "port": 8886
}

# 配置
settings = {
    "debug": True,
    "mysql": {
            "host": "127.0.0.1",
            'database': "root",
            "user": "root",
            'password': "mysql"

        }
}
