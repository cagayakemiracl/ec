# -*- coding: utf-8 -*-

# Copyright (c) 2015 cagayakemiracl All Rights Reserved.
# $Mail: <cagayakemiracl@gmail.com>

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
        self.spec.mate(self, other)
        del self.fitness.values, other.fitness.values

        return self, other

    def mutate(self):
        self.spec.mutate(self)
        del self.fitness.values

        return self
