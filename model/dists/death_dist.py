'''
class DeathDist
'''

from numpy.random import normal

class DeathDist:
    '''
    Information about the distribution of ages at death.
    '''
    mean = 79.158
    std_dev = 3.979

    @staticmethod
    def draw_age_at_death():
        '''
        Draws an age at death from the distribution.
        '''
        return int(normal(loc=DeathDist.mean,scale=DeathDist.std_dev))
