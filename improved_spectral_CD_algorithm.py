import numpy as np
import math as math
from network_graph import network_generate
from optimal_alpha import optimal_alpha
from eigenvectors import regularized_eigenvectors
from last_step_kmeans import modified_kmeans


### Get the graph on which we want to extract the communities
A, ground_truth, startGround_truth = network_generate()  ## startGround_truth is 0 when the minimum value of the ground truth is 0 and 1 otherwise
### Get the adjacency matrix and the ground_truth from csv files
#A = np.genfromtxt('adjacency.csv', delimiter=",")
#ground_truth = np.genfromtxt('conf_true.csv', delimiter=",")

n=len(A[:,1])

## Step 1: Compute the optimal value of \alpha

#### The following part is concerned by the estimation of the model parameters given the adjacency matrix
## Degree vector
d = A.dot(np.ones((n, 1)))

##Estimate the average connectivities
qEst = d / math.sqrt(np.sum(d))

## Number of classes
if (startGround_truth == 0):
    K = int(np.amax(ground_truth) + 1)
else:
    K = int(np.amax(ground_truth))
print K

alpha=optimal_alpha(qEst,n)
#print alpha


#### Step 2: Leading eigenvectors of L_alpha extraction
normalized_evecs=regularized_eigenvectors(A, d, K, alpha)


### Step 3: Kmeans on the normalized eigenvectors and computation of performances
perf = modified_kmeans(normalized_evecs, K, ground_truth, startGround_truth)


