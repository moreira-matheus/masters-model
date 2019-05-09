'''
class Individual
'''

from numpy import exp
from numpy.random import uniform

RHO_S = 0.107
BETA_0, BETA_1 = 0.081, -0.0012

class Individual:
    '''
    Represents the agent.
    '''
    def __init__(self):
        self.endowment = 0.0
        self.income = {'wages': 0.0, 'transfers':0.0}
        self.current_age = 0
        self.age_at_death = 0
        self.schooling = 0

    def grow_older(self):
        self.current_age += 1

    def is_alive(self):
        return self.current_age < self.age_at_death

    def get_overall_income(self):
        return sum(self.income.values())

    def reset_income(self):
        self.income['wages'] = 0.0
        self.income['transfers'] = 0.0

    def update_wage(self, schooling_age):
        self.reset_income()

        is_working = self.current_age > (self.schooling+schooling_age)

        x = is_working * (self.current_age-(self.schooling+schooling_age))
        s = is_working*self.schooling+\
            (not is_working)*max([self.current_age-schooling_age])

        self.income['wages'] = self.endowment*\
            ((not is_working)+is_working*exp(RHO_S*s+BETA_0*x+BETA_1*x**2))
        
    def receive_transfer(self, transfer):
        self.income['transfers'] += transfer

    def pay_taxes(self, due_rate, avg_rate):
        a, b = sorted([due_rate, 2*avg_rate-due_rate])
        real_rate = max([0.0, uniform(a,b)])
        taxes = real_rate * self.get_overall_income()
        self.income['wages'] -= taxes
        return taxes

    def __str__(self):
        st = '\nIndividual:'
        st+= '\n\t Endowment: ' + str(self.endowment)
        st+= '\n\t Current income: ' + str(self.income)
        st+= '\n\t Current age: ' + str(self.current_age)
        st+= '\n\t Age at death: ' + str(self.age_at_death)
        st+= '\n\t Schooling: ' + str(self.schooling) + '\n'
        return st

if __name__=='__main__':
    ind = Individual()
    ind.endowment = 100.0
    ind.schooling = 10
    ind.current_age = 25
    ind.update_wage(6)
    print(ind)