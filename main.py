
'''
Main script.
'''

import os
import time
import pandas as pd
from param import Param
from simulation import Simulation

def save_results(results, filename, folder='./res/'):
    os.makedirs(folder, exist_ok=True)
    data = pd.DataFrame.from_dict(results)
    data.index += 1
    data.to_csv(folder+filename+'.csv', 
                index_label=['time'])

N, R, T = 1000, 1000, 100
b = -.25

folder = './RESULTS/main/res/'

param = Param()
param.size = N
param.bias = b
param.negative_tax = False
param.basic_income = False

print('\n-->START.\n')
start = time.time()

print('-'*50)
print('\n\t >Control Simulation:')
control = Simulation(param)

print('\n\t\tRunning...')
results = control.run_many(R,T)

print('\n\t\tSaving results...')
save_results(results,'control',folder)

print('\n1st Partial running time: %.2f seconds.'%(time.time()-start))

print('-'*50)

param.negative_tax = True
param.exemption_quantile = 0.3429
param.subsidy_rate = 0.5
param.basic_income = False

print('\n\t >1st Treatment Simulation:')
treat1 = Simulation(param)

print('\n\t\tRunning...')
results = treat1.run_many(R,T)

print('\n\t\tSaving results...')
save_results(results,'treat1',folder)

print('\n2nd Partial running time: %.2f seconds.'%(time.time()-start))

print('-'*50)

param.basic_income = True
param.fixed_benefit = 0.0
param.variable_benefit = 0.25
param.negative_tax = False

print('\n\t >2nd Treatment Simulation:')
treat2 = Simulation(param)

print('\n\t\tRunning...')
results = treat2.run_many(R,T)

print('\n\t\tSaving results...')
save_results(results,'treat2',folder)

end = time.time()
print('\n\nOverall running time: %.2f seconds.'%(end-start))
print('\n\n-->END.')