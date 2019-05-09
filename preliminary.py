
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

print('\n--> START.\n')
start = time.time()

N, R, T = 1000, 1000, 100
biases = [-1.0, -0.75, -0.5, -0.25, 0.0, 0.25, 0.5, 0.75, 1.0]

folder = './RESULTS/preliminary/res/'
filename = 'prelim'

param = Param()
param.size = N
param.basic_income = False
param.negative_tax = False

for pos,bias in enumerate(biases):
    print('\nBias = ',bias)
    param.bias = bias
    print('\n\tRunning...')
    sim = Simulation(param)
    res = sim.run_many(R,T)
    print('\n\tSaving results...')
    save_results(res,filename+str(pos),folder)

end = time.time()
print('\nTotal running time: %.2f seconds.'%(end-start))

print('\n\n--> END.')