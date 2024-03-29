# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.pipelines.files import FilesPipeline
from scrapy.exceptions import DropItem
from scrapy import log


class SwissracesPipeline(object):
    def process_item(self, item, spider):
        return item


class MyFilesPipeline(FilesPipeline):

    def file_path(self, request, response=None, info=None):
        file_guid = request.meta['url'][0]
        log.msg(file_guid, level=log.DEBUG)
        return 'full/%s' % (file_guid)

    def get_media_requests(self, item, info):
        for file_url in item['file_urls']:
            yield scrapy.Request(file_url, meta=item)

    def item_completed(self, results, item, info):
        file_paths = [x['path'] for ok, x in results if ok]
        if not file_paths:
            raise DropItem("Item contains no files")
        item['file_paths'] = file_paths
        return item



