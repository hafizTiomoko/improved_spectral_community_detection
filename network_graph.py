#### Import statements
def network_generate():
    import numpy as np
    import math as math
    import networkx as nx
    from scipy.stats import bernoulli

    ### We may have real world networks or synthetic graphs following the DCSBM

    ## Choice of the network to generate
    #network='real_world'   ## Choose either 'real_world' or 'DCSBM'
    network='DCSBM'

    if network=='real_world':
        ##Get the adjacency matrix
        #Given the network, find the corresponding adjacency matrix
        scenario='dolphins.gml'
        G = nx.read_gml(scenario)
        G_0=G

        ##Remove nodes without neighbors
        isolated_nodes=nx.isolates(G)
        G.remove_nodes_from(isolated_nodes)

        ## Adjacency matrix
        A=nx.adjacency_matrix(G,nodelist=None,weight=None)
        A=A.todense()

        ##New number of instances after removing isolated nodes
        n=len(A[:,1])

        ## Ground truth
        ground_truth=np.zeros((n,1))
        for i in range(int(0),int(n)):
            if(0 in G_0.nodes()):
                ground_truth[i] = G_0.node[i]['value']
            else:
                ground_truth[i] = G_0.node[i+1]['value']

        ## Remove the label of the node with no neighbor
        np.delete(ground_truth,isolated_nodes)
        ##Check wether the first element of the ground truth start from 0 or from 1
        if(min(ground_truth)==0):
            startGround_truth=0
        else:
            startGround_truth = 1

    if network=='DCSBM':
        n_init=1000
        ##Class proportions
        cs = [0.25,0.25,0.5]
        ## Number of classes
        K = len(cs)
        ## Number of instances per class
        ns =np.array(cs) * n_init

        ##Setting of the model parameters
        ## Average connectivities q's
        #bs = [0.25,0.75]
        bs = [0.75, 0.25]
        q1 = 0.4
        q2= 0.8
        q=np.repeat(np.array([q1,q2]),[int(n_init*bs[0]),int(n_init*bs[1])])

        # Choice of affinity matrix M
        #M = 10 * (-1 * np.ones(K) + 2 * np.identity(K))
        M=5*np.identity(K)
        # Construction of C
        C = np.ones((int(K),int(K)))+M/math.sqrt(n_init)

        ##Extenxion of C in an nxn bloc matrix
        large_C=np.zeros((int(n_init),int(n_init)))
        for i in range(int(0),int(K)):
            for j in range(int(0),int(K)):
                large_C[int(np.sum(ns[int(0):i])):int(np.sum(ns[int(0):i+1])),int(np.sum(ns[int(0):j])):int(np.sum(ns[int(0):j+1]))]=C[i,j]*np.ones((ns[i],ns[j]))

        ## Construction of matrix of DCSBM edge probabilities
        P=np.minimum(((np.diag(q)).dot(large_C)).dot(np.diag(q)),np.ones((n_init,n_init)))
        ## Generation adjacency matrix A
        A = np.zeros((int(n_init), int(n_init)))
        for i in range(int(0),int(n_init)):
            #A[i,]=np.random.binomial(1,P[i,], size=n)
            A[i,]=bernoulli.rvs(P[i,:],size=n_init)

        ## Ground_truth
        ground_truth = np.zeros((n_init,1))
        for i in range(int(0),int(K)):
            ground_truth[int(np.sum(ns[int(0):i])):int(np.sum(ns[int(0):i+1]))]=i* np.ones((ns[i],1))

        ##Construct graph from adjacency matrix
        G = nx.from_numpy_matrix(A)
        ##Remove nodes without neighbors
        isolated_nodes=nx.isolates(G)
        G.remove_nodes_from(isolated_nodes)
        ## Remove the label of the node with no neighbor
        np.delete(ground_truth,isolated_nodes)

        A=nx.adjacency_matrix(G,nodelist=None,weight=None)
        A=A.todense()

        ## Symmetrization of the adjacency matrix in order to have an undirected unweighted graph
        A = np.triu(A)+np.transpose(np.triu(A))
        startGround_truth=0

    return A,ground_truth,startGround_truth
