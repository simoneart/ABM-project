import numpy as np
import random as rnd
import igraph as ig

'''
S = 0
I = 1
R = 2
'''

def lattice(Ntot, NI):
    '''
    

    Parameters
    ----------
    Ntot : total number of individuals.
    NI : number of initial infected.
        

    Returns
    -------
    initial population arranged in a lattice, with randomly distrubuted initial
    infectuos individuals.

    '''
    
    L = ig.Graph.Lattice([int(np.sqrt(Ntot)),int(np.sqrt(Ntot))], circular=False)
    L.vs['state'] = 0
    
    count = 0
    while count < NI:
        a = rnd.randint(0, Ntot-1)
        if L.vs[a]['state'] == 0:
            L.vs[a]['state'] = 1
            count += 1
    
    return L

def random_network(Ntot, NI, p):
    '''
    

    Parameters
    ----------
    Ntot : total number of individuals.
    NI :  number of initial infected.
    p : probability of forming an edge in the random graph

    Returns
    -------
    G : Renyi-Erdos random graph with values assigned to each node as the state
    of the individual. There are NI randomly selected infected nodes. 
           
    '''
    
    G = ig.Graph.Erdos_Renyi(Ntot, p)
    
    G.vs['state'] = 0
    
    count = 0
    while count < NI:
        a = rnd.randint(0, Ntot-1)
        if G.vs[a]['state'] == 0:
            G.vs[a]['state'] = 1
            count += 1
    
    return G

def SW_network(Ntot, NI, k, p):
    '''
    

    Parameters
    ----------
    Ntot : total number of individuals.
    NI :  number of initial infected.
    k : number of initial nn links on both sides.
    p : rewiring probability.

    Returns
    -------
    Watts-Strogatz graph with values assigned to each node as the state
    of the individual. There are NI randomly selected infected nodes.

    '''
    
    G = ig.Graph.Watts_Strogatz(1, Ntot, k, p)
    
    G.vs['state'] = 0
    
    count = 0
    while count < NI:
        a = rnd.randint(0, Ntot-1)
        if G.vs[a]['state'] == 0:
            G.vs[a]['state'] = 1
            count += 1
    
    return G

def scale_free_network(Ntot, NI, M):
    '''
    

    Parameters
    ----------
    Ntot : total number of individuals.
    NI :  number of initial infected.
    m : number of edges added to each new node.

    Returns
    -------
    Barbasi-Albert graph with values assigned to each node as the state
    of the individual. There are NI randomly selected infected nodes.

    '''
    
    G = ig.Graph.Barabasi(n=Ntot, m=M, power=1)
    
    G.vs['state'] = 0
    
    count = 0
    while count < NI:
        a = rnd.randint(0, Ntot-1)
        if G.vs[a]['state'] == 0:
            G.vs[a]['state'] = 1
            count += 1
    
    return G

def time_evo(graph, Nsteps, inf_rate, healing_rate):
    '''
    

    Parameters
    ----------
    graph : Initial graph to be evolved
    Nsteps : Number of steps
    inf_rate : Infectioon rate
    healing_rate : Healing rate

    Returns
    -------

    ro_sus : density of susceptibles against time
    ro_inf : density of infected against time
    ro_rec : density of recovered against time

    '''
    
    evo_graph = graph.copy()
    
    Ntot = evo_graph.vcount()
    
    ro_sus = np.zeros(Nsteps+1)
    ro_inf = np.zeros(Nsteps+1)
    ro_rec = np.zeros(Nsteps+1)
    
    #day = 0
    ro_sus[0] = sum([1 for i in range(Ntot) if  evo_graph.vs[i]['state'] == 0])/float(Ntot)
    ro_inf[0] = 1. - ro_sus[0]
    ro_rec[0] = 0
    
    neighborhoods = evo_graph.get_adjlist()
    
    for t in range(1,Nsteps+1):
        
        for i in range(Ntot):
            
            #updating the recovered
            if evo_graph.vs[i]['state'] == 1 and rnd.random() <= healing_rate:
                evo_graph.vs[i]['state'] = 2
                
            for neis in neighborhoods[i]:
                #updating the infected 
                if evo_graph.vs[i]['state'] == 0 and neis == 1 and rnd.random() <= inf_rate:
                    evo_graph.vs[i]['state'] = 1                    

        ro_sus[t] = sum([1 for i in range(Ntot) if  evo_graph.vs[i]['state'] == 0])/Ntot
        ro_inf[t] = sum([1 for i in range(Ntot) if  evo_graph.vs[i]['state'] == 1])/Ntot
        ro_rec[t] = sum([1 for i in range(Ntot) if  evo_graph.vs[i]['state'] == 2])/Ntot
    
    return [ro_sus, ro_inf, ro_rec]

