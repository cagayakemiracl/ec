# -*- coding: utf-8 -*-

# Copyright (c) 2015 cagayakemiracl All Rights Reserved.
# $Mail: <cagayakemiracl@gmail.com>

from .factory.geno import Geno
from .factory.individual import Individual
from .factory.population import Population as Factory


class Population:

    def __init__(self, spec):
        self.spec = spec

        self.buildFactory()

        return

    def buildFactory(self):
        geno = Geno()
        individual = Individual(geno, self.spec, self.spec.bits)
        population = Factory(individual, self.spec, self.spec.m)

        self.factory = population

        return self

    def make(self, n):
        self.factory.spec = self.spec

        return self.factory.make(n)
