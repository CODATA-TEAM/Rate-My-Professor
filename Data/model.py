# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-03 00:44:31
# @Last Modified time: 2016-09-03 01:10:01
# @FileName: model.py

import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.svm import SVR
from sklearn.grid_search import GridSearchCV
from sklearn.linear_model import LogisticRegression

# Load Train dataset
data = np.loadtxt('train.in')
# helpfulness | 7| 8| 9| 10| 11| 12-31| 32| 33| 34
help_data_X = data[:, 7:34]
help_data_y = data[:, 34]

# clarity | 3| 4| 5| 6| 9| 10| 11| 12-31|32 |33| 35
clar_data_X1 = data[:, 3:7]
clar_data_X2 = data[:, 9:34]
clar_data_X = np.concatenate((clar_data_X1, clar_data_X2), axis=1)
clar_data_y = data[:, 35]


hX_train, hX_test, hy_train, hy_test = train_test_split(help_data_X, help_data_y, test_size=0.2, random_state=42)
cX_train, cX_test, cy_train, cy_test = train_test_split(clar_data_X, clar_data_y, test_size=0.2, random_state=42)

# svr = GridSearchCV(SVR(kernel='rbf', gamma=0.1), cv=5,
#                    param_grid={"C": [1e0, 1e1, 1e2, 1e3],
#                                "gamma": np.logspace(-2, 2, 5)})
lr = LogisticRegression()
# svr = GridSearchCV(SVR(kernel='rbf', gamma=0.1), cv=5,
#                    param_grid={"C": [1e0],
#                                "gamma": np.logspace(-2,5)})
# svr.fit(hX_train, hy_train)
# y_svr = svr.predict(hX_test)
lr.fit(hX_train, hy_train)
y_lr = lr.predict(hX_test)
mse = mean_squared_error(hy_test, y_lr)
print("MSE HELP: {}".format(mse))

# svr_c = GridSearchCV(SVR(kernel='rbf', gamma=0.1), cv=5,
#                    param_grid={"C": [1e0, 1e1, 1e2, 1e3],
#                                "gamma": np.logspace(-2, 2, 5)})
# svr_c.fit(cX_train, cy_train)
# y_svr_c = svr_c.predict(cX_test)
# mse = mean_squared_error(cy_test, y_svr_c)
# print("MSE: {}".format(mse))
clr = LogisticRegression()
clr.fit(cX_train, cy_train)
y_clr = clr.predict(cX_test)
mse = mean_squared_error(cy_test, y_clr)
print("MSE CLAR: {}".format(mse))