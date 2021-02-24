#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


classification active learning with mocu
For discrete case
No sampling in calculation, everything is accurate, enumerate over 
all possible x and theta


"""

import numpy as np
#import matplotlib.pyplot as plt
#from numpy.random import choice
from time import time
#import json
#import copy
#import pickle 
import MethodsTrueData as Methods
import MethodsTrueData_M as Methods_M
#import MethodsFlipError as Methods
#from numpy.random import default_rng, SeedSequence
from Initialization import pz_theta_model, py_eq_z, Initialization, classnum, multiclass
from sklearn.linear_model import LogisticRegression
    
def SingleIteration(k, T, rglist, methodlist, xnum, thetanum):
    print(k)
    
    #Initialize
    np.random.seed(rglist[k])
    xspace, yspace, thetalist = Initialization(xnum, thetanum)
#    errormat  = np.ones([20, T])
    ymatpile = np.zeros([len(xspace), T])
    thetaridx = np.random.randint(len(thetalist))
    dataidx = []
    
    
    #Problem Setting
    if multiclass:
        problem = Methods_M.Problem(xspace, yspace, thetalist, pz_theta_model, py_eq_z, classnum = classnum)
    else:
        problem = Methods.Problem(xspace, yspace, thetalist, pz_theta_model, py_eq_z)
    
    if yspace is None:
        #that is synthetic data
        thetar = thetalist[thetaridx]
        bayesian_error = problem.BayesianError(thetar)
        for t in range(T):
            ymatpile[:, t] = problem.fr(xspace, thetar)
    else: 
        clf = LogisticRegression(max_iter = 200, penalty = 'none').fit(xspace, yspace)
        thetar = np.append(clf.coef_, clf.intercept_)
        thetar = thetar[np.newaxis]
        thetalist = np.concatenate((thetalist, thetar), axis  = 0)
        thetar = np.reshape(thetar, (-1))
        problem = Methods.Problem(xspace, yspace, thetalist, pz_theta_model, py_eq_z, dataidx = dataidx)
#        thetar = thetar[np.newaxis]
        bayesian_error = problem.BayesianError(thetar)
#        bayesian_error = 1 - clf.score(xspace, yspace)
        for t in range(T):
            ymatpile[:, t] = yspace
    
    
    #Active Learning
    for i in methodlist:
#    for i in [0, 1, 2]:
        dataidx = []
        pi_theta = np.ones(len(thetalist))
        pi_theta /= pi_theta.sum()
        problem.Initialize(xspace, yspace, pi_theta, dataidx)
        if i == 0:
            str_label = 'random'
        elif i == 1:
            str_label = 'MES'
        elif i == 2:
            str_label = 'BALD'
        elif i == 3:
            str_label = 'ELR'
        elif i == 4:
            str_label = 'Weighted_MOCU'
        elif i == 5:
            str_label = 'Weighted_MOCU2'
#        elif i == 6:
#            str_label = 'Soft_MOCU10'
#        elif i == 7:
#            str_label = 'Soft_MOCU2'
#        elif i == 8:
#            str_label = 'Soft_MOCU20'
        elif i == 9:
            str_label = 'Soft_MOCU2_20'
        elif i == 10:
            str_label = 'Soft_MOCU2_10'
        elif i == 11:
            str_label = 'Soft_MOCU2_1'
        elif i == 12:
            str_label = 'Soft_MOCU2_2'
        elif i == 13:
            str_label = 'Soft_MOCU2_5'
        elif i == 14:
            str_label = 'Soft_MOCU2_50'
        elif i == 15:
            str_label = 'Soft_MOCU2_100'
        elif i == 16:
            str_label = 'Soft_MOCU2_1000'
        elif i == 17:
            str_label = 'Soft_MOCU2_10000'
        elif i <0:
            str_label = 'Soft_MOCU_'+str(-i)
        error_txt = open(str_label+'error.txt', 'a')
        data_txt = open(str_label+'data.txt', 'a')
        
        for t in range(T):
#            start_time = time()
            if i == 0:
                xidx = np.random.randint(len(problem.xspace))
                xstar = problem.xspace[xidx]
            elif i == 1:
                xstar, _, xidx = problem.Selector(problem.UncertaintyWhole)
            elif i == 2:
                xstar, _, xidx = problem.Selector(problem.EntropyWhole)
            elif i == 3:
                xstar, _, xidx = problem.Selector(problem.MinIbrResidualWhole)
#            elif i == 4:
#                xstar, _, xidx = problem.Selector(problem.Weighted_MOCUWhole)
            elif i == 4:
                xstar, _, xidx = problem.Selector(problem.SoftMOCUWhole(softtype = 4))
            elif i == 5:
                if multiclass:
                    xstar, _, xidx = problem.Selector(problem.SoftMOCUWhole(softtype = 3))
                else:
                    xstar, _, xidx = problem.Selector(problem.Weighted_MOCUWhole2)
            
#            elif i == 6:
#                xstar, _, xidx = problem.Selector(problem.SoftMOCUWhole(k = 10))
#            elif i == 7:
#                xstar, _, xidx = problem.Selector(problem.SoftMOCUWhole(k = 2))
#            elif i == 8:
#                xstar, _, xidx = problem.Selector(problem.SoftMOCUWhole(k = 20))
            elif i == 9:
                xstar, _, xidx = problem.Selector(problem.SoftMOCUWhole(k = 20, softtype = 2))
            elif i == 10:
                xstar, _, xidx = problem.Selector(problem.SoftMOCUWhole(k = 10, softtype = 2))
            elif i == 11:
                xstar, _, xidx = problem.Selector(problem.SoftMOCUWhole(k = 1, softtype = 2))
            elif i == 12:
                xstar, _, xidx = problem.Selector(problem.SoftMOCUWhole(k = 2, softtype = 2))
            elif i == 13:
                xstar, _, xidx = problem.Selector(problem.SoftMOCUWhole(k = 5, softtype = 2))
            elif i == 14:
                xstar, _, xidx = problem.Selector(problem.SoftMOCUWhole(k = 50, softtype = 2))
            elif i == 15:
                xstar, _, xidx = problem.Selector(problem.SoftMOCUWhole(k = 100, softtype = 2))
            elif i == 16:
                xstar, _, xidx = problem.Selector(problem.SoftMOCUWhole(k = 1000, softtype = 2))
            elif i == 17:
                xstar, _, xidx = problem.Selector(problem.SoftMOCUWhole(k = 10000, softtype = 2))
            elif i < 0:
                xstar, _, xidx = problem.Selector(problem.SoftMOCUWhole(k = -i, softtype = 2))
#            print("--- %s is %s seconds ---" % (str_label, time() - start_time))
            if yspace is None:
                ystar = ymatpile[xidx, t]
            else:
                problem.dataidx.append(xidx)
                ystar = problem.yspace[xidx]
            problem.Update(xstar, ystar, xidx)
            
#            errormat[i, t] = problem.ClassifierError(thetar, problem.pi_theta) - bayesian_error
            if yspace is None:
                errortemp = problem.ClassifierError(thetar, problem.pi_theta) - bayesian_error
            else:
#                errortemp = problem.ClassifierError(thetar, problem.pi_theta, xspace) - bayesian_error
                errortemp = problem.ClassifierError(thetar, problem.pi_theta) - bayesian_error
            error_txt.write(str(errortemp)+'\t')
            data_txt.write(str([xstar, ystar])+'\t')
        error_txt.write('\n')
        data_txt.write('\n')
        error_txt.close()
        data_txt.close()
    
    
#%%
# setting:
#  xspace, yspace, thetalist, pz_theta_model, py_eq_z        
        

