import numpy as np
import random as rnd
import matplotlib.pyplot as plt
from nwSIR_functions import *
import igraph as ig
import time
from tabulate import tabulate 
start_time = time.time()

#infection and healing rate
alfa, beta = 0.2, 0.1 

#total population, number of initial infected agents, number of steps of the time evolution
Ntot, Nsteps = 400, 60
NI = int(Ntot/100)

#number of realizations of the evolution
Nreal = 10 

#--------------------------topology of the network--------------------------------
top = 'Barabasi-Albert' #'Lattice', 'Erdos-Renyi', 'Watts-Strogatz', 'Barabasi-Albert'
#---------------------------------------------------------------------------------

print('-----%s case study: parameters-----' %top)

#table with general parameters
table1 = [
    ['%i'%Ntot, '%i'%NI, '%1.3f'%alfa, '%1.3f'%beta]
    ]

head1 = ['# agents', '# initial infected', 'infection rate', 'healing rate']

print(tabulate(table1, headers=head1, tablefmt="grid"))

if top == 'Erdos-Renyi':
    k_values = [5,10,15,50]
    
elif top == 'Watts-Strogatz':
   k_values = [1,2,5,10]

elif top == 'Barabasi-Albert':
    k_values = [1,4,10,20]

elif top == 'Lattice':
    k_values = [0] #dummy
    
c = 0

roS_ave, roI_ave, roR_ave = np.zeros((len(k_values),Nsteps+1)), np.zeros((len(k_values),Nsteps+1)), np.zeros((len(k_values),Nsteps+1))
roS_dev, roI_dev, roR_dev = np.zeros((len(k_values),Nsteps+1)), np.zeros((len(k_values),Nsteps+1)), np.zeros((len(k_values),Nsteps+1))
deg_dist, ave_path_length = np.zeros((len(k_values),Ntot)), np.zeros(len(k_values))

for k in k_values:
    
    if top == 'Erdos-Renyi':
        p = 0.001 
        edges = k*p #probability of forming an edge
        
    elif top == 'Watts-Strogatz':
        p = 0.4 #rewiring probability
        edges = k*int(Ntot/200) #NN on each side
    
    elif top == 'Barabasi-Albert':
        p = 0 #dummy
        edges = k*int(Ntot/200) #number of edges added to each new node
        
    elif top == 'Lattice':
        p = 0 #dummy
        edges = 0 #dummy
    
    stuff = ensemble_stats(top, [NI, edges, p], Ntot, Nreal, Nsteps, alfa, beta)
    roS_ave[c], roI_ave[c], roR_ave[c] = stuff[0][0], stuff[0][1], stuff[0][2]
    roS_dev[c], roI_dev[c], roR_dev[c] = np.sqrt(stuff[1][0]), np.sqrt(stuff[1][1]), np.sqrt(stuff[1][2])
    deg_dist[c], ave_path_length[c] = stuff[2][0], stuff[2][1]
    
    c += 1



days = [n for n in range(Nsteps+1)]

if top == 'Lattice':
    plt.figure(1, (16,9))
    plt.errorbar(days, roS_ave[0], yerr=roS_dev[0], label = r'$\rho_{S}$')
    plt.errorbar(days, roI_ave[0], yerr=roI_dev[0], label = r'$\rho_{I}$')
    plt.errorbar(days, roR_ave[0], yerr=roR_dev[0], label = r'$\rho_{R}$')
    plt.grid()
    plt.title(' -- Average shortest path length: %1.3f --' %ave_path_length[0] )
    plt.xlabel('Days')
    plt.legend()
    plt.suptitle("Dyanmics of the epidemy in a %s network " %top) 
    
    plt.figure(2)
    plt.hist(deg_dist[0], bins='auto', density='True', alpha=0.7, color='blue', edgecolor='black')
    plt.title('Degree Distribution Histogram - %s' % top)
    plt.xlabel('k')
    plt.ylabel(r'$P(k)$')
    plt.grid(True)
    
