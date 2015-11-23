# -*- coding: utf-8 -*-

# Copyright (c) 2015 cagayakemiracl All Rights Reserved.
# $Mail: <cagayakemiracl@gmail.com>

from abc import ABCMeta, abstractmethod


class BaseFactory:
    __metaclass__ = ABCMeta

    def make(self, n):
        return [self.new_instance() for _ in range(n)]

    @abstractmethod
    def new_instance(self):
        pass
