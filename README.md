# Implementation of the SIR epidemic model on networks <br>

## Goal
The goal of the project is to compare epidemic spreading on different network topologies and to study the dependence of the populations dynamics (i.e. the densities of the S, I and R agents over time) on the choice of parameters. <br> 

## Short introduction

### Epidemic models
Epidemic models have their origin in the compartimental SIR model developed in the early 20th century. In this simple model the population is divided in three different groups: the Susceptibles (S), who are the agents that can be infected, the Infected (I), who are the agents that can in some way spread the disease and the Removed (R), which are those who either have recovered from the disease and became immune or are deceased. <br> How these agents change their state, i.e. move between compartments, is assumed to be governed by the following set of differential equations:

$$ \frac{dS}{dt} = -\beta SI/N $$  <br> 

$$  \frac{dI}{dt} = \beta SI/N -\gamma I $$  <br> 

$$ \frac{dR}{dt} = \gamma I $$  <br> 

where $N$ is the total number of agents, $\beta$ is the infenction rate times the number of average contacts per unit time and $\gamma$ is the healing rate. The key assumption here is that the population mixes at random, which means that the probability of each individual of coming into contact with any other agent is uniform.  <br>
Even though this model is able to capture some key features of certain epidemics, it is apparent that its simplicity fails to capture the complexity of a real situation, mainly under two points of view: the first one is related to the actual mechanism of infection and contagion spreading, while the second one is related to the structure of social relations and interactions, which are overlooked by the random mixing hypothesis. On one hand, the model can be made more sophisticated by taking into account a greater number of compartments, e.g. introducing a period of incubation, letting a fraction of the removed to become subsceptible again after a transient of time and so on and so forth. On the other hand, it is possible to implement these kinds of dynamics on complex networks, discarding the differential equations approach. In this project I focus on the latter strategy. <br>

### Network classes and their properties
In this section I want to give a quick overview of the topologies I am going to study with some few key features. <br>

-**Square lattice**: The simplest kind of regular, deterministic graph. In 2-dimensions each node has exactly 4 neighbors.

-**Erdos-Renyi**: A simple regular random network, where the edges between the N nodes have the same probability of existing. The average degree $&lt k &gt$ represents well the number of neighbors of the nodes.

-**Watts-Strogatz**: An initial network organized in a ring where each node has a certain number of links to the closest nodes, is rewired clockwise with probability $p$ to another node chosen at random. In these kind of graphs the average degree $&lt k &gt$ represents well the number of neighbors of the nodes, but the rewiring process greatly reduces the shortest path length $&lt l &gt$, giving rise to a network with small world property (average shortest path length increase slower than any postive power of the size of the graph, whereas for a $d-dimensional$ lattice $&lt l &gt \propto N^{\frac{1}{d}}$ ).

-**Barabasi-Albert**: Starting from a simple network (depends on the algorithm), new vertices are added, connecting them to a certain number of pre-existing vertices that are chosen with a probability proportional to their degree at that time. These kind of graphs show a power law degree distribution $P(k) \propto k^{-\gamma}$ with $\gamma = 3$ and the small world property.

