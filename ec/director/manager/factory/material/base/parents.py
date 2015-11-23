# -*- coding: utf-8 -*-

# Copyright (c) 2015 cagayakemiracl All Rights Reserved.
# $Mail: <cagayakemiracl@gmail.com>

import random
from copy import deepcopy

from .group import Group
from .children import Children


class Parents(Group):

    def mate(self):
        """
        親集団から偶数奇数でペアを作り親を選択
        ペアで交叉をして子を２つ作る
        """

        children = [deepcopy(x) for x in self]
        [child1.mate(child2) for child1, child2 in zip(
            children[::2], children[1::2]) if random.random() < self.spec.pc]

        return Children(children, self.spec)
