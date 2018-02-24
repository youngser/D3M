#!/usr/bin/env python

# numclust.py
# Copyright (c) 2017. All rights reserved.

import os
import rpy2.robjects as robjects
import rpy2.robjects.numpy2ri
rpy2.robjects.numpy2ri.activate()
import numpy as np

from typing import Sequence, TypeVar
from primitive_interfaces.transformer import TransformerPrimitiveBase

Input = np.ndarray
Output = int
Params = TypeVar('Params')

class NumberOfClusters(TransformerPrimitiveBase[Input, Output, Params]):
    """
    TODO: YP Document
    """

    def produce(self, *, inputs: Sequence[Input]) -> Sequence[Output]:
        """
        TODO: YP description

        **Positional Arguments:**

        X:
            - TODO: YP description
        """

        path = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                "numclust.interface.R")
        cmd = """
        source("%s")
        fn <- function(X) {
            numclust.interface(X)
        }
        """ % path

        return int(robjects.r(cmd)(inputs)[0])
