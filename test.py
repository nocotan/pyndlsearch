# -*- coding: utf-8 -*-

from pyndlsearch.client import NDLSearchClient
from pyndlsearch.cql import CQL


if __name__ == '__main__':
    cql = CQL()
    cql.title = 'Python'
    print(cql.payload())

    client = NDLSearchClient(cql)
    print(client)
    res = client.get_response()

    print(res.text)
