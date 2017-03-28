def regularized_eigenvectors(A, d, K, alpha):

    import numpy as np
    import math as math
    from scipy.sparse.linalg.eigen.arpack import eigsh as largest_eigsh

    d = np.array(d)
    n = len(A[:, 1])
    # Compute the degrees and other related metrics
    dalpha = np.power(d, -alpha)

    d1alpha = np.power(d, (alpha - 1))
    invDalpha = np.diag(dalpha[:, 0])
    invD1alpha = np.diag(d1alpha[:, 0])


    # Compute the affinity matrix L_alpha
    B = (A - d.dot(np.transpose(d)) / (np.transpose(d).dot((np.ones((n, 1)))))) / math.sqrt(n)
    L_alpha = (invDalpha.dot(B)).dot(invDalpha)

    # Compute the dominant eigenvectors of L_alpha
    evals_large_sparse, evecs_large_sparse = largest_eigsh(L_alpha, K-1, which='LM')

    #Normalize the dominant eigenvectors
    normalized_evecs = invD1alpha.dot(evecs_large_sparse)

    return normalized_evecs
