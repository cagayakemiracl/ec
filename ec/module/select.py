# -*- coding: utf-8 -*-

# Copyright (c) 2015 cagayakemiracl All Rights Reserved.
# $Mail: <cagayakemiracl@gmail.com>

from deap import tools


def selectBest(population):
    return tools.selBest(population, 1)[0]


def selectChildrenOnly(parents, children):
    return children
