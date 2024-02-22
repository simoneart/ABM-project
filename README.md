# Implementation of the SIR epidemic model on networks <br>

## Goal
The goal of the project is to compare the epidemic spreading on different network topologies and to study the dependence of the populations dynamics (i.e. the densities of the S, I and R agents over time) on the choice of parameters. <br> 

## Short introduction
Epidemic models have their origin in the compartimental SIR model developed in the early 20th century. In this simple model the population is divided in three different groups: the Susceptibles (S), who are the agents that can be infected, the Infected (I), who are the agents that can in some way spread the disease and the Removed (R), which are those who either have recovered from the disease and cannot be infected anymore or are deceased. <br> How these agents change their state, i.e. move between compartments, is assumed to be governed by the following set of differential equations:

$$ \frac{dS}{dt} = -\beta SI/N $$  <br> 

$$  \frac{dI}{dt} = \beta SI/N -\gamma I $$  <br> 

$$ \frac{dR}{dt} = \gamma I $$  <br> 

where $N$ is the total number of agents, $\beta$ is the infenction rate times the number of average contact each person has at any given time and $\gamma$ is the healing rate. <br>
Even though this model is able to capture some key features of certain epidemics, it is apparent that its simplicity fails to capture the complexity of a real situation, mainly under two points of view: the first one is related to the actual mechanism of infection and contagion spreading, while the second one is related to structure of social relations and interactions. On one hand, the model can be made more sophisticated by taking into account a greater number of compartments, e.g. introducing a period of incubation, letting a fraction of the removed to become subsceptible again after a transient of time and so on and so forth. On the other hand, it is possible to implement these kinds of dynamics on complex networks, discarding the differential equations approach. In this project I focus on the latter approach. <br>

## Method
I use **Python** to run the simulations and specifically the **igraph** package to create and operate on graphs. Square lattice, Erdos-Renyi, Watts-Strogatz and Barabasi-Albert networks are considered and particular attention is paid to their degree distribution and average shortest path length. They are generated through a series of functions in **nwSIR_functions.py** in such a way that each node correspond to a certain agent (S=0, I=1, R=2) and they are initialized with a given number of initial infected positioned at random in the graph. Given a certain graph realization, keeping fixed the parameters (healing and infenction rate, initial number of infected and total population) for each topology, its epidemic dynamics is repeated a number of times to study the statistics of the spreading. In **main.py** plots containing the populations trend and the degree distribution are produced for different choices of the parameters once a particular topology is chosen. An implementation of the model via differential equations is also present for comparison. <br>

