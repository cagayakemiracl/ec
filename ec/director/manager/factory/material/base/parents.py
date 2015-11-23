# -*- coding: utf-8 -*-

# Copyright (c) 2015 cagayakemiracl All Rights Reserved.
# $Mail: <cagayakemiracl@gmail.com>


from .group import Group
from .children import Children


class Parents(Group):

    def mate(self):
        children = []

        for parent1, parent2 in zip(self[::2], self[1::2]):
            child1, child2 = parent1.mate(parent2)
            children.append(child1)
            children.append(child2)

        return Children(children, self.spec)
