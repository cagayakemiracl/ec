# -*- coding: utf-8 -*-

# Copyright (c) 2015 cagayakemiracl All Rights Reserved.
# $Mail: <cagayakemiracl@gmail.com>

from .group import Group
from .children import Children


class Parents(Group):

    def mate(self):
        """
        親集団から偶数奇数でペアを作り親を選択
        ペアで交叉をして子を２つ作る
        Parents.mate(self)の返り値がlistのためflattenする
        """
        children = [child for childs in [parent1.mate(
            parent2) for parent1, parent2 in zip(self[::2], self[1::2])] for child in childs]

        return Children(children, self.spec)
