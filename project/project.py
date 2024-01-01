import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def plot_data(df):
    plt.xlabel("feature_2")
    plt.ylabel("feature_1")
    plt.title("scatter plot before clusttering")
    plt.scatter(x=df.iloc[2], y=df.iloc[1],cmap='jet')
    plt.savefig(r'./scatterplot-before-clustering.jpg')
    return "done"

#  فانکشن محاسبه فاصله هر نقطه با نقاط مرکزی با هدف تخصیص نقاط به کلاستر های مربوطه بر اساس کمترین فاصله

def recalculate_clusters(X, centroids, k):
   # Recalculates the clusters
    # Initiate empty clusters
    clusters = {}
    for i in range(k):
        clusters[i] = []
    for data in X:
        euc_dist = []
        for j in range(k):
            euc_dist.append(np.linalg.norm(data - centroids[j]))
        # Append the cluster of data to the dictionary
        clusters[euc_dist.index(min(euc_dist))].append(data)
    return clusters


#--------------------------------------------------------------------------------
#   فانکشن محاسبه مجدد نقاط مرکزی بر اساس میانگین نقاط موجود در هر کلاستر


def recalculate_centroids(centroids, clusters, k):
    # Recalculates the centroid position based on the plot
    for i in range(k):
        centroids[i] = np.average(clusters[i], axis=0)
    return centroids


#sum squared error--------------------------------------------------------------------

def sse(x, clusters, centroids):
    errors = []

    for i,k in zip(clusters,centroids):
        for j in clusters[i]:
            #compute the distance (error) between one point and its closest centroid
            error = np.linalg.norm(np.array(j) - np.array(centroids[k]))
            #append squared error to the list of error
            errors.append(error**2)

    #and sum up all the errors
    sse = sum(errors)
    return sse

#-------------------------------فانکشن کلاسترینگ---------------------------------------------

def kmeans_clustering(x,k,max_iter = 100, tol = pow(10,-3) ):
    it = -1
    all_sse = []
    clusters = {}
    centroids = {}
    for i in range(k):
        clusters[i] = []

    for i in range(k):
        centroids[i] = x[i]

    while (len(all_sse)<=1 or (it < max_iter and np.absolute(all_sse[it] - all_sse[it-1])/all_sse[it-1] >= tol)):
        it += 1
        clust=recalculate_clusters(x,centroids, k)
        centroids=recalculate_centroids(centroids, clust, k)
        sse_kmeans = sse(x, clust, centroids)
        all_sse.append(sse_kmeans)
    return clust,centroids

def main():
    df=pd.read_csv("./rc_task_2.csv",header=None)
    plot_data(df)
    data = np.loadtxt("./rc_task_2.csv",delimiter=",",skiprows=1)
    final_clust,centroids=kmeans_clustering(data,k=5)
    print(centroids)
    df['cluster']=""
    for i in final_clust:
         for j in final_clust[i]:
             for k in df.index:
                 if list(j)==list(df.iloc[k,[0,1]]):
                     df['cluster'].iloc[k]=i

if __name__ == "__main__":
    main()
