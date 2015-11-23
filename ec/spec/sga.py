# -*- coding: utf-8 -*-

# Copyright (c) 2015 cagayakemiracl All Rights Reserved.
# $Mail: <cagayakemiracl@gmail.com>

from deap import tools

from .ga import GA


class SGA(GA):

    def __init__(self, bits, pc, pm, m):
        super().__init__(bits=bits, pc=pc, pm=pm, weights=(1.0,), m=m)

        return

    @staticmethod
    def selectReproduction(pop):
        return tools.selRoulette(pop, len(pop))

    @staticmethod
    def mate(ind1, ind2):
        return tools.cxOnePoint(ind1, ind2)

    @staticmethod
    def mutate(ind):
        return tools.mutFlipBit(ind, 1 / ind.spec.bits)

    @staticmethod
    def selectSurvival(parents, children):
        return children
