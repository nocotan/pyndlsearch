# -*- coding: utf-8 -*-

from pyndlsearch.client import SRUClient
from pyndlsearch.cql import CQL


if __name__ == '__main__':
    cql = CQL()
    cql.title = 'Python'
    cql.fromdate = '2000-10-10'
    print(cql.payload())

    client = SRUClient(cql)
    client.set_maximum_records(10)
    print(client)
    #res = client.get_response()
    #print(res.text)

    # SRU
    srres = client.get_srresponse()

    for record in srres.records:
        print("title:", record.recordData.title)
        print("creator:", record.recordData.creator)
        print("description:", record.recordData.description)
