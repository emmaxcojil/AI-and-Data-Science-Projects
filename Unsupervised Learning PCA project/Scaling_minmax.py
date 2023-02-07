from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
cancer = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target,random_state=1)
print(X_train.shape)
print(X_test.shape)
#note down the output


from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler(feature_range=(0, 1))
scaler.fit(X_train)
# transform data

X_train_scaled = scaler.transform(X_train)
# print dataset properties before and after scaling
print("transformed shape: {}".format(X_train_scaled.shape))
print("per-feature minimum before scaling (train data):\n {}".format(X_train.min(axis=0)))
print("per-feature maximum before scaling (train data):\n {}".format(X_train.max(axis=0)))
print("per-feature minimum after scaling (train data):\n {}".format(X_train_scaled.min(axis=0)))
print("per-feature maximum after scaling (train data):\n {}".format(X_train_scaled.max(axis=0)))

# transform test data
X_test_scaled = scaler.transform(X_test)
# print test data properties after scaling
print("per-feature minimum after scaling (test data):\n{}".format(X_test_scaled.min(axis=0)))
print("per-feature maximum after scaling (test data):\n{}".format(X_test_scaled.max(axis=0)))


