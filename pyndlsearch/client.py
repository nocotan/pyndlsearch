# -*- coding: utf-8 -*-
""" Main NDL Search client.
"""

from abc import abstractmethod
from abc import ABCMeta

from .api.sru import SRUApi


class AbstractClient(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, query):
        self.api = None
        self.query = query

    @abstractmethod
    def get_response(self):
        return self.query.get()


class SRUClient(AbstractClient):
    def __init__(self, query):
        self.api = SRUApi(query.payload())

    def get_response(self):
        return self.api.get()

    def get_srresponse(self):
        return self.api.parse()

    def set_start_record(self, startRecord):
        self.api.startRecord = startRecord

    def set_maximum_records(self, maximumRecords):
        self.api.maximumRecords = maximumRecords

    def set_record_packing(self, recordPacking):
        self.api.recordPacking = recordPacking

    def set_record_schema(self, recordSchema):
        self.api.recordSchema = recordSchema

    def set_inprocess(self, inprocess):
        self.api.inprocess = inprocess

    def set_only_bib(self, onlyBib):
        self.api.onlyBib = onlyBib
