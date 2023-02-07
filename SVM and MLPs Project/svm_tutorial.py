import matplotlib.pyplot as plt
import numpy as np
from sklearn import svm

# linear data
X = np.array([1, 5, 1.5, 8, 1, 9, 7, 8.7, 2.3, 5.5, 7.7, 6.1])
y = np.array([2, 8, 1.8, 8, 0.6, 11, 10, 9.4, 4, 3, 8.8, 7.5])

# show unclassified data
plt.scatter(X, y)
plt.show()

# shaping data for training the model, we use vstack function to stack the two arragys and then use transpose to make is 12x2 shape.
training_X = np.vstack((X, y)).T
training_y = [0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1]

# define the model
# kernel{‘linear’, ‘poly’, ‘rbf’, ‘sigmoid’, ‘precomputed’} or callable, default=’rbf’
# Cfloat, default=1.0 Regularization parameter.
clf = svm.SVC(kernel='linear', C=1.0)
# train the model
clf.fit(training_X, training_y)

# remember that equation of Hyperplane in 2 dimension is
# W[0]*X[0]+W[1]*X[1]+y_intercept=0,
# here W are weights of features given by clf.coef_ and Y_intercept is given by clf_intercept_[0],
# X[1]=-W[0]/W[1] * X[0] - y_intercept/W[1]

# get the weight values for the linear equation from the trained SVM model

w=clf.coef_[0]

# make the x-axis space for the data points
XX = np.linspace(0, 13)

# get the y-values to plot the decision boundary
yy = -w[0]/w[1] * XX - clf.intercept_[0] / w[1]

# yy = w[0] * XX + clf.intercept_[0]

print(clf.intercept_[0] / w[1])
# plot the decision boundary
plt.plot(XX, yy, 'r-')

# show the plot visually
plt.scatter(training_X[:, 0], training_X[:, 1], c=training_y)
# plt.legend()
plt.show()