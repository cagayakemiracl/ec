# -*- coding: utf-8 -*-

# Copyright (c) 2015 cagayakemiracl All Rights Reserved.
# $Mail: <cagayakemiracl@gmail.com>

from .base.group import Group
from .base.parents import Parents


class Population(Group):

    def selectReproduction(self):
        return Parents(self.spec.selectReproduction(self), self.spec)