def ensemble_stats(graph_topology, graph_parameters, Ntot, Nreal, Nsteps, inf_rate, healing_rate):
    '''
    

    Parameters
    ----------
    graph_topology : String type variable. Choose between 'Lattice', 'Erdos-Renyi',
                    'Watts-Strogatz', 'Barabasi-Albert'.
    graph_parameters : A list containing the appropriate set of parameters relative to the specific
                        graph. Order sensitive.
                        Lattice -> initial number of infected;
                        ER -> initial number of infected, probability of forming an edge;
                        WS -> initial number of infected, number of initial nn links on both sides,
                               rewiring probability.
                        BA -> initial number of infected, number of edges added to each new node
    Ntot : total number of agents
    Nreal : number of realizations of the time evolution considered
    Nsteps : Number of steps
    inf_rate : Infection rate
    healing_rate : Healing rate

    Returns
    -------
    Average density of S, I and R at each time step and corresponding variances. 

    '''
    if graph_topology == 'Lattice':
        G = lattice(Ntot, graph_parameters[0])
        
    elif graph_topology == 'Erdos-Renyi':
        G = random_network(Ntot, graph_parameters[0], graph_parameters[1])
        
    elif graph_topology == 'Watts-Strogatz':
        G = SW_network(Ntot, graph_parameters[0], graph_parameters[1], graph_parameters[2])
        
    elif graph_topology == 'Barabasi-Albert':
        G = scale_free_network(Ntot, graph_parameters[0], graph_parameters[1])
        
    #relevant structural properties of the graph
    pk = G.degree()
    ave_path_length = G.average_path_length()
    
    #define the ensembles of the densities, first index is the realization index,
    #second index is the time index.
    roS_ens = []
    roI_ens = []
    roR_ens = []
    
    #realizations of time evolution
    for n in range(Nreal):
        stuff = time_evo(G, Nsteps, inf_rate, healing_rate)
        roS_ens.append(stuff[0])
        roI_ens.append(stuff[1])
        roR_ens.append(stuff[2])
    
    roS_ens = np.array(roS_ens)
    roI_ens = np.array(roI_ens)
    roR_ens = np.array(roR_ens)
    
    roS_ave = np.zeros(Nsteps+1)
    roI_ave = np.zeros(Nsteps+1)
    roR_ave = np.zeros(Nsteps+1)
    
    roS_var = np.zeros(Nsteps+1)
    roI_var = np.zeros(Nsteps+1)
    roR_var = np.zeros(Nsteps+1)
    
    for i in range(Nsteps+1): #averages at each instant of time
        roS_ave[i] = sum(roS_ens[:,i])/Nreal
        roI_ave[i] = sum(roI_ens[:,i])/Nreal
        roR_ave[i] = sum(roR_ens[:,i])/Nreal
        
        roS_var[i] = sum([(roS_ens[j,i]-roS_ave[i])**2 for j in range(Nreal)])/(Nreal-1)
        roI_var[i] = sum([(roI_ens[j,i]-roI_ave[i])**2 for j in range(Nreal)])/(Nreal-1)
        roR_var[i] = sum([(roR_ens[j,i]-roR_ave[i])**2 for j in range(Nreal)])/(Nreal-1)
    
    return [[roS_ave, roI_ave, roR_ave], [roS_var, roI_var, roR_var], [pk, ave_path_length]]
