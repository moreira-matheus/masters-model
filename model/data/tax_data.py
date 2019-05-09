
'''
class TaxData
'''

#from numpy import array

class TaxData:
    '''
    Data about the income tax.
    '''
    due_rates = [0.0, 0.075, 0.15, 0.225, 0.275]
    # [ 44.59; 21.62; 10.79; 6.13; 16.87 ]
    quantiles = [0.4459, 0.6621, 0.77, 0.8313]
'''
    @staticmethod
    def get_due_rate(quantile):
        index = sum(quantile > array(TaxData.quantiles))
        return TaxData.due_rates[index]
'''