import numpy as np
# Testing set

X = np.array([[-1,1],[2,-2],[-1,-1.5],[-2, -1],[-2, 1],[1.5,0.5]])
# labels for the calculation must be in this format for the peceptron to work correctly, making the first one positive for the sole reason of having the learning rate from class
y = np.array([1,-1,-1,-1,1,-1,1,1])
# starting perceptron function
#drop the features to make prediction on as x and the y will be the
def perceptron(X, Y):
    # this should be the learning rate for ours it was set at 05
    learning_rate = 0.2
    # this is to calculate wsub 0
    w = np.zeros(len(X[0]))
    # the number of times a set is ran through the traning
    times_running = 5
# t as the current ineteration
    for t in range(times_running):
        # for i, features in enumerate(X):
            # sum product over the last axis of a and b.
        if (np.dot(X[t], w)*Y[t]) <= 0:
            w = w + learning_rate*X[t]*Y[t]
            # this should print weigths
            print(w)
                #WWWWORKS


w_list = perceptron(X,y)
