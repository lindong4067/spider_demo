# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os

class SpiderDemoPipeline(object):
    def process_item(self, item, spider):
        return item


class StockPipeline(object):
    def __init__(self):
        self.file = open("executive_prep.csv", "a+")

    def process_item(self, item, spider):
        # 类加载时创建文件，判断文件是否为空

        # 判断文件是否为空，为空写：
        if os.path.getsize("executive_prep.csv"):
            self.write_content(item)
        else:
            self.file.write("高管姓名，性别，年龄，股票代码，职位\n")
        self.file.flush()
        return item

    def write_content(self, item):
        names = item["names"]
        sexs = item["sexs"]
        ages = item["ages"]
        codes = item["codes"]
        leaders = item["leaders"]
        result = ""
        for i in range(len(names)):
            result = names[i] + "," + sexs[i] + "," + ages[i] + "," + codes[i] + "," + leaders[i] + "\n"
            self.file.write(result)
