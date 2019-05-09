
'''
class Government
'''

import random
from numpy import quantile
#from dists.income_dist import IncomeDist
from model.data.tax_data import TaxData
from model.data.evasion_data import EvasionData
from model.data.benefit_data import CCB, BFP

class Government:
    def __init__(self):
        self.revenue, self.expenses = 0.0, 0.0
        self.society = None

    def reset_accounts(self):
        self.revenue, self.expenses = 0.0, 0.0

    def collect_taxes(self):
        all_incomes = self.society.get_overall_incomes()
        
        tax_thresholds = [quantile(all_incomes,q) \
                          for q in TaxData.quantiles]
        evasion_thresholds = [quantile(all_incomes,q) \
                              for q in EvasionData.quantiles]
        for ind in self.society.population:
            income = ind.get_overall_income()
            tax_level = sum([income > t \
                             for t in tax_thresholds])
            
            evasion_level = sum([income > t \
                                 for t in evasion_thresholds])
            
            due_rate = TaxData.due_rates[tax_level]
            avg_rate = EvasionData.avg_rates[evasion_level]
            self.revenue += ind.pay_taxes(due_rate,avg_rate)

    def pay_benefits(self):
        sorted_inds = sorted(self.society.population,
                             key=lambda ind: ind.get_overall_income())
        min_value = sorted_inds[0].get_overall_income()
        num_ccbs = int(CCB.elderly_ratio*
                       sum([i.current_age>CCB.elderly_age \
                            for i in sorted_inds]))
        num_ccbs += int(CCB.disabled_ratio*self.society.size)
        num_bfps = int(BFP.beneficiary_ratio*self.society.size)

        for ind in sorted_inds:
            transfer = 0.0

            if ((ind.current_age>=CCB.elderly_age) or
                (random.random()<CCB.disabled_prob)) and num_ccbs>0:
                transfer += CCB.min_wage_ratio * min_value
                self.expenses += transfer
                num_ccbs -= 1

            elif num_bfps>0:
                transfer += BFP.min_wage_ratio * min_value
                self.expenses += transfer
                num_bfps -= 1

            ind.receive_transfer(transfer)

    def redistribute_revenue(self, bias):
        R = self.revenue
        N = self.society.size
        b = bias
        def pi(n):
            return (R/N**2) * (2*b*n + N - b*N)

        sorted_inds = sorted(self.society.population,
                             key=lambda ind: ind.get_overall_income())
        
        for pos, ind in enumerate(sorted_inds):
            transfer = (pi(pos)+pi(pos+1))/2.
            ind.receive_transfer(transfer)

    def pay_negative_tax(self, subsidy_rate, exemption_quantile):
        exemption_threshold = quantile(self.society.get_overall_incomes(),
                                       exemption_quantile)

        for ind in self.society.population:
            income = ind.get_overall_income()
            if (income < exemption_threshold):
                benefit = subsidy_rate*(exemption_threshold-income)
                ind.receive_transfer(benefit)
                self.expenses += benefit

    def pay_basic_income(self, fixed_benefit, variable_benefit):
        gdp_pc = sum(self.society.get_overall_incomes())/self.society.size
        benefit = fixed_benefit + variable_benefit*gdp_pc
        for ind in self.society.population:
            ind.receive_transfer(benefit)
            self.expenses += benefit