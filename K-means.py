import numpy as np

import matplotlib.pyplot as plt

#data generation
X1, Y1 = np.random.multivariate_normal([4,4], [[1,0], [0, 1]], 100).T
X2, Y2 = np.random.multivariate_normal([-3,3], [[1.5,0], [0, .5]], 100).T
X3, Y3 = np.random.multivariate_normal([0,-3], [[1,0], [0, .75]], 100).T

X = np.append(X1, X2)
X = np.append(X, X3)
Y = np.append(Y1, Y2)
Y = np.append(Y, Y3)

data = np.zeros((300, 2))
#likely a more efficent way to do This
for i in range(300):
    data[i, 0] = X[i]
    data[i, 1] = Y[i]


#clustering
def clustering(X, iterations):
    centroids = np.random.rand(3, 2);

    assignments = np.zeros((300));

    dist = np.zeros((3));

    n1 = 0
    n2 = 0
    n3 = 0

    for j in range(iterations):

        for k in range(300):

            for i in range(3):

                dist[i] = np.linalg.norm(data[k, :] - centroids[i, :])

                assignments[k] = np.argmin(dist)


        for k in range(300):

            if assignments[k] == 0:

                plt.scatter(data[k, 0], data[k, 1], color = "red")

                centroids[0, 0] = data[k, 0] + centroids[0, 0]
                centroids[0, 1] = data[k, 1] + centroids[0, 1]

                n1 = n1 + 1

            elif assignments[k] == 1:

                plt.scatter(data[k, 0], data[k, 1], color = "blue")

                centroids[1, 0] = data[k, 0] + centroids[1, 0]
                centroids[1, 1] = data[k, 1] + centroids[1, 1]

                n2 = n2 + 1
            else:

                plt.scatter(data[k, 0], data[k, 1], color = "green")

                centroids[2, 0] = data[k, 0] + centroids[2, 0]
                centroids[2, 1] = data[k, 1] + centroids[2, 1]

                n3 = n3 + 1

        centroids[0,0] = centroids[0,0]/n1
        centroids[0,1] = centroids[0,1]/n1
        centroids[1,0] = centroids[1,0]/n2
        centroids[1,1] = centroids[1,1]/n2
        centroids[2,0] = centroids[2,0]/n3
        centroids[2,1] = centroids[2,1]/n3


    plt.show()


for i in range(3):
    clustering(data, i)
