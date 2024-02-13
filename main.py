import numpy as np
import matplotlib.pyplot as plt
from functions import *
import igraph as ig
from tabulate import tabulate 

#infection and healing rate
alfa, beta = 0.8, 0.1 

#total population, number of initial infected agents, number of steps of the time evolution
Ntot, Nsteps = 400, 40
NI = int(Ntot/5)

#number of realizations of the evolution
Nreal = 10 

#topology of the network
top = 'Barabasi-Albert'

edges = int(Ntot/5)

stuff = ensemble_stats(top, [NI, edges], Ntot, Nreal, Nsteps, alfa, beta)
roS_ave, roI_ave, roR_ave = stuff[0][0], stuff[0][1], stuff[0][2]
roS_dev, roI_dev, roR_dev = np.sqrt(stuff[1][0]), np.sqrt(stuff[1][1]), np.sqrt(stuff[1][2])
deg_dist, ave_path_length = stuff[2][0], stuff[2][1]

days = [n for n in range(Nsteps+1)]

plt.figure(1, (16,9))
plt.errorbar(days, roS_ave, yerr=roS_dev, label = r'$\rho_{S}$')
plt.errorbar(days, roI_ave, yerr=roI_dev, label = r'$\rho_{I}$')
plt.errorbar(days, roR_ave, yerr=roR_dev, label = r'$\rho_{R}$')
plt.grid()
plt.title('Barabasi-Albert')
plt.xlabel('Days')
plt.legend()


plt.figure(2)
plt.hist(deg_dist, bins='auto', density='True', alpha=0.7, color='blue', edgecolor='black')
plt.title('Degree Distribution Histogram - %s' % top)
plt.xlabel('k')
plt.ylabel(r'$P(k)$')
plt.grid(True)

print('-----%s case study: parameters-----' %top)

#table with general parameters
table1 = [
    ['%i'%Ntot, '%i'%NI, '%1.3f'%alfa, '%1.3f'%beta]
    ]

head1 = ['# agents', '# initial infected', 'infection rate', 'healing rate']

print(tabulate(table1, headers=head1, tablefmt="grid"))

#graph specific table
table2 = [
    ['%i'%edges, '%1.3f' % ave_path_length]
    ]

head2 = ['# added edges', 'average path length']

print(tabulate(table2, headers=head2, tablefmt="grid"))
