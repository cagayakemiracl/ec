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

    def evolve(self, population, i):
        if self.spec.judgeExitCondition(population, i):
            self.count = i
            return False

        parents = population.selectReproduction()
        children = parents.mate()
        children.mutate()
        children.evaluate()
        population[:] = self.spec.selectSurvival(
            parents, children)

        return True

    def end_of_loop(self):
        raise StopIteration

    def evolveLoop(self, population=None):
        if population is None:
            population = self.makePopulations(n=1)[0]

        try:
            [i if self.evolve(population, i) else self.end_of_loop()
             for i in itertools.count()]
        except:
            pass

        return population, self.count
