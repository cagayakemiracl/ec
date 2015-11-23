#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (c) 2015 cagayakemiracl All Rights Reserved.
# $Mail: <cagayakemiracl@gmail.com>

from deap import tools

from ec.spec.sga import GA as Spec
from ec.director.ga import GA as Director
from ec.module.select import selectBest


def judgeExitCondition(pop, i):
    if i == 40:
        return True

    return False


def main():
    spec = Spec(bits=100, pc=0.5, pm=0.2, weights=(1.0,), m=300)
    spec.evaluate = lambda ind: (sum(ind),)
    spec.judgeExitCondition = judgeExitCondition
    spec.selectReproduction = lambda pop: tools.selTournament(
        pop, len(pop), tournsize=3)
    spec.mate = tools.cxTwoPoint
    spec.mutate = lambda ind: tools.mutFlipBit(ind, indpb=0.05)
    spec.selectSurvival = lambda parents, children: children

    director = Director(spec)
    population, i = director.evolveLoop()
    best = selectBest(population)

    print("evolving times: ", i)
    print("best individual: %s %s" % (best, best.fitness.values[0]))

    return

if __name__ == '__main__':
    main()
