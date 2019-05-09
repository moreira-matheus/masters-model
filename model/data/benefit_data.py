
'''
classes CCB (Continuous Cash Benefit) and BFP (Bolsa Familia Program)
'''

class CCB:
    elderly_age = 65
    elderly_ratio = 0.1138
    disabled_ratio = 0.00912
    disabled_prob = 0.239
    min_wage_ratio = 1.0

#BFP_BASIC = 0.5
#BFP_VARIABLE = 0.2

class BFP:
    #fem_prob = 0.51
    beneficiary_ratio = 0.065566
    min_wage_ratio = 0.19    #97/510

'''
    @staticmethod
    def value():
        values = [BFP_BASIC, BFP_BASIC + BFP_VARIABLE, 
                  BFP_BASIC + 2*BFP_VARIABLE, BFP_BASIC + 3*BFP_VARIABLE,
                  BFP_BASIC + 4*BFP_VARIABLE, BFP_BASIC + 5*BFP_VARIABLE]
        freqs = [0.25, 0.15, 0.15, 0.15, 0.15, 0.15]
        return choice(values, p=freqs)        
'''