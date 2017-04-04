# Content
## [Improved spectral community detection in large heterogeneous graphs](http://romaincouillet.hebfree.org/docs/articles/JMVA_TIOMOKO.pdf)
This page contains the python code implementing our new spectral community detection algorithm based on a Random Matrix Theory 
analysis of graph similarity matrices. 
To recall, the algorithm consists of the following steps

### Computation of an estimate of the optimal value of the modularity normalization parameter alpha
  This is implementing with the function _optimal_alpha_
### Extraction of the dominant eigenvectors of L_alpha and regularization by D^(alpha-1) as described in the paper
  This is implementing with the function _regularized_eigenvectors_
### K-means on the previous regularized dominant eigenvectors and overlap performance of the algorithm
  This is implementing with the function _modified_kmeans_
  
  
## We have other useful codes for a visualization of the empirical and theoretical histograms of the eigenvalues of the similarity matrix L_alpha, the visualization of the dominant eigenvectors in 2D
  Histogram plots implemented in the function _histogram_eigenvalues_
  Eigenvectors plots implemented in the function _eigen_plots_
  
  
  # JUPITER NOTEBOOK
  You can use an interactive real-time version of the codes within your web-browser with our [Jupiter Notebook](https://github.com/hafizTiomoko/improved_spectral_community_detection/blob/master/RMT4CD.ipynb).
  
  # CONTACTS
  * Hafiz TIOMOKO ALI
    * Phd Student at CentraleSupélec
    * 3 Rue Joliot Curie, Plateau de Moulon, 91192 Gif-Sur-Yvette (France)
    * e-mail: tio.hafiz@gmail.com
    * Website: (http://laneas.com/hafiz-tiomoko-ali)
  * Romain COUILLET
    * Professor at CentraleSupélec
    * 3 Rue Joliot Curie, Plateau de Moulon, 91192 Gif-Sur-Yvette (France)
    * e-mail: romain.couillet@gmail.com
    * Website: (http://romaincouillet.hebfree.org/)
