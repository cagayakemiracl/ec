# -*- coding: utf-8 -*-

# Copyright (c) 2015 cagayakemiracl All Rights Reserved.
# $Mail: <cagayakemiracl@gmail.com>

import itertools

from .manager.population import Population


class GA:

    def __init__(self, spec):
        self.spec = spec
        self.manager = Population(self.spec)

        return

    def makePopulations(self, n):
        self.manager.spec = self.spec
        populations = self.manager.make(n)
        [population.evaluate() for population in populations]

        return populations

    def selectReproduction(self):
        self.parents = self.population.selectReproduction()

        return self.parents

    def mate(self):
        self.children = self.parents.mate()

        return self.children

    def mutate(self):
        self.children.mutate()

        return self.children

    def evaluate(self):
        self.children.evaluate()

        return self.children

    def selectSurvival(self):
        self.population[:] = self.spec.selectSurvival(
            self.parents, self.children)

        return self.population

    def evolve(self, population):
        self.population = population

        self.selectReproduction()
        self.mate()
        self.mutate()
        self.evaluate()
        self.selectSurvival()

        return self

    def evolveLoop(self, population=None):
        if population is None:
            population = self.makePopulations(n=1)[0]

        for i in itertools.count():
            if self.spec.judgeExitCondition(population, i):
                return population, i

            self.evolve(population)

        return None
