import numpy as np
import scipy as sp
from scipy.optimize import linear_sum_assignment


def generate_task(n):
    return np.array(
            [np.random.choice(range(n), size = n, replace=False) for i in range(n)])

def generate_random_assignment(matrix):
    n = matrix.shape[0]
    return np.arange(0, n, 1), np.random.choice(range(n), size = n, replace=False)

def reduction(matrix):
    newarr = np.zeros_like(matrix)
    for i in range(len(newarr)):
        for j in range(len(newarr)):
            newarr[i, matrix[i, j]] = j
    return newarr

def calculate_min(mat_size):
    task_mat = generate_task(mat_size)
    a,b = generate_random_assignment(task_mat)
    c,d = linear_sum_assignment(task_mat)
    
    random = task_mat[a,b].sum()
    optimized = task_mat[c,d].sum()
    return random, optimized

def perform_experiment():
    mat_size = 30
    num_experiments = 1000
    random_result = 0
    random_results = []
    optimized_result = 0
    optimized_results = []
    for i in range(num_experiments):
        random, optimized = calculate_min(30) 
        random_result += random
        random_results.append(random)
        optimized_result += optimized
        optimized_results.append(optimized)
    print("The number of experiments is {}, matrix size is {}".format(num_experiments, mat_size))
    random_result/=num_experiments
    optimized_result/=num_experiments
    print("The mean error value for random assignment is {}".format(random_result))
    print("The mean error value for optimized assignement is {}".format(optimized_result))
    return random_results, optimized_results

if __name__ == "__main__":
    perform_experiment()
