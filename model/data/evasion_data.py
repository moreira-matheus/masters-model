
'''
class EvasionData
'''

#from numpy import array

class EvasionData:
    '''
    Data about tax evasion.
    '''
    avg_rates = [.000, .006, .035, .088, .118, .110, .082, .067]
    quantiles = [0.210, 0.507, 0.783, 0.916, 0.973, 0.992, 0.997]
    #quantiles = [0.20969592, 0.50719355, 0.78273750, 0.91567774,
     #              0.97257064, 0.99214333, 0.99730358]
'''
    @staticmethod
    def get_avg_rate(quantile):
        index = sum(quantile > array(EvasionData.quantiles))
        return EvasionData.avg_rates[index]
'''