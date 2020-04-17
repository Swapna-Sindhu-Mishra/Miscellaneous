"""
Input: Data file with 2 columns
Output: Pearson correlation coefficient

Last edited on 11 April 2020 by Swapna Sindhu Mishra
"""
folderpath='U:/' #Datafile location?
filename='Correlation_Data.dat' #Datafile name?

import numpy as np
from scipy.stats import pearsonr
import os

os.chdir(folderpath)
data = np.loadtxt(filename)

correlation, _ = pearsonr(data[:,0], data[:,1])
print(f'The correlation is {correlation}')
print(correlation)