## Method
I use **Python** to run the simulations and specifically the **igraph** package to create and operate on graphs. Square lattice, Erdos-Renyi, Watts-Strogatz and Barabasi-Albert networks are considered, as said earlier, and particular attention is paid to their degree distribution and average shortest path length. They are generated through a series of functions in [nwSIR_functions.py](https://github.com/simoneart/ABM-project/blob/main/nwSIR_functions.py) in such a way that each node correspond to a certain agent (S=0, I=1, R=2) and they are initialized with a given number of initial infected positioned at random in the graph. Then, the dynamics is implemented firstly updating the infected according to the healing rate ($I \rightarrow R$ transition), then checking whether in the neighborhood of each S node (chosen in a differente order at each time step) there are infected agents and thus infecting the said node with probability given by the infection rate and the number of neighboring I nodes ($S \rightarrow I$ transition). Given a certain graph realization, keeping fixed the parameters (healing and infenction rate, initial number of infected and total population) for each topology, its epidemic dynamics is repeated a number of times to study the statistics of the spreading. In [main.py](https://github.com/simoneart/ABM-project/blob/main/main.py) plots containing the populations trends and the degree distributions are produced for different choices of the parameters once a particular topology is chosen. An implementation of the model via differential equations in the random-mixing hypothesis is also present for comparison. <br>

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

### Random Mixing
Solution of the SIR differential equations, choosing $m = 4$ number of average contancts per unit time.

![SIR_pde](https://github.com/simoneart/ABM-project/assets/95907355/8312eabc-24fe-4305-ae76-970eb44dadda)


### 2D Square Lattice Network

![pops_L](https://github.com/simoneart/ABM-project/assets/95907355/7ed213e3-abb2-4a29-a5a9-08cc1cbf383e)

![dd_L](https://github.com/simoneart/ABM-project/assets/95907355/137afb9a-4c16-4c86-97da-e013bd2951b6)

### Erdos-Renyi Network


The following plots are obtained varying the probability of forming an edge in the process of building the graph ($p = 0.001 k$, $k = 5, 10, 15, 50$).

![pops_ER_1](https://github.com/simoneart/ABM-project/assets/95907355/e233ab49-8059-4a91-b289-2702ea1a4db1)

![pops_ER_2](https://github.com/simoneart/ABM-project/assets/95907355/080c85d0-e7a5-414a-98a1-cff352af8c33)

![dd_ER](https://github.com/simoneart/ABM-project/assets/95907355/4a94d4bf-b0a9-4d87-a47a-c21bf0cf3341)

### Watts-Strogatz Network


With fixed rewiring probability ($p=0.4$), I varied the number of initial edges: $NN = 2k$, $k=1,2,5,10$.

![pops_WS_1](https://github.com/simoneart/ABM-project/assets/95907355/bc871c20-02a3-40d9-947f-b06c059b9482)

![pops_WS_2](https://github.com/simoneart/ABM-project/assets/95907355/d37bf1c5-7c0a-4497-a95a-bd4b20068576)

![dd_WS](https://github.com/simoneart/ABM-project/assets/95907355/7554980a-77cd-4bb3-85b2-8eb24b8a5c17)

### Barabasi-Albert Network

The plots are obtained varying th number of edges added to each new node ($New Edges = 2k$, $k=1,4,10,20$).

![pops_BA_1](https://github.com/simoneart/ABM-project/assets/95907355/9207b35c-b509-4ee6-91da-6f17476f2dce)

![pops_BA_2](https://github.com/simoneart/ABM-project/assets/95907355/4da73f71-cf73-40d6-aff6-5c8903587c36)

![dd_BA](https://github.com/simoneart/ABM-project/assets/95907355/dddbc3d1-5d11-4cbb-aa64-6377ab91942f)

### Comments

First of all, it is interesting to notice the difference between the model on the lattice and the model solved with the differential equations. Even though in both cases, with my choice of parameters, each agent is assumed to be in contact with four other agents, the absence of mixing in the lattice give rise to a very different dynamics with respect to the one given by the DEs. In particular, as one could expect, the epidemy spreads much slower in the former case, since an S agent that starts very far from any I agent will find an infectuous neighbor only after a time proportional to the distance between the two, whereas in the random mixing case each agent at each step has a fixed probability of getting into contact. This highlights well the limitations of both approaches: the set of differential equations looses all the details of the actual spreading of the disease, while the SIR on a lattice is too simple a model to capture the complexity of real social networks. <br>
Scaling up the complexity by considering other topologies, one thing that can be readily noticed about the other plots is how the parameters change the epidemic spreading. As suggested by the above discussion and confirmed by the plots, the average shortest path length seems to be a good property of the network to look at to understand how fast the peak of infections is reached and the maximum value of infected agents. As $&lt l &gt$ gets shorter, the contagion spreads more quickly and the maximum fraction of total infected gets bigger, independently by the details of the topology (at a qualitative level). This property is the one that the standard SIR model is able to reproduce quite well. <br>
For this reason, it is interesting to look at the average path length in the different kinds of network varying the parameters with which they are constructed at fixed number of nodes ($Ntot=400$ as before), as seen in the following plots.

![apl_ER](https://github.com/simoneart/ABM-project/assets/95907355/ec5bd95a-e8cf-4e73-b0bc-dd7a072115c5)
![apl_WS1](https://github.com/simoneart/ABM-project/assets/95907355/0598fa46-8e7a-4d0f-aa1a-6af42810c5c9)
![apl_WS2](https://github.com/simoneart/ABM-project/assets/95907355/7e699046-67c7-4893-80f6-176ebc6d68a0)
![apl_BA](https://github.com/simoneart/ABM-project/assets/95907355/e93c2d00-5cbb-47bb-b39a-0de114b749a9)

In both the Barabasi-Albert and Watts-Strogatz networks the average path length decays very fast increasing the values of the parameters, while the Erdos-Renyi network shows a more rich behaviour with an increasiing trend followed by a slower decay compared to the other two topologies. 

## Conclusions 
A comparison between different methods for simulationg a simple SIR model has been carried out. In particular, the differential equation approach and the implementations on different network topologies were considered, highligthinh out how the average shortest path length of the graphs is a relevant quantity in understanding the strength of the epidemic diffusion. This featrure is captured in a simplified way in the random-mixing hypothesis used for writing the SIR DEs. Finally, a quick study of the dependece of $&lt l &gt$ on the paramters used to initialize the graphs was done. <br>
  
