# kmeans clustering
## _implement k-means from scratch!_

[![N|Solid](https://cldup.com/dTxpPi9lDf.thumb.png)](https://nodesource.com/products/nsolid)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

With this code i have tried to cluster data by using k-means algorithm .
Unsupervised Machine Learning is the process of teaching a computer to use unlabeled, unclassified data and enabling the algorithm to operate on that data without supervision. Without any previous data training, the machine’s job in this case is to organize unsorted data according to parallels, patterns, and variations.

The goal of clustering is to divide the population or set of data points into a number of groups so that the data points within each group are more comparable to one another and different from the data points within the other groups. It is essentially a grouping of things based on how similar and different they are to one another.

We are given a data set of items, with certain features, and values for these features (like a vector). The task is to categorize those items into groups. To achieve this, we will use the K-means algorithm; an unsupervised learning algorithm. ‘K’ in the name of the algorithm represents the number of groups/clusters we want to classify our items into.

## dataset

- feature_1 is Y or latitude
- feature_2 is X or longitude

After loading data from csv by plotting the data we can recognized that thet 5 group is exist in data.
- first we try to chose five centroid randomly Then, assign each remaining points to the closest centroid based on some distance measure, such as how far they are from each other. This forms k clusters around the centroids.
- Next, update the centroids by calculating the average or the mean of all the things in each cluster. This moves the centroids to the middle of their clusters. _recalculate_centroids_
- repeat these steps until the centroids stop moving or change very little. This means that you have found a stable grouping. _recalculate_clusters_