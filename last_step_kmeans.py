def modified_kmeans(normalized_evecs, K, ground_truth, startGround_truth):
    import numpy as np
    from sklearn.cluster import KMeans
    from munkres import Munkres

    ## Number of instances
    n=len(ground_truth)

    ## k-means to normalized eigenvectors
    kmeans_output = KMeans(n_clusters=K, init='k-means++', random_state=None).fit(normalized_evecs)
    labels = kmeans_output.labels_

    #print labels



    ## Computation of the cost matrix
    costMat = np.zeros((int(K), int(K)))
    for a in range(int(0), int(K)):
        for b in range(int(0), int(K)):
            idd = np.where(labels == a)[0]
            if (startGround_truth == 0):
                costMat[a, b] = -(np.sum((np.array(ground_truth))[idd] == b)) ** 2
            else:
                costMat[a, b] = -(np.sum((np.array(ground_truth))[idd] == (b + 1))) ** 2
    #print costMat

    ## Find the best label permutation best matching the ground truth with the previous cost Matrix using the Hungarian Munkres algorithm
    m = Munkres()
    permutation = m.compute(costMat)
    #print  permutation
    perm = np.array(permutation)

    ## Permute the labels
    Labels = []
    for l in range(int(0), int(n)):
        for j in range(int(0), int(K)):
            if labels[l] == j:
                Labels.append(perm[j, 1])

    # Labels = np.transpose(labels)

    ## Compute the accuracy (normalized number of matching with the ground truth)
    if (startGround_truth == 0):
        accuracy = float(np.sum(((np.asarray(Labels)) == np.squeeze(ground_truth)))) / n
    else:
        accuracy = float(np.sum(((np.asarray(Labels) + 1) == np.squeeze(ground_truth)))) / n

    ## Compute the overlap performance
    perf = (accuracy - 1.0 / K) / (1 - 1.0 / K)
    print perf

    return perf