else:
    plt.figure(1, (16,9))
    plt.subplot(121)
    plt.errorbar(days, roS_ave[0], yerr=roS_dev[0], label = r'$\rho_{S}$')
    plt.errorbar(days, roI_ave[0], yerr=roI_dev[0], label = r'$\rho_{I}$')
    plt.errorbar(days, roR_ave[0], yerr=roR_dev[0], label = r'$\rho_{R}$')
    plt.grid()
    plt.title(' -- Average shortest path length: %1.3f --' %ave_path_length[0] )
    plt.xlabel('Days')
    plt.legend()
    plt.subplot(122)
    plt.errorbar(days, roS_ave[1], yerr=roS_dev[1], label = r'$\rho_{S}$')
    plt.errorbar(days, roI_ave[1], yerr=roI_dev[1], label = r'$\rho_{I}$')
    plt.errorbar(days, roR_ave[1], yerr=roR_dev[1], label = r'$\rho_{R}$')
    plt.grid()
    plt.title(' -- Average shortest path length: %1.3f --' %ave_path_length[1] )
    plt.xlabel('Days')
    plt.legend()
    plt.suptitle("Dyanmics of the epidemy in a %s network" %top) 
    
    plt.figure(2, (16,9))
    plt.subplot(121)
    plt.errorbar(days, roS_ave[2], yerr=roS_dev[2], label = r'$\rho_{S}$')
    plt.errorbar(days, roI_ave[2], yerr=roI_dev[2], label = r'$\rho_{I}$')
    plt.errorbar(days, roR_ave[2], yerr=roR_dev[2], label = r'$\rho_{R}$')
    plt.grid()
    plt.title(' -- Average shortest path length: %1.3f --' %ave_path_length[2] )
    plt.xlabel('Days')
    plt.legend()
    plt.subplot(122)
    plt.errorbar(days, roS_ave[3], yerr=roS_dev[3], label = r'$\rho_{S}$')
    plt.errorbar(days, roI_ave[3], yerr=roI_dev[3], label = r'$\rho_{I}$')
    plt.errorbar(days, roR_ave[3], yerr=roR_dev[3], label = r'$\rho_{R}$')
    plt.grid()
    plt.title(' -- Average shortest path length: %1.3f --' %ave_path_length[3] )
    plt.xlabel('Days')
    plt.legend()
    plt.suptitle("Dyanmics of the epidemy in a %s network" %top) 
    
    fig, axs = plt.subplots(2, 2)
    fig.suptitle('Degree distributions of the graphs - %s networks' %top)
    axs[0, 0].hist(deg_dist[0], bins='auto', density='True', alpha=0.7, color='blue', edgecolor='black')
    axs[0, 0].set_title('Graph 1')
    axs[0, 1].hist(deg_dist[1], bins='auto', density='True', alpha=0.7, color='blue', edgecolor='black')
    axs[0, 1].set_title('Graph 2')
    axs[1, 0].hist(deg_dist[2], bins='auto', density='True', alpha=0.7, color='blue', edgecolor='black')
    axs[1, 0].set_title('Graph 3')
    axs[1, 1].hist(deg_dist[3], bins='auto', density='True', alpha=0.7, color='blue', edgecolor='black')
    axs[1, 1].set_title('Graph 4')
    
    for ax in axs.flat:
        ax.set(xlabel=r'$k$', ylabel=r'$P(k)$')

#SIR model simulated using the standard set of partial differential equation
#the b parameter is the infection rate times the average number of contacts each agent has at a given time.

NN = 4 #lattice
b = alfa * NN

pde_sol = SIR_PDE(Ntot, NI, b, beta, dt = 0.1, Num_steps = 600)
s = pde_sol[0]/Ntot
i = pde_sol[1]/Ntot
r = pde_sol[2]/Ntot
xaxis = pde_sol[3]

plt.figure(3, (16,9))
plt.plot(xaxis, s, label = r'$\rho_{S}$')
plt.plot(xaxis, i, label = r'$\rho_{I}$')
plt.plot(xaxis, r, label = r'$\rho_{R}$')
plt.grid()
plt.suptitle('SIR model -- PDE approach')
plt.title('Number of average contacts: %i' %NN)
plt.xlabel('Time')
plt.legend()
    
    # Hide x labels and tick labels for top plots and y ticks for right plots.
    for ax in axs.flat:
        ax.label_outer()

print("--- %s seconds ---" % (time.time() - start_time))
