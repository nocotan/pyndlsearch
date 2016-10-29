# pyndlsearch
[![MIT License](http://img.shields.io/badge/license-MIT-blue.svg?style=flat)](LICENSE)　　

[国立国会会図書館サーチ](http://iss.ndl.go.jp/information/api/)のPythonラッパー  

### Requirements
- Python 3.5.2
- requests 2.10.0

### Instration

```
pip install pyndlsearch
```

### SRU(Search/Retrieve Via URL)
http://iss.ndl.go.jp/api/sru
- version: 1.2
- query: CQL
- startRecord: default 1
- maximumRecords: default 200
- recordPacking: default "string"
- recordSchema: default "dc"
- inprocess: default "false"
- onlyBib: default "false"

#### Usage

```python:sample
# -*- coding: utf-8 -*-

from pyndlsearch.client import SRUClient
from pyndlsearch.cql import CQL


if __name__ == '__main__':
    # CQL検索クエリの組み立て
    cql = CQL()
    cql.title = 'Python'
    cql.fromdate = '2000-10-10'
    #print(cql.payload())

    # NDL Searchクライアントの設定
    client = SRUClient(cql)
    client.set_maximum_records(2)
    #print(client)
    
    # get_response()ではxml形式で取得可能
    #res = client.get_response()
    #print(res.text)

    # SRU
    srres = client.get_srresponse()

    for record in srres.records:
        print(record.recordData.title)
        print(record.recordData.creator)

```

- 出力結果

```
10日でおぼえるPython入門教室
穂苅実紀夫, 寺田学, 中西直樹, 堀田直孝, 永井孝 著
1500円定番ARMマイコン・ボードで試して合点! アプリはスクリプトで柔軟に!マイコン用MicroPythonプログラミング
中村 晋一郎
```

### 注意
- デフォルトだと200件取りに行ってしまうためちゃくちゃ遅いです
- CRUClientの最大件数を調節してください
