

from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import mglearn
from sklearn.neural_network import MLPClassifier
from sklearn.datasets import make_moons

from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer()

mglearn.plots.plot_scaling()
plt.show()