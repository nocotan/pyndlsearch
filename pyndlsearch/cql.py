# -*- coding: utf-8 -*-


class CQL(object):
    def __init__(self):
        """ データプロバイダID. """
        self.dpid = ''

        """ データプロバイダグループID. """
        self.dpgroupid = ''

        """ タイトル. """
        self.title = ''

        """ 作成者. """
        self.creator = ''

        """ 出版社. """
        self.publisher = ''

        """ 分類(NDC,NDLC,LCC,DCC,UDC) """
        self.ndc = ''

        """ 分類(NDLC) """
        self.ndlc = ''

        """ 内容記述. """
        self.description = ''

        """ 主題. """
        self.subject = ''

        """ ISBN. """
        self.isbn = ''

        """ ISSN. """
        self.issn = ''

        """ 全国書誌番号. """
        self.jpno = ''

        """ 開始出版年月 (YYYY-MM-DDD). """
        self.fromday = ''

        """ 終了出版年月日 (YYY-MM-DDD). """
        self.untilday = ''

        """ 検索対象項目は国立国会図書館サーチの簡易検索と同一. """
        self.anywhere = ''

        """ 国立国会図書館サーチ内部での書誌のアイテム番号. """
        self.itemno = ''

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
        self.mediatype = ''

        """ ソートの基準となる参照名を記述する.
        [title|creator|created_at|modified_date|issued_date]
        /[sort.ascending|sort.descending]
        """
        self.sortBy = ''

    def payload(self):
        req = 'title%3d"{}"'.format(self.title)
        print (req)

        return req
