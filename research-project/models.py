import numpy as np
import sklearn
import xgboost

class GradientBoostingAlgorithm1(object):
    def __init__(self, baselearner, loss, subgrad, n_jobs=1):
        self.base_learner = BaseLearner
        self.models = []
        self.fit = False
        self.weights = []
        self.n_jobs = n_jobs
        self.loss = loss
        self.subgrad = subgrad
        self.n_rounds = 0

        #weight update
        #w_{t+1} = min(w_t, 1/(2L)\xi(F(X_t), y))
        #\sum_{i = 1}^{T}
        #<C(F_T(X), f> -> max 
        #\sum_{i=0}^{sample_size} <subgradC(F_t, y), f> 

    def calc_intermediate(self, X, y_true, n_rounds):
        res = 0
        assert n_rounds < len(self.models)
        for i in range(n_rounds):
            model = self.models[i]
            weight = self.weights[i]
            res += weight * model.predict(X)
        return res
        
    def fit(self, X, y_true, num_steps):
        for 1, i in range(num_steps): 
             
        self.fit = True
        return None

    def predict(self, Xtest):
        pass


class GradientBoostingAlgorithm2(object):
    def __init__(self, baselearner, loss, subgrad, n_jobs=1):
        self.base_learner = BaseLearner
        self.models = []
        self.fit = False
        self.weights = []
        self.n_jobs = n_jobs
        self.loss = loss
        self.subgrad = subgrad

        #weight update
        #w_{t+1} = min(w_t, 1/(2L)\xi(F(X_t), y))
        #\sum_{i = 1}^{T}
        #<C(F_T(X), f> -> max 
        
    def _calc_gradient(self, X, y_true):
        pass

    def calc_intermediate(self, X, y_true, n_rounds):
        self.
        
    def fit(self, X, y_true, num_steps, loss='squared'):
        self.fit = True
        pass

    def predict(self, Xtest):
        pass
