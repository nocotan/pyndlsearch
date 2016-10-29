# -*- coding: utf-8 -*-
""" SRU: Search/Retrieval via URL APIクラス."""

import requests
from xml.etree import ElementTree

from .abs_api import AbstractAPI


class RecordData(object):
    title = ''
    creator = ''
    descriptions = {}
    publisher = ''
    language = ''

    def __init__(self):
        pass

class Record(object):
    recordSchema = ''
    recordPacking = ''
    recordData = None
    recordPosition = 0

    def __init__(self):
        pass


class extraResponseData(object):
    facets = {}

    def __init__(self):
        pass


class searchRetrieveResponse(object):
    version = ''
    numberOfRecords = 0
    nextRecordPosition = ''
    extraResponseData = None
    records = []

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

    def parse(self):
        res = searchRetrieveResponse()
        extra_resdata = extraResponseData()

        root = ElementTree.fromstring(self.get().text)

        res.version = root.find('{http://www.loc.gov/zing/srw/}version').text
        res.numberOfRecords = root.find('{http://www.loc.gov/zing/srw/}numberOfRecords').text
        res.nextRecordPosition = root.find('{http://www.loc.gov/zing/srw/}numberOfRecords').text

        # extraResponseData
        ext_root = ElementTree.fromstring(root.find('{http://www.loc.gov/zing/srw/}extraResponseData').text)
        for child in ext_root:

            name = child.get('name')
            if name == 'REPOSITORY_NO':
                repository_no = {}
                for child_repo in child:
                    repository_no[child_repo.get('name')] = child_repo.text

                extra_resdata.facets['REPOSITORY_NO'] = repository_no

            elif name == 'NDC':
                ndc = {}
                for child_ndc in child:
                    ndc[child_ndc.get('name')] = child_ndc.text

                extra_resdata.facets['NDC'] = ndc

            elif name == 'ISSUED_DATE':
                issued_date = {}
                for child_issued in child:
                    issued_date[child_issued.get('name')] = child_issued.text

                extra_resdata.facets['ISSUED_DATE'] = issued_date

            elif name == 'LIBRARY':
                library = {}
                for child_lib in child:
                    library[child_lib.get('name')] = child_lib.text

                extra_resdata.facets['LIBRARY'] = library

        # records
        records = []
        records_root = root.find('{http://www.loc.gov/zing/srw/}records')
        for record in records_root:
            tmp_record = Record()
            tmp_record.recordSchema= record.find('{http://www.loc.gov/zing/srw/}recordSchema').text
            tmp_record.recordPacking = record.find('{http://www.loc.gov/zing/srw/}recordPacking').text
            tmp_record.recordPosition = record.find('{http://www.loc.gov/zing/srw/}recordPosition').text

            tmp_record_data = RecordData()
            record_data_root = ElementTree.fromstring(record.find('{http://www.loc.gov/zing/srw/}recordData').text)

            title = record_data_root.find('{http://purl.org/dc/elements/1.1/}title')
            if title is not None:
                tmp_record_data.title = title.text

            creator = record_data_root.find('{http://purl.org/dc/elements/1.1/}creator')
            if creator is not None:
                tmp_record_data.creator = creator.text

            publisher = record_data_root.find('{http://purl.org/dc/elements/1.1/}publisher')
            if publisher is not None:
                tmp_record_data.publisher = publisher.text

            language = record_data_root.find('{http://purl.org/dc/elements/1.1/}language')
            if language is not None:
                tmp_record_data.language = language.text

            subject = record_data_root.find('{http://purl.org/dc/elements/1.1/}subject')
            if subject is not None:
                tmp_record_data.subject = subject.text

            descriptions = record_data_root.find('{http://purl.org/dc/elements/1.1/}description')
            if descriptions is not None:
                tmp_record_data.descriptions = descriptions

            tmp_record.recordData = tmp_record_data
            records.append(tmp_record)

        res.extraResponseData = extra_resdata
        res.records = records

        return res
