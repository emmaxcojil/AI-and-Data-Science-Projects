
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
import graphviz
from IPython.display import Image, display

cancer = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(
cancer.data, cancer.target, stratify=cancer.target, random_state=42)

# in the following if we not set max_feature, it means there is no limit, so comment of the two lines below
tree = DecisionTreeClassifier(max_depth=4, random_state=0)
#tree = DecisionTreeClassifier(random_state=0)

tree.fit(X_train, y_train)
print("Accuracy on training set: {:.3f}".format(tree.score(X_train, y_train)))
print("Accuracy on test set: {:.3f}".format(tree.score(X_test, y_test)))

# export_graphviz(tree, out_file="tree.dot", class_names=["malignant", "benign"],
#                 feature_names=cancer.feature_names, impurity=False, filled=True)
# with open("tree.dot") as f:
#     dot_graph = f.read()
# graphviz.Source(dot_graph).view()
#
