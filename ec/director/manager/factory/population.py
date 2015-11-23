# -*- coding: utf-8 -*-

# Copyright (c) 2015 cagayakemiracl All Rights Reserved.
# $Mail: <cagayakemiracl@gmail.com>

from .base.contractor import Contractor
from .material.population import Population as Material


class Population(Contractor):
    instance = Material
