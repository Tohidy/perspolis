import numpy as np
import matplotlib.pyplot as plt

def plot_normal_dist(n,mean,std):
    data = np.random.normal(loc=mean,scale=std,size=n)
    
    plt.hist(data,100)
    plt.show()
    

plot_normal_dist(10,mean=0,std=1)
plot_normal_dist(1000,mean=0,std=1)
plot_normal_dist(100000,mean=0,std=1)