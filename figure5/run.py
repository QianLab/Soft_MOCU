#%%
import numpy as np
import multiprocessing

from joblib import Parallel, delayed
import sys
import ProblemSetting as PS

#with open('RandomGenerator.txt', 'r') as f:
#    datalist = json.load(f)

#from tqdm import tqdm
num_cores = 1
runnum = 100
T = 100
methodlist = [0, 1, 2, 3, -10, -100, -1000]
xnum = 100
thetanum = 100


inputs = list(range(runnum))
sq = np.random.SeedSequence(5905687423)
rglist = sq.generate_state(runnum)
if __name__ == "__main__":
    processed_list = Parallel(n_jobs=num_cores)(delayed(PS.SingleIteration)(k, T, rglist, methodlist, xnum, thetanum) for k in inputs)
    
    
#if i == 0:
#    str_label = 'random'
#elif i == 1:
#    str_label = 'MES'
#elif i == 2:
#    str_label = 'BALD'
#elif i == 3:
#    str_label = 'MOCU'
#elif i == 4:
#    str_label = 'Weighted_MOCU'
#elif i == 5:
#    str_label = 'Weighted_MOCU2'
#elif i == 6:
#    str_label = 'Soft_MOCU10'
#elif i == 7:
#    str_label = 'Soft_MOCU2'
#elif i == 8:
#    str_label = 'Soft_MOCU20'
#elif i == 9:
#    str_label = 'Soft_MOCU2_20'
#elif i == 10:
#    str_label = 'Soft_MOCU2_10'
#%%









#thetar = [0.12, 0.003]
#xstar = [0, 0.06]
#ystar = fr(xspace, thetar)
#pyx = PzGivenXTheta(xspace, thetar)