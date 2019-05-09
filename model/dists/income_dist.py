
'''
class IncomeDist
'''

import numpy as np

ALPHA = 1.4654
X_MIN = 1.
ERROR = 0.0

class IncomeDist:
    '''
    Information about the income (Pareto) distribution.
    '''
    alpha = ALPHA
    x_min = X_MIN
    error = ERROR

    @staticmethod
    def draw_income():
        return IncomeDist.x_min * (1. + np.random.pareto(IncomeDist.alpha))

    @staticmethod
    def estimate_param(values):
        x_min = min(values)
        n = len(values)
        alpha = n/np.sum(np.log(values) - np.log(x_min))
        error = alpha/np.sqrt(n)
        return alpha, x_min, error
    '''
    @staticmethod
    def cumulative_probability(value):
        if value < IncomeDist.x_min:
            return 0.0
        return 1. - (IncomeDist.x_min/value)**IncomeDist.alpha

    @staticmethod
    def gini():
        if IncomeDist.alpha <= 1.0:
            return np.inf
        return 1./(2. * IncomeDist.alpha - 1.)

    @staticmethod
    def mean():
        if IncomeDist.alpha <= 1.0:
            return np.inf
        return (IncomeDist.alpha/(IncomeDist.alpha - 1.)) * IncomeDist.x_min

    @staticmethod
    def median():
        return IncomeDist.x_min * (np.power(2., (1./IncomeDist.alpha)))

    @staticmethod
    def quantile_function(prob):
        if prob == 1.:
            return np.inf
        return IncomeDist.x_min/np.power(1.- prob, (1./IncomeDist.alpha))

    @staticmethod
    def reset_param():
        IncomeDist.alpha = ALPHA
        IncomeDist.x_min = X_MIN
        IncomeDist.error = ERROR

    @staticmethod
    def update_param(alpha,x_min,error):
        IncomeDist.alpha = alpha
        IncomeDist.x_min = x_min
        IncomeDist.error = error
    '''