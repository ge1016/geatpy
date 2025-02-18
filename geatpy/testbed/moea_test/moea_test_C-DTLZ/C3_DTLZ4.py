# -*- coding: utf-8 -*-
import numpy as np
import geatpy as ga

class C3_DTLZ4(ga.Problem): # 继承Problem父类
    def __init__(self, M):
        self.name = 'C3-DTLZ4' # 初始化name（函数名称，可以随意设置）
        self.M = M # 初始化M（目标维数）
        self.maxormins = [1] * self.M # 初始化maxormins（目标最小最大化标记列表）
        self.Dim = self.M + 9 # 初始化Dim（决策变量维数）
        self.varTypes = np.array([0] * self.Dim) # 初始化varTypes（决策变量的类型）
        lb = [0] * self.Dim # 决策变量下界
        ub = [1] * self.Dim # 决策变量上界
        self.ranges = np.array([lb, ub]) # 初始化ranges（决策变量范围矩阵）
        lbin = [1] * self.Dim
        ubin = [1] * self.Dim
        self.borders = np.array([lbin, ubin]) # 初始化borders（决策变量范围边界矩阵）
    
    def aimFuc(self, Vars, CV):
        alpha = 100
        M = Vars.shape[1] - 9 # M is the dimension
        XM = Vars[:,(M-1):]
        g = np.array([np.sum((XM - 0.5) ** 2, 1)]).T
        ones_metrix = np.ones((g.shape[0], 1))
        ObjV = np.fliplr(np.cumprod(np.hstack([ones_metrix, np.cos(Vars[:,:M-1]**alpha * np.pi / 2)]), 1)) * np.hstack([ones_metrix, np.sin(Vars[:, range(M - 2, -1, -1)]**alpha * np.pi / 2)]) * np.tile(1 + g, (1, M))
        # 计算可行度矩阵的值
        CV = 1 + 3/4 * ObjV**2 - np.array([np.sum(ObjV**2, 1)]).T
        
        return ObjV, CV
    
    def calBest(self):
        realBestObjV = np.loadtxt("True_PF/C3_DTLZ4.csv",delimiter=",",usecols=range(self.M)) # 读取真实前沿数据
        return realBestObjV
    