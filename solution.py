import pandas as pd
import numpy as np


chat_id = 396928060 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    mu = np.log(x).mean() 
    sigma = np.log(x).std() 
    a = np.exp(mu + sigma**2/2) 

    sample_sizes = [10, 100, 1000]
    mse_thresholds = [0.259, 0.0547, 0.0194, 0.194] 
    mses = []
    for size in sample_sizes:
        sample = np.random.choice(x, size=size, replace=True)
        a_estimate = np.exp(np.log(sample).mean() + np.log(sample).std()**2/2)
        mse = ((a_estimate - a)**2)/size
        mses.append(mse)
        
    score = 0
    if mses[2] < mse_thresholds[3]:
        score += 1
    if mses[1] < mse_thresholds[2]:
        score += 1
    if mses[0] < mse_thresholds[1]:
        score += 1
    if mses[2] < mse_thresholds[0]:
        score += 1
    
    return a
