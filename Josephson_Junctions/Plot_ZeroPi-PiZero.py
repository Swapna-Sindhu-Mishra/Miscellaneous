import math
import numpy as np
import matplotlib.pyplot as plt
import os

def ZeroPi(x):
    return math.exp(-x/10)*math.cos(x)

def PiZero(x):
    return math.exp(-x/10)*math.sin(x)

x= np.linspace(0,20,1000)
ZP = np.vectorize(ZeroPi)
PZ = np.vectorize(PiZero)


plt.plot(x, ZP(x),  color='b', label='Singlet wavefunction', )
plt.plot(x, PZ(x),  color='r', label='Triplet wavefunction')
plt.hlines(y=0, xmin=0, xmax=20, linewidth=1, linestyles='--', color='gray')
plt. margins(x=0)
plt.title(f'0-$\pi$ Oscillations in Ferromagnets', fontsize=15)
plt.ylabel('Pair correlation function, $\Psi$', fontsize=15)
plt.xlabel('Ferromagnet thickness, d', fontsize=15)
plt.legend(loc='best', fontsize=12)
plt.xticks([], [])
plt.yticks([], [])
plt.savefig(f'0-Pi.pdf')
plt.savefig(f'0-Pi.svg')
plt.show()
