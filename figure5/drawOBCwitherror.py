
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import pickle 
from numpy.random import choice
import copy
#%%
#%%
#import pylab
# this one is used to generate comparison figure
runnum = 500
T = 300
compare = T
new_colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
              '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
              '#bcbd22', '#17becf']
# store real error
#errormat = np.ones([runnum, T])
errormat1 = np.ones([runnum, T])
errormat2 = np.ones([runnum, T])
errormat3 = np.ones([runnum, T])
errormat4 = np.ones([runnum, T])
errormat5 = np.ones([runnum, T])
errormat6 = np.ones([runnum, T])
errormat7 = np.ones([runnum, T])
errormat8 = np.ones([runnum, T])
errormat = np.ones([runnum, T])
x1 = list(range(1, T+1))
fig2, ax2 = plt.subplots()
for i in [0,1,  2, 3, 5, 7, 9,  12]:
#for i in [9,   12]:
    if i == 0:
        errormat = errormat1
        str_label = 'random'
        color = 'b'
    elif i == 1:
        errormat = errormat2
        str_label = 'MES'
        color = 'y'
    elif i == 2:
        errormat = errormat3
        str_label = 'BALD'
        color = 'g'
    elif i == 3:
        errormat = errormat4
        str_label = 'ELR'
        color = 'r'
#    elif i == 4:
#        errormat = errormat5
#        str_label = 'Weighted_MOCU'
#        color = 'm'
    elif i == 4:
        errormat = errormat6
        str_label = 'Weighted_MOCU2'
#    elif i == 5:
#        errormat = errormat7
#        str_label = 'Soft_MOCU2_10'
    
    elif i == 5:
        str_label = 'Soft_MOCU2_1'
    elif i == 6:
        str_label = 'Soft_MOCU2_2'
    elif i == 7:
        str_label = 'Soft_MOCU2_5'
    elif i == 9:
        errormat = errormat7
        str_label = 'Soft_MOCU2_20'
    elif i == 8:
        str_label = 'Soft_MOCU2_10'
    elif i == 10:
        str_label = 'Soft_MOCU2_50'
    elif i == 11:
        str_label = 'Soft_MOCU2_100'
    elif i == 12:
        str_label = 'Soft_MOCU2_1000'
    f = open(str_label+'error.txt', 'r')
    a = f.readlines()
    b = [x.split() for x in a]
    floatmat = [[float(y) for y in x] for x in b]
    npmat = np.array(floatmat)
    errormat[:] = npmat[0:runnum]
    f.close()
#    if i == 1:
#        str_label = 'MES'
#    ax2.plot(x1[0:compare], np.mean(errormat[:, 0:compare], axis = 0) , label = str_label, color = new_colors[i])
    stdlist = np.std(errormat[:, 0:compare], axis = 0)
#    print(stdlist)
    ax2.errorbar(x1[0:compare], np.mean(errormat[:, 0:compare], axis = 0),yerr = stdlist[ 0:compare]/np.sqrt(runnum), 
                 errorevery = 9 , label = str_label)
ax2.set_yscale('log')
ax2.set_xlabel('Iteration number')
ax2.set_ylabel('error regret')
#ax2.set_yticks([0.001, 0.005])
#ax2.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
#ax2.set_xticks(list(range(2, 21, 2)))
#ax2.set_yticks([0.001], ['10'])
ax2.legend()

#%%
#letterEF
#import pylab
# this one is used to generate comparison figure
runnum = 1
T = 300
compare = T
new_colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
              '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
              '#bcbd22', '#17becf']
# store real error
#errormat = np.ones([runnum, T])
errormat1 = np.ones([runnum, T])
errormat2 = np.ones([runnum, T])
errormat3 = np.ones([runnum, T])
errormat4 = np.ones([runnum, T])
errormat5 = np.ones([runnum, T])
errormat6 = np.ones([runnum, T])
errormat7 = np.ones([runnum, T])
x1 = list(range(1, T+1))
fig2, ax2 = plt.subplots()
for i in [0, 1, 2, 3, 4]:
    if i == 0:
        errormat = errormat1
        str_label = 'random'
        color = 'b'
        label = str_label
    elif i == 1:
        errormat = errormat2
        str_label = 'US'
        color = 'y'
        label = 'MES'
    elif i == 2:
        errormat = errormat3
        str_label = 'Entropy'
        color = 'g'
        label = 'BALD'
    elif i == 3:
        errormat = errormat4
        str_label = 'MOCU'
        color = 'r'
        label = 'ELR'
    elif i == 4:
        errormat = errormat5
        str_label = 'MOCU_modify'
        color = 'm'
        label = 'Weighted_MOCU'
    elif i == 5:
        errormat = errormat6
        str_label = 'MOCU_modify2'
    elif i == 6:
        errormat = errormat7
        str_label = 'MOCU_modify3'
    f = open(str_label+'error.txt', 'r')
    a = f.readlines()
    b = [x.split() for x in a]
    floatmat = [[float(y) for y in x] for x in b]
    npmat = np.array(floatmat)
    errormat[:] = npmat[0:runnum]
    f.close()
    ax2.plot(x1[0:compare], np.mean(errormat[:, 0:compare], axis = 0) , label = label, color = new_colors[i])
ax2.set_yscale('log')
ax2.set_xlabel('Iteration number')
ax2.set_ylabel('error rate')
#ax2.set_xticks(list(range(2, 17, 2)))
#ax2.set_yticks([0.02, 0.1])
ax2.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax2.legend()

#%%
#import pylab
# this one is used to generate comparison figure
runnum = 5
T = 80
# store real error
errormat1 = np.ones([runnum, T])
errormat2 = np.ones([runnum, T])
errormat3 = np.ones([runnum, T])
errormat4 = np.ones([runnum, T])
errormat5 = np.ones([runnum, T])
x1 = list(range(T))
fig2, ax2 = plt.subplots()
for i in [0,1, 2, 3, 4]:
    if i == 0:
        errormat = errormat1
        str_label = 'random'
    elif i == 1:
        errormat = errormat2
        str_label = 'MES'
    
    elif i == 2:
        errormat = errormat3
        str_label = 'BALD'
    elif i == 3:
        errormat = errormat4
        str_label = 'ELR'
    elif i == 4:
        errormat = errormat5
        str_label = 'Weighted_MOCU'
    for k in range(runnum):
        f = open(str_label+str(k)+'error.txt', 'r')
        a = f.readlines()
        b = [x.split() for x in a]
        floatmat = [[float(y.replace('[', '').replace(']', '')) for y in x] for x in b] #because I store list in text
        npmat = np.array(floatmat)
        errormat[k, :] = npmat[0:runnum]
        f.close()
    ax2.plot(x1, np.mean(errormat, axis = 0), label = str_label)
    np.savetxt(str_label+'error.txt', errormat, fmt = '%10.5f')
ax2.set_yscale('log')
ax2.set_xlabel('Iteration number')
ax2.set_ylabel('error rate')
ax2.set_xticks([1, 10, 20])
ax2.legend()
#%%
fig2.savefig('simulatederror2.pdf')
