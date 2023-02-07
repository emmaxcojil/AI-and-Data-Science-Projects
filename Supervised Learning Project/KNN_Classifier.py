import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import mglearn

#Now let’s look at how we can apply the k-nearest neighbors algorithm using scikit- learn. First, we split our data into a training and a test set so we can evaluate general‐ ization performance

from sklearn.model_selection import train_test_split

X, y = mglearn.datasets.make_forge()
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

#Next, we import and instantiate the class. This is when we can set parameters, like the number of neighbors to use. Here, we set it to 3

from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier(n_neighbors=3)

#Now, we fit the classifier using the training set. For KNeighborsClassifier this means storing the dataset, so we can compute neighbors during prediction:
clf.fit(X_train, y_train)

#To make predictions on the test data, we call the predict method. For each data point in the test set, this computes its nearest neighbors in the training set and finds the most common class among these
print("Test set predictions: {}".format(clf.predict(X_test)))

#To evaluate how well our model generalizes, we can call the score method with  test data together with the test labels:
print("Test set accuracy: {:.2f}".format(clf.score(X_test, y_test)))


#The following code produces the visualizations of the decision boundaries for one, three, and nine neighbors

fig, axes = plt.subplots(1, 3, figsize=(10, 3))
#zip joines two tuples together

for n_neighbors, ax in zip([1, 3, 9], axes):
    # the fit method returns the object self, so we can instantiate
    # and fit in one line
    clf = KNeighborsClassifier(n_neighbors=n_neighbors).fit(X, y)
    mglearn.plots.plot_2d_separator(clf, X, fill=True, eps=0.5, ax=ax, alpha=.4)
    mglearn.discrete_scatter(X[:, 0], X[:, 1], y, ax=ax)
    ax.set_title("{} neighbor(s)".format(n_neighbors))
    ax.set_xlabel("feature 0")
    ax.set_ylabel("feature 1")
axes[0].legend(loc=3)
plt.show()