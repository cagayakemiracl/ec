# -*- coding: utf-8 -*-

# Copyright (c) 2015 cagayakemiracl All Rights Reserved.
# $Mail: <cagayakemiracl@gmail.com>

from abc import ABCMeta, abstractmethod


class GA:
    __metaclass__ = ABCMeta

    def __init__(self, bits, pc, pm, weights, m):
        self.bits = bits
        self.pc = pc
        self.pm = pm
        self.weights = weights
        self.m = m

        return

    @abstractmethod
    def evaluate(individual):
        pass

    @abstractmethod
    def judgeExitCondition(population, i):
        pass

    @abstractmethod
    def selectReproduction(population):
        pass

    @abstractmethod
    def mate(child1, child2):
        pass

    @abstractmethod
    def mutate(child):
        pass

    @abstractmethod
    def selectSurvival(parents, children):
        pass
