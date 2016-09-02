# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-02 13:16:14
# @Last Modified time: 2016-09-02 13:20:20
# @FileName: datatrain.py

import numpy as np
import sklearn as sk

class ModelTrain(Object):
    def __init__(self):
        self.train_data = np.loadtxt('train.in')

