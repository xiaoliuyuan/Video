# -*-  conding: utf-8 -*-

# Author:  Liuyuan
# Datetime : 2021年5月25日
# software: PyCharm

import pymysql


# 数据库
class DataBase():
    def __init__(self, host, user, passwd,dbName):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.dbName = dbName

    # 连接
    def connet(self):
        self.db = pymysql.connect(host=self.host, user=self.user, password=self.passwd, database=self.dbName)
        self.cursor = self.db.cursor()

    # 断开
    def close(self):
        self.cursor.close()
        self.db.close()
    # 查
        # 查全部
    def get_all(self, sql_tell):
            res = ()
            try:
                self.connet()
                self.cursor.execute(sql_tell)
                res = self.cursor.fetchone()
                self.close()
            except:
                print('查询2失败')
            return res

    def get_one(self, sql_tell):
        res = None
        try:
            self.connet()
            self.cursor.execute(sql_tell)
            res = self.cursor.fetchone()
            self.close()
        except:
            print('失败')
        return res

# 返回元组
    def get_obj(self, sql_tell, tableName, *args):
        resList = []
        fieldsList = []
        if( len(args) > 0):
            for item in args:
                fieldsList.append(item)
        else:
            fieldssql = 'select COLUMN_NAME from information_schema.COLUMNS where table_name ="%s" and table_schema = "%s"' %(
                tableName, self.dbName)
            fields = self.get_all(fieldssql)
            for item in fields:
                fieldsList.append(item[0])
        # 执行
        res = self.get_all(sql_tell)
        for item in res:
            obj = {}
            count = 0
            print(str(item))
            for x in item:
                obj[fieldsList[count]] = x
                count += 1
            resList.append(obj)
        return resList



    def dgub(self):
        self.connet()
        self.cursor.execute("select * from stu;")
        res = self.cursor.fetchone()
        self.close()
        return res
