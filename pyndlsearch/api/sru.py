# -*- coding: utf-8 -*-
""" SRU: Search/Retrieval via URL APIクラス."""

import requests
from xml.etree import ElementTree

from .abs_api import AbstractAPI


class RecordData(object):
    title = None
    creator = None
    description = None
    publisher = None
    language = None
    issued_date = None
    series = None
    subject = None
    materialType = None


    def __init__(self):
        pass

class Record(object):
    recordSchema = None
    recordPacking = None
    recordData = None
    recordPosition = 0

    def __init__(self):
        pass


class extraResponseData(object):
    facets = {}

    def __init__(self):
        pass


class searchRetrieveResponse(object):
    version = None
    numberOfRecords = 0
    nextRecordPosition = None
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
        res.nextRecordPosition = root.find('{http://www.loc.gov/zing/srw/}nextRecordPosition').text

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
            if title is not None and title.text:
                tmp_record_data.title = title.text

            creator = record_data_root.find('{http://purl.org/dc/elements/1.1/}creator')
            if creator is not None and creator.text:
                tmp_record_data.creator = creator.text

            publisher = record_data_root.find('{http://purl.org/dc/elements/1.1/}publisher')
            if publisher is not None:
                tmp_record_data.publisher = publisher.text

            language = record_data_root.find('{http://purl.org/dc/elements/1.1/}language')
            if language is not None and language.text:
                tmp_record_data.language = language.text

            subject = record_data_root.find('{http://purl.org/dc/elements/1.1/}subject')
            if subject is not None and subject.text:
                tmp_record_data.subject = subject.text

            description = record_data_root.find('{http://purl.org/dc/elements/1.1/}description')
            if description is not None and description.text:
                tmp_record_data.description = description.text

            tmp_record.recordData = tmp_record_data
            records.append(tmp_record)

        res.extraResponseData = extra_resdata
        res.records = records

        return res

    def parse_dcndl(self):
        res = searchRetrieveResponse()
        extra_resdata = extraResponseData()

        root = ElementTree.fromstring(self.get().text)

        res.version = root.find('{http://www.loc.gov/zing/srw/}version').text
        res.numberOfRecords = root.find('{http://www.loc.gov/zing/srw/}numberOfRecords').text
        res.nextRecordPosition = root.find('{http://www.loc.gov/zing/srw/}nextRecordPosition').text

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
            recordData = record.find('{http://www.loc.gov/zing/srw/}recordData')
            record_data_root = recordData.find('{http://ndl.go.jp/dcndl/dcndl_simple/}dc')

            title = record_data_root.find('{http://purl.org/dc/elements/1.1/}title')
            if title is not None and title.text:
                tmp_record_data.title = title.text

            creator = record_data_root.findall('{http://purl.org/dc/elements/1.1/}creator')
            if creator is not None:
              creators = []
              for item in creator:
                creators.append(item.text)
              tmp_record_data.creator = creators

            publisher = record_data_root.find('{http://purl.org/dc/elements/1.1/}publisher')
            if publisher is not None:
                tmp_record_data.publisher = publisher.text

            language = record_data_root.find('{http://purl.org/dc/elements/1.1/}language')
            if language is not None and language.text:
                tmp_record_data.language = language.text

            issued_date = record_data_root.find('{http://purl.org/dc/terms/}issued')
            if issued_date is not None and issued_date.text:
                tmp_record_data.issued_date = issued_date.text

            series = record_data_root.find('{http://ndl.go.jp/dcndl/terms/}seriesTitle')
            if series is not None and series.text:
                tmp_record_data.series = series.text

            materialType = record_data_root.find('{http://ndl.go.jp/dcndl/terms/}seriesTitle')
            if series is not None and series.text:
                tmp_record_data.series = series.text

            subjects = record_data_root.findall('{http://purl.org/dc/elements/1.1/}subject')
            if subjects is not None:
              subject_dict = {}
              for element in subjects:
                  if element.attrib:
                      subject_dict[element.attrib['{http://www.w3.org/2001/XMLSchema-instance}type']] = element.text
                  tmp_record_data.subject = subject_dict

            description = record_data_root.find('{http://purl.org/dc/elements/1.1/}description')
            if description is not None and description.text:
                tmp_record_data.description = description.text

            tmp_record.recordData = tmp_record_data
            records.append(tmp_record)

        res.extraResponseData = extra_resdata
        res.records = records

        return res