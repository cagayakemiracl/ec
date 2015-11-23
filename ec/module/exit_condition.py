# -*- coding: utf-8 -*-

# Copyright (c) 2015 cagayakemiracl All Rights Reserved.
# $Mail: <cagayakemiracl@gmail.com>

from .select import selectBest


def hasFoundOneBest(population, i, limit):
    if i == limit:
        return True

    best_individual = selectBest(population)

    if best_individual.fitness.values[0] >= 1:
        return True

    return False
