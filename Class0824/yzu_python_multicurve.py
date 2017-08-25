# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 00:11:40 2017

@author: AnCheTeng
"""
import matplotlib.pyplot as plt
from yzu_python_io import get_csv

def plot_csv(csv_name, label_name, color_name, marker_type):
    x_list, y_list = get_csv(csv_name)
    plt.plot(x_list, y_list, color=color_name, label=label_name,
             marker=marker_type, linewidth=1.5, markersize=10)
    plt.legend(loc=3,bbox_transform=plt.gcf().transFigure)
