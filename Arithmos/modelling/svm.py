from Arithmos.classification import (
    SVMLearner as SVCLearner,
    LinearSVMLearner as LinearSVCLearner,
    NuSVMLearner as NuSVCLearner,
)
from Arithmos.modelling import SklFitter
from Arithmos.regression import SVRLearner, LinearSVRLearner, NuSVRLearner

__all__ = ['SVMLearner', 'LinearSVMLearner', 'NuSVMLearner']


class SVMLearner(SklFitter):
    __fits__ = {'classification': SVCLearner, 'regression': SVRLearner}


class LinearSVMLearner(SklFitter):
    __fits__ = {'classification': LinearSVCLearner, 'regression': LinearSVRLearner}


class NuSVMLearner(SklFitter):
    __fits__ = {'classification': NuSVCLearner, 'regression': NuSVRLearner}
