# -*- coding: utf-8 -*-

# Copyright (c) 2015 cagayakemiracl All Rights Reserved.
# $Mail: <cagayakemiracl@gmail.com>

import random

from .group import Group


class Children(Group):

    def mutate(self):
        [child.mutate() for child in self if random.random() < self.spec.pm]

        return self
