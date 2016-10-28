# -*- coding: utf-8 -*-
""" Main NDL Search client.
"""
from .api.sru import SRUApi


class NDLSearchClient(object):
    def __init__(self, query):
        self.query = SRUApi(query.payload())

    def get_response(self):
        return self.query.get()
