# -*- coding: utf-8 -*-

# Copyright (c) 2015 cagayakemiracl All Rights Reserved.
# $Mail: <cagayakemiracl@gmail.com>

from .base.subcontract import Subcontract
from .material.geno import Geno as Material


class Geno(Subcontract):
    instance = Material.random
