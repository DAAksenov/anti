import warnings
from typing import Tuple, Any, Union

from numpy import ndarray, dtype

warnings.filterwarnings("ignore")
import numpy as np
import uuid  # она нужна
import pickle
import uuid


class DecisionTreeRegressorFromScratch:

    def __init__(self, max_depth=None, tree_=None, min_samples_leaf=1):
        self.tree_ = {}
        self.max_depth_ = max_depth

    def mse(self, y_true, y_pred):
        return np.mean(np.power(y_true - y_pred, 2))

    def fit(self, X, y, tree_path='0'):

        if len(tree_path) - 1 == self.max_depth_ or X.shape[0] <= 1:
            self.tree_[tree_path] = np.mean(y)
            return

        minimum_mse = None
        best_split = None

        # For every unique value of every feature of X split the data in two parts:
        #   one part are observations which are less than or equal to this value
        #   second part are the others
        for feature in range(X.shape[1]):
            for value in sorted(set(X[:, feature])):

                less_than_or_equal_obs = X[:, feature] <= value  # select observations
                # which are less than or equal to value

                # one part are observations which are less than or equal to this value
                X1, y1 = X[less_than_or_equal_obs], y[less_than_or_equal_obs]

                # second part are the others
                X2, y2 = X[~less_than_or_equal_obs], y[~less_than_or_equal_obs]

                # Calculate weighted MSE for a split
                MSE1 = self.mse(y1, np.mean(y1))
                MSE2 = self.mse(y2, np.mean(y2))
                weight_1 = len(y1) / len(y)
                weight_2 = len(y2) / len(y)
                weighted_mse = MSE1 * weight_1 + MSE2 * weight_2

                # Update MSE
                if minimum_mse is None or weighted_mse < minimum_mse:
                    minimum_mse = weighted_mse
                    best_split = (feature, value)

        # Get samples with best split
        feature, value = best_split
        splitting_condition = X[:, feature] <= value
        X1, y1, X2, y2 = X[splitting_condition], y[splitting_condition], \
            X[~splitting_condition], y[~splitting_condition]

        #  Add the splitting condition to tree
        self.tree_[tree_path] = best_split

        # Continue growing the tree
        self.fit(X1, y1, tree_path=tree_path + '0')
        self.fit(X2, y2, tree_path=tree_path + '1')

    def predict(self, X, ):
        results = []
        for i in range(X.shape[0]):
            tree_path = '0'
            while True:
                value_for_path = self.tree_[tree_path]
                if type(value_for_path) != tuple:
                    result = value_for_path
                    break
                feature, value = value_for_path
                if X[i, feature] <= value:
                    tree_path += '0'
                else:
                    tree_path += '1'
            results.append(result)
        return np.array(results)


class GradientBoostingRegressorFromScratch:

    def fit(self, X, y):

        self.trees = []  # Create a list to store trees

        for i in range(100):
            tree = DecisionTreeRegressorFromScratch(3)
            tree.fit(X, y - self.predict(X))  # Fit the tree to data
            self.trees.append(tree)  # Add the tree to the list of trees

        return self.trees

    def predict(self, X):

        # Create array to store predictions
        trees_predictions = np.zeros((len(X), len(self.trees)))

        # Predict for each observation for each tree
        for i, tree in enumerate(self.trees):
            # Predict with a tree and multiply by learning rate
            trees_predictions[:, i] = tree.predict(X) * (1 if i == 0 else 0.1)

        # Return a sum of all trees predictions for each observation
        return np.sum(trees_predictions, axis=1)


def predict(filename_model: str, filename_data: str, file_name_real: str) -> tuple[ndarray[Any], ndarray[Any]]:
    try:
        x_test = np.genfromtxt(filename_data, delimiter=';')
        y_real = np.genfromtxt(file_name_real, delimiter=';')[:, 4]
    except:
        return 'Error'
    try:
        with open(filename_model, 'rb') as f:
            model = pickle.load(f)
            y_pred = model.predict(x_test)
    except:
        return 'Error'
    else:
        return y_real, y_pred


def fit(file_name: str) -> str:
    try:
        data = np.genfromtxt(file_name, delimiter=';')
        x_train, y_train = data[:, :3], data[:, 4]
    except:
        return 'Error'
    model = GradientBoostingRegressorFromScratch()
    model.fit(x_train, y_train)
    unique_filename = str(uuid.uuid4()) + '.pkl'
    try:
        with open(unique_filename, 'wb') as f:
            pickle.dump(model, f)
    except:
        return 'Error'
    else:
        return unique_filename


model_name = fit('train.csv')
y_real, y_pred = predict(model_name, 'test.csv', 'train.csv')

print(y_real, y_pred)
