# Implementation of the SIR epidemic model on networks <br>

## Goal
The goal of the project is to compare epidemic spreading on different network topologies and to study the dependence of the populations dynamics (i.e. the densities of the S, I and R agents over time) on the choice of parameters. <br> 

## Short introduction

### Epidemic models
Epidemic models have their origin in the compartimental SIR model developed in the early 20th century. In this simple model the population is divided in three different groups: the Susceptibles (S), who are the agents that can be infected, the Infected (I), who are the agents that can in some way spread the disease and the Removed (R), which are those who either have recovered from the disease and cannot be infected anymore or are deceased. <br> How these agents change their state, i.e. move between compartments, is assumed to be governed by the following set of differential equations:

$$ \frac{dS}{dt} = -\beta SI/N $$  <br> 

$$  \frac{dI}{dt} = \beta SI/N -\gamma I $$  <br> 

$$ \frac{dR}{dt} = \gamma I $$  <br> 

where $N$ is the total number of agents, $\beta$ is the infenction rate times the number of average contacts per unit time and $\gamma$ is the healing rate. The key assumption here is that the population mixes at random, which means that the probability of each individual of coming into contact with any other agent is uniform.  <br>
Even though this model is able to capture some key features of certain epidemics, it is apparent that its simplicity fails to capture the complexity of a real situation, mainly under two points of view: the first one is related to the actual mechanism of infection and contagion spreading, while the second one is related to the structure of social relations and interactions, which are overlooked by the random mixing hypothesis. On one hand, the model can be made more sophisticated by taking into account a greater number of compartments, e.g. introducing a period of incubation, letting a fraction of the removed to become subsceptible again after a transient of time and so on and so forth. On the other hand, it is possible to implement these kinds of dynamics on complex networks, discarding the differential equations approach. In this project I focus on the latter strategy. <br>

### Network classes and their properties
In this section I just want to give a quick overview of the topologies I am going to study with some few key features. <br>

-**Square lattice**: The simplest kind of regular, deterministic graph. In 2-dimensions each node has exactly 4 neighbors.

-**Erdos-Renyi**: A very simple regular random network, where the edges between the N nodes have the same probability of existing. The average degree $&lt k &gt$ represents well the number of neighbors of the nodes.

-**Watts-Strogatz**: An initial network organized in a ring where each node has a certain number of links to the closest nodes, is rewired clockwise with probability $p$ to another node chosen at random. In these kind of graphs the average degree $&lt k &gt$ represents well the number of neighbors of the nodes, but the rewiring process greatly reduces the shortest path length $&lt l &gt$, giving rise to a network with small world property (average shortest path length increase slower than any postivi power of the size of the graph, whereas for a $d-dimensional$ lattice $&lt l &gt \propto N^{\frac{1}{d}}$ ).

-**Barabasi-Albert**: Starting from a simple network (depends on the algorithm), new vertices are added, connecting them to a certain number of pre-existing vertices that are chosen with a probability proportional to their degree at that time. These kind of graphs show a power law degree distribution $P(k) \propto k^{-\gamma}$ with $\gamma = 3$ and the small world property.

## Method
I use **Python** to run the simulations and specifically the **igraph** package to create and operate on graphs. Square lattice, Erdos-Renyi, Watts-Strogatz and Barabasi-Albert networks are considered and particular attention is paid to their degree distribution and average shortest path length. They are generated through a series of functions in [nwSIR_functions.py](https://github.com/simoneart/ABM-project/blob/main/nwSIR_functions.py) in such a way that each node correspond to a certain agent (S=0, I=1, R=2) and they are initialized with a given number of initial infected positioned at random in the graph. Then, the dynamics is implemented firstly updating the infected according to the healing rate, then checking whether in the neighborhood of each S node (chosen in a differente order at each time step) there are infected agents and thus infecting the said node with probability given by the infection rate and the number of neighboring I nodes. Given a certain graph realization, keeping fixed the parameters (healing and infenction rate, initial number of infected and total population) for each topology, its epidemic dynamics is repeated a number of times to study the statistics of the spreading. In [main.py](https://github.com/simoneart/ABM-project/blob/main/main.py) plots containing the populations trends and the degree distributions are produced for different choices of the parameters once a particular topology is chosen. An implementation of the model via differential equations in the random-mixing hypothesis is also present for comparison. <br>

## Results 

The analysis has been carried fixing the following parameters for all topologies:

- $\alpha = 0.2$ infection rate;
- $\beta = 0.1$ healing rate; 
- $N=400$ total population;
- $I(0) = 4$ initial infectuos agents;
- $Days = 60$ number of time steps in the evolution;
- $n = 10$ number of realizations of the dynamics.

These choices of parameters will allow us to appreciate, despite the relatively small values of the infection rate and of the initial number of I, the crucial role played by the properties of the graph, in particulare the average shortest path length. <br>

In the following the relevant plots are reported.

### 2D Square Lattice Network

![pops_L](https://github.com/simoneart/ABM-project/assets/95907355/8f509bf3-0af2-47e6-92ad-4821cc5f0f04)

![dd_L](https://github.com/simoneart/ABM-project/assets/95907355/522cd203-a9e8-4593-a681-830c79efb034)


