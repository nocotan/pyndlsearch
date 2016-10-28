# pyndlsearch
[![MIT License](http://img.shields.io/badge/license-MIT-blue.svg?style=flat)](LICENSE)　　

国立国会図書館サーチAPIのpythonラッパー  
[国立こ会図書館サーチ](http://iss.ndl.go.jp/information/api/)のPythonラッパー  

### Requirements
- Python 3.5.2
- requests 2.10.0

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
