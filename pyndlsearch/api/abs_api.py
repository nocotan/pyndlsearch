# -*- coding: utf-8 -*-
""" APIの抽象クラス."""

from abc import abstractmethod
from abc import ABCMeta


class AbstractAPI(metaclass=ABCMeta):

    @abstractmethod
    def make_query(self):
        pass

    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def parse(self):
        pass
