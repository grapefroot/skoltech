

import numpy as np
import matplotlib.pyplot as plt

from sklearn import datasets
from awc import AWC
from itertools import cycle
from sklearn import metrics
from sklearn.datasets import make_classification

def draw(X, labels, name, save=False):
    n_clusters = len(set(labels))
    colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
    plt.figure(figsize=(10,10))
    for k, col in zip(range(n_clusters), colors):
        class_members = labels == k
        plt.plot(X[class_members, 0], X[class_members, 1], col + 'o')
    
    plt.title(name)
    if(save == True):
        plt.savefig('{}.png'.format(name))
    plt.show()

import time
    
def run_iris(X, y, l, name, plot_lambda=False):
    #iris = datasets.load_iris()
    #X = iris.data
    #y = iris.target
    #X, y = make_classification(1000, 10)

    lambda_interval = np.linspace(0., 1., 11)
    time1 = time.clock()
    AWC_object = AWC(speed=1.)
    # To tune parameter \lambda, plot sum of the weights for \lambda 's from some interval 
    #and take a value at the end of plateau or before huge jump.
    if plot_lambda == True:
        AWC_object.plot_sum_of_weights(lambda_interval, X)
    if l is None:
        l = 0.6
    AWC_object.awc(l, X)
    clusters = AWC_object.get_clusters()
    labels = AWC_object.get_labels()
    time2 = time.clock()
    print(time2 - time1)
    draw(X, labels, name, True)
    
    print('Estimated number of clusters: %d' % len(set(labels)))
    print('cluster sizes: '),
    for c in clusters:
        print(len(c)),
    print("\nV-measure: %0.3f" % metrics.v_measure_score(y, labels))
    

from sklearn import datasets

import timeit

if __name__ == '__main__':

    n_samples = 1002

   # X,y = datasets.make_circles(n_samples=n_samples, factor=.5, noise=.05, random_state=42)
    # X, y = datasets.make_blobs(n_samples=n_samples,
    #                            cluster_std=[1.0, 2.5, 0.5],
    #                            random_state=8)

    X,y = datasets.make_blobs(n_samples=n_samples,
                                 cluster_std=[1.0, 2.5, 0.5],
                                 random_state=8)


    run_iris(X, y, 6)
