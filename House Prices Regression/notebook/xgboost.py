import pandas as pd
import numpy as np
from sklearn.cross_validation import StratifiedKFold, KFold
import xgboost
from sklearn.grid_search import ParameterGrid
from sklearn.metrics import mean_squared_error

CLASS = False  # Whether classification or regression
SCORE_MIN = True  # Optimizing score through minimum
k = 5  # Number of folds
best_score = 10
best_params = None
best_iter = None

train_name = '../input/train.csv'
test_name = '../input/test.csv'
submission_name = '../input/sample_submission.csv'
submission_col = 'SalePrice'
submission_target = 'test_sub1.csv'

# Read files
train = pd.DataFrame.from_csv(train_name)
train = train.fillna(-1)
test = pd.DataFrame.from_csv(test_name)
test = test.fillna(-1)
submission = pd.DataFrame.from_csv(submission_name)
# Extract target
target = train['SalePrice']
del train['SalePrice']

# Label nominal variables to numbers
columns = train.columns.values
nom_numeric_cols = ['MSSubClass']
dummy_train = []
dummy_test = []
for col in columns:
    # Only works for nominal data without a lot of factors
    if train[col].dtype.name == 'object' or col in nom_numeric_cols:
        dummy_train.append(pd.get_dummies(train[col].values.astype(str), col))
        dummy_train[-1].index = train.index
        dummy_test.append(pd.get_dummies(test[col].values.astype(str), col))
        dummy_test[-1].index = test.index
        del train[col]
        del test[col]
train = pd.concat([train] + dummy_train, axis=1)
test = pd.concat([test] + dummy_test, axis=1)

# Use only common columns
columns = []
for col_a in train.columns.values:
    if col_a in test.columns.values:
        columns.append(col_a)
train = train[columns]
test = test[columns]

# CV
train = np.array(train)
target = np.log(np.array(target))  # Changes to Log
test = np.array(test)
print(train.shape, test.shape)

if CLASS:
    kfold = StratifiedKFold(target, k)
else:
    kfold = KFold(train.shape[0], k)

early_stopping = 50

param_grid = [
              {'silent': [1],
               'nthread': [2],
               'eval_metric': ['rmse'],
               'eta': [0.03],
               'objective': ['reg:linear'],
               'max_depth': [5, 7],
               'num_round': [1000],
               'subsample': [0.2, 0.4, 0.6],
               'colsample_bytree': [0.3, 0.5, 0.7],
               }
              ]

# Hyperparmeter grid optimization
for params in ParameterGrid(param_grid):
    print(params)
    # Determine best n_rounds
    xgboost_rounds = []
    for train_index, test_index in kfold:
        X_train, X_test = train[train_index], train[test_index]
        y_train, y_test = target[train_index], target[test_index]

        xg_train = xgboost.DMatrix(X_train, label=y_train)
        xg_test = xgboost.DMatrix(X_test, label=y_test)

        watchlist = [(xg_train, 'train'), (xg_test, 'test')]

        num_round = params['num_round']
        xgclassifier = xgboost.train(params, xg_train, num_round,
                                     watchlist,
                                     early_stopping_rounds=early_stopping);
        xgboost_rounds.append(xgclassifier.best_iteration)

    num_round = int(np.mean(xgboost_rounds))
    print('The best n_rounds is %d' % num_round)
    # Solve CV
    rmsle_score = []
    for cv_train_index, cv_test_index in kfold:
        X_train, X_test = train[cv_train_index, :], train[cv_test_index, :]
        y_train, y_test = target[cv_train_index], target[cv_test_index]

        # train machine learning
        xg_train = xgboost.DMatrix(X_train, label=y_train)
        xg_test = xgboost.DMatrix(X_test, label=y_test)

        watchlist = [(xg_train, 'train'), (xg_test, 'test')]

        xgclassifier = xgboost.train(params, xg_train, num_round);

        # predict
        predicted_results = xgclassifier.predict(xg_test)
        rmsle_score.append(np.sqrt(mean_squared_error(y_test, predicted_results)))

    if SCORE_MIN:
        if best_score > np.mean(rmsle_score):
            print(np.mean(rmsle_score))
            print('new best')
            best_score = np.mean(rmsle_score)
            best_params = params
            best_iter = num_round
    else:
        if best_score < np.mean(rmsle_score):
            print(np.mean(rmsle_score))
            print('new best')
            best_score = np.mean(rmsle_score)
            best_params = params
            best_iter = num_round

# Solution using best parameters
print('best params: %s' % best_params)
print('best score: %f' % best_score)
xg_train = xgboost.DMatrix(train, label=target)
xg_test = xgboost.DMatrix(test)
watchlist = [(xg_train, 'train')]
num_round = best_iter  # already int
xgclassifier = xgboost.train(best_params, xg_train, num_round, watchlist);
submission[submission_col] = np.exp(xgclassifier.predict(xg_test))
submission.to_csv(submission_target)