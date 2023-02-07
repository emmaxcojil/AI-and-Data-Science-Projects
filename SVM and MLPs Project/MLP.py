
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import mglearn
from sklearn.neural_network import MLPClassifier
from sklearn.datasets import make_moons

X, y = make_moons(n_samples=100, noise=0.25, random_state=3)
#if test size, train size is not mentioned, default is 0.25,
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)
# by default MLPClassifier uses 100 layer
#mlp = MLPClassifier(solver='lbfgs', random_state=1).fit(X_train, y_train)
#by default MLP uses 100 nodes, if we reduce this to 10, as our data set is small, we will still get good results
#mlp = MLPClassifier(solver='lbfgs', random_state=1, hidden_layer_sizes=[10]).fit(X_train, y_train)

#by default MLP uses 1 hidden layer, if we want to use two hidden layers each with 10 nodes,
#mlp = MLPClassifier(solver='lbfgs', random_state=1, hidden_layer_sizes=[10,10]).fit(X_train, y_train)

#by default MLP uses relu, you can try using tanh
mlp = MLPClassifier(solver='lbfgs', activation='tanh', random_state=0, hidden_layer_sizes=[10,10]).fit(X_train, y_train)


mglearn.plots.plot_2d_separator(mlp, X_train, fill=True, alpha=.3)
mglearn.discrete_scatter(X_train[:, 0], X_train[:, 1], y_train)

plt.xlabel("First Feature")
plt.ylabel("Second Feature")
plt.show()