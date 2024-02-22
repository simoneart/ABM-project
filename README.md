# Implementation of the SIR epidemic model on networks <br>
## Exam project for the PhD course 'Agent-Based models' 
### Goal
The goal of the project is to compare the epidemic spreading on different network topologies and to study the dependence of the populations dynamics (i.e. the densities of the S, I and R agents over time) on the choice of parameters. <br> 
### Short introduction
Epidemic models have their origin in the compartimental model SIR developed in the early 20th century. In this simple model the population is divided in three different groups: the Susceptibles (S), who are the agents that can be infected, the Infected (I), who are the agents that can in some way spread the disease and the Removed (R), which are those who either have recovered from the disease and cannot be infected anymore or are deceased. <br> How these agents change their state, i.e. move between compartments, is assumed to be governed by the following set of differential equations:
\begin{equation}
test
\end{equation}
### Method
Square lattice, Erdos-Renyi, Watts-Strogatz and Barabasi-Albert networks are considered. They are generated through a series of functions in nwSIR_functions.py in such a way that each node correspond to a certain agent (S=0, I=1, R=2) and they are initialized with a given number of initial infected positioned at random in the graph. Given a certain graph realization, its epidemic dynamics is repeated a number of times to study the statistics of the spreading and finally graphs containing the populations trend and the degree distribution are produced for different choices of the parameters. <br>

