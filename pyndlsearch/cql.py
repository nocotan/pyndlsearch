# -*- coding: utf-8 -*-


class CQL(object):
    """ 検索クエリ. """
    query = ''

    """ データプロバイダID. """
    dpid = ''

    """ データプロバイダグループID. """
    dpgroupid = ''

    """ タイトル. """
    title = ''

    """ 作成者. """
    creator = ''

    """ 出版社. """
    publisher = ''

    """ 分類(NDC,NDLC,LCC,DCC,UDC) """
    ndc = ''

    """ 分類(NDLC) """
    ndlc = ''

    """ 内容記述. """
    description = ''

    """ 主題. """
    subject = ''

    """ ISBN. """
    isbn = ''

    """ ISSN. """
    issn = ''

    """ 全国書誌番号. """
    jpno = ''

    """ 開始出版年月 (YYYY-MM-DDD). """
    fromdate = ''

    """ 終了出版年月日 (YYY-MM-DDD). """
    untildate = ''

    """ 検索対象項目は国立国会図書館サーチの簡易検索と同一. """
    anywhere = ''

    """ 国立国会図書館サーチ内部での書誌のアイテム番号. """
    itemno = ''

    """ 資料種別.
    国立国会図書館サーチの詳細検索の資料種別に対応
    '1': 本
    '2': 記事
    '3': 新聞
    '4': 児童書
    '5': レファレンス情報
    '6': デジタル資料
    '7': その他
    '8': 障害者向け資料
    '9': 立法情報
    """
    mediatype = ''

    """ ソートの基準となる参照名を記述する.
    [title|creator|created_at|modified_date|issued_date]
    /[sort.ascending|sort.descending]
    """
    sortBy = ''

    def __init__(self, query=''):
        self.query = query

    def is_empty(self, param):
        return True if param is '' else False

    def is_empty_query(self):
        return True if self.query is '' else False

    def commit(self):
        if not self.is_empty(self.dpid):
            self.query += 'dpid%3d"{}"'.format(self.dpid)

        if not self.is_empty(self.dpgroupid):
            if self.is_empty_query():
                self.query += 'dpgroupid%3d"{}"'.format(self.dpgroupid)
            else:
                self.query += ' AND dpgroupid="{}"'.format(self.dpgroupid)

        if not self.is_empty(self.title):
            if self.is_empty_query():
                self.query += 'title%3d"{}"'.format(self.title)
            else:
                self.query += ' AND title="{}"'.format(self.title)

        if not self.is_empty(self.creator):
            if self.is_empty_query():
                self.query += 'creator%3d"{}"'.format(self.creator)
            else:
                self.query += ' AND creator="{}"'.format(self.creator)

        if not self.is_empty(self.publisher):
            if self.is_empty_query():
                self.query += 'publisher%3d"{}"'.format(self.publisher)
            else:
                self.query += ' AND publisher="{}"'.format(self.publisher)

        if not self.is_empty(self.ndc):
            if self.is_empty_query():
                self.query += 'ndc%3d"{}"'.format(self.ndc)
            else:
                self.query += ' AND ndc="{}"'.format(self.ndc)

        if not self.is_empty(self.ndlc):
            if self.is_empty_query():
                self.query += 'ndlc%3d"{}"'.format(self.ndlc)
            else:
                self.query += ' AND ndlc="{}"'.format(self.ndlc)

        if not self.is_empty(self.description):
            if self.is_empty_query():
                self.query += 'description%3d"{}"'.format(self.description)
            else:
                self.query += ' AND description="{}"'.format(self.description)

        if not self.is_empty(self.subject):
            if self.is_empty_query():
                self.query += 'subject%3d"{}"'.format(self.subject)
            else:
                self.query += ' AND subject="{}"'.format(self.subject)

        if not self.is_empty(self.isbn):
            if self.is_empty_query():
                self.query += 'isbn%3d"{}"'.format(self.isbn)
            else:
                self.query += ' AND isbn="{}"'.format(self.isbn)

        if not self.is_empty(self.issn):
            if self.is_empty_query():
                self.query += 'issn%3d"{}"'.format(self.issn)
            else:
                self.query += ' AND issn="{}"'.format(self.issn)

        if not self.is_empty(self.jpno):
            if self.is_empty_query():
                self.query += 'jpno%3d"{}"'.format(self.jpno)
            else:
                self.jpno += ' AND jpno="{}"'.format(self.jpno)

        if not self.is_empty(self.fromdate):
            if self.is_empty_query():
                self.query += 'from%3d"{}"'.format(self.fromdate)
            else:
                self.query += ' AND from="{}"'.format(self.fromdate)

        if not self.is_empty(self.untildate):
            if self.is_empty_query():
                self.query += 'until%3d"{}"'.format(self.untildate)
            else:
                self.query += ' AND until="{}"'.format(self.untildate)

        if not self.is_empty(self.itemno):
            if self.is_empty_query():
                self.query += 'itemno%3d"{}"'.format(self.itemno)
            else:
                self.query += ' AND itemno="{}"'.format(self.itemno)

        if not self.is_empty(self.mediatype):
            if self.is_empty_query():
                self.query += 'mediatype%3d"{}"'.format(self.mediatype)
            else:
                self.query += ' AND mediatype="{}"'.format(self.mediatype)

        if not self.is_empty(self.sortBy):
            if self.is_empty_query():
                self.query += 'sortBy%3d"{}"'.format(self.sortBy)
            else:
                self.query += ' AND sortBy="{}"'.format(self.sortBy)

    def payload(self):
        self.commit()
        return self.query
