# -*- coding: utf-8 -*-

# Copyright (c) 2015 cagayakemiracl All Rights Reserved.
# $Mail: <cagayakemiracl@gmail.com>

from .base_factory import BaseFactory


class Contractor(BaseFactory):
    instance = None

    def __init__(self, subcontract, spec, n):
        self.subcontract = subcontract
        self.spec = spec
        self.n = n

        return

    def new_instance(self):
        self.subcontract.spec = self.spec
        material = self.subcontract.make(self.n)

        return self.instance(material, self.spec)
