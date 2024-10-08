"""
Input: Data file with 2 columns
Output: Pearson correlation coefficient
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
