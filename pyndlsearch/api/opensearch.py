# -*- coding: utf-8 -*-
""" openSearch APIクラス """

from .abs_api import AbstractAPI


class OpenSearchApi(AbstractAPI):

    URL = 'http://iss.ndl.go.jp/api/opensearch'

    def __init__(self):

        """ データプロバイダID. """
        self.dpid = ''

        """ データプロバイダグループID. """
        self.dpgroupid = ''

        """ すべての項目を対象に検索. """
        self.any = ''

        """ タイトル. """
        self.title = ''

        """ 作成者. """
        self.creator = ''

        """ 出版者. """
        self.publisher = ''

        """ 分類(NDC). """
        self.ndc = ''

        """ 開始出版年月日(YYYY-MM-DD). """
        self.fromdate = ''

        """ 終了年月日(YYYY-MM-DD). """
        self.untildate = ''

        """ 出力レコード上限値. """
        self.cnt = 200

        """ レコード取得開始位置. """
        self.idx = 1

        """ ISBN. """
        self.isbn = ''

        """ 資料種別.
        '1': 本
        '2': 記事・論文
        '3': 新聞
        '4': 児童書
        '5': レファレンス情報
        '6': デジタル資料
        '7': その他
        '8': 障害者向け資料
        '9': 立法情報
        """
        self.mediatype = ''

    def get():
        pass
