# -*- coding: utf-8 -*-

# Copyright (c) 2015 cagayakemiracl All Rights Reserved.
# $Mail: <cagayakemiracl@gmail.com>

from .base_factory import BaseFactory


class Subcontract(BaseFactory):
    instance = None

    def new_instance(self):
        return self.instance()
