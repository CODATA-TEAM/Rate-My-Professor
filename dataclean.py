# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-01 17:11:47
# @Last Modified time: 2016-09-01 18:11:56
# @FileName: dataclean.py

import pandas as pd


# calculate the number of Nan in a list
def calNan(data_list):
    res = 0
    for i in data_list:
        if i != i:
            res += 1
    return res

def solveAttendance(data_list):
    print(calNan(data_list))

def main():
    data = pd.read_csv('Data\\train.csv')
    solveAttendance(data['attendance'])

if __name__ == '__main__':
    main()
