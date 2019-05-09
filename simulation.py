
'''
class Simulation
'''

import calculations as calc
from numpy import array, zeros
from model.society import Society
from model.government import Government
from model.dists.income_dist import IncomeDist

class Simulation:
    def __init__(self, param):
        self.param = param
        self.society = None
        self.government = None

    def reset(self):
        #IncomeDist.reset_param()
        self.society = Society()
        self.society.populate(self.param.size)
        self.government = Government()
        self.government.society = self.society

    def run_many(self, runs, times):
        res = {}
        alphas, xs_min, errors = zeros(times), zeros(times), zeros(times)
        ginis, means = zeros(times), zeros(times)
        gdps, pops = zeros(times), zeros(times)
        revs, exps = zeros(times), zeros(times)
        btms, tops = zeros(times), zeros(times)

        for r in range(runs):
            if r%20 == 0:
                print('Run: ',r+1)
            results = self.run_once(times)

            alphas += array(results['alpha'])
            xs_min += array(results['x_min'])
            errors += array(results['error'])
            ginis += array(results['gini'])
            means += array(results['mean'])
            pops += array(results['pop'])
            gdps += array(results['gdp'])
            revs += array(results['rev'])
            exps += array(results['exp'])
            btms += array(results['btm'])
            tops += array(results['top'])

        res['alpha'] = alphas/runs
        res['x_min'] = xs_min/runs
        res['error'] = errors/runs
        res['gini'] = ginis/runs
        res['mean'] = means/runs
        res['pop'] = pops/runs
        res['gdp'] = gdps/runs
        res['rev'] = revs/runs
        res['exp'] = exps/runs
        res['btm'] = btms/runs
        res['top'] = tops/runs

        return res

    def run_once(self, times):
        res = {}
        alphas, xs_min, errors = [], [], []
        ginis, means = [], []
        pops, gdps, revs, exps = [], [], [], []
        btms, tops = [], []

        self.reset()

        for t in range(times):
            self.society.update_all_wages()
            self.government.reset_accounts()
            
            self.government.collect_taxes()

            self.government.redistribute_revenue(self.param.bias)
            self.government.pay_benefits()
            
            if(self.param.negative_tax):
                self.government.pay_negative_tax(self.param.subsidy_rate,
                                                 self.param.exemption_quantile)
            if(self.param.basic_income):
                self.government.pay_basic_income(self.param.fixed_benefit,
                                                 self.param.variable_benefit)

            all_incomes = self.society.get_overall_incomes()

            a,x,e = IncomeDist.estimate_param(all_incomes)
            alphas.append(a)
            xs_min.append(x)
            errors.append(e)

            ginis.append(calc.gini(all_incomes))
            gdps.append(sum(all_incomes))
            means.append(gdps[-1]/self.society.size)
            revs.append(self.government.revenue)
            exps.append(self.government.expenses)
            pops.append(self.society.size)

            bottom, top = calc.bottom_top(all_incomes)
            btms.append(bottom)
            tops.append(top)
            
            self.society.update_population()

        res['alpha'] = alphas
        res['x_min'] = xs_min
        res['error'] = errors
        res['gini'] = ginis
        res['mean'] = means
        res['pop'] = pops
        res['gdp'] = gdps
        res['rev'] = revs
        res['exp'] = exps
        res['btm'] = btms
        res['top'] = tops

        return res
