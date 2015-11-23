# -*- coding: utf-8 -*-

# Copyright (c) 2015 cagayakemiracl All Rights Reserved.
# $Mail: <cagayakemiracl@gmail.com>

from copy import deepcopy
import random

from deap import base


class _Fitness(base.Fitness):
    pass


class Individual(list):

    def __init__(self, chromosome, spec):
        list.__init__(self, chromosome)

        _Fitness.weights = spec.weights
        self.spec = spec
        self.fitness = _Fitness()

        return

    def evaluate(self):
        self.fitness.values = self.spec.evaluate(self)

        return self.fitness.values

    def mate(self, other):
        child1 = deepcopy(self)
        child2 = deepcopy(other)

        if random.random() < self.spec.pc:
            self.spec.mate(child1, child2)

        return child1, child2

    def mutate(self):
        if random.random() < self.spec.pm:
            self.spec.mutate(self)

        return self
