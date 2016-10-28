# -*- coding: utf-8 -*-
""" SRU: Search/Retrieval via URL APIクラス."""

import requests
from .abs_api import AbstractAPI


class SRUResponse(object):
    def __init__(self):
        pass

class SRUApi(AbstractAPI):
    URL = 'http://iss.ndl.go.jp/api/sru'

    def __init__(self, query):
        self.operation = 'searchRetrieve'
        self.version = '1.2'

        """ 検索条件(CQL). """
        self.query = query

        """ 開始位置. """
        self.startRecord = '1'

        """ 最大取得件数. """
        self.maximumRecords = '200'

        """ xml or string. """
        self.recordPacking = 'string'

        """ 取得データのスキーマ. """
        self.recordSchema = 'dc'

        """ NDL新着書誌情報のみを取得. """
        self.inprocess = 'false'

        """ 書誌情報のみを取得. """
        self.onlyBib = 'false'

    def make_query(self):
        self.query = 'operation={}&query={}'.format(
            self.operation,
            self.query,
        )

        if self.startRecord != '1':
            self.query += '&startRecord={}'.format(self.startRecord)

        if self.maximumRecords != '200':
            self.query += '&maximumRecords={}'.format(self.maximumRecords)

        if self.recordPacking != 'string':
            self.query += '&recordPacking={}'.format(self.recordPacking)

        if self.recordSchema != 'dc':
            self.query += '&recordSchema={}'.format(self.recordSchema)

        if self.inprocess != 'false':
            self.query += '&inprocess={}'.format(self.inprocess)

        if self.onlyBib != 'false':
            self.query += '&onlyBib={}'.format(self.onlyBib)

    def get(self):
        self.make_query()
        res = requests.get(self.URL, params=self.query)

        return res
