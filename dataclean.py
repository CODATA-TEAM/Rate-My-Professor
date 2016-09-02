# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-01 17:11:47
# @Last Modified time: 2016-09-01 18:23:33
# @FileName: dataclean.py

import pandas as pd


# calculate the number of Nan in a list
def calNan(data_list):
    res = 0
    for i in data_list:
        if i != i:
            res += 1
    return res

# solve attendance column data, 
# return a list
def solveAttendance(data_list):
    res_list = []
    for i in data_list:
        if i == i:
            if 'Not' in i:
                res_list.append(-1)
            else: 
                res_list.append(1)
        else:
            res_list.append(0)
    # print(calNan(data_list))
    # print res_list
    return res_list

def main():
    data = pd.read_csv("Data\\train.csv")
    attendance_list = solveAttendance(data['attendance'])
    return attendance_list

if __name__ == '__main__':
    main()
