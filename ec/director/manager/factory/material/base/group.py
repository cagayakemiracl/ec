# -*- coding: utf-8 -*-

# Copyright (c) 2015 cagayakemiracl All Rights Reserved.
# $Mail: <cagayakemiracl@gmail.com>


class Group(list):

    def __init__(self, individuals, spec):
        list.__init__(self, individuals)

        self.spec = spec

        return

    def evaluate(self):
        [ind.evaluate() for ind in self if not ind.fitness.valid]

        return self
