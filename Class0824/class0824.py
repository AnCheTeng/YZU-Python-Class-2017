# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 23:19:29 2017

@author: AnCheTeng
"""
from random import randint
import yzu_python_io as ypio
import yzu_python_multicurve as ypmc

# WRITE tutorial
noise = range(20)
error_rate1 = []
error_rate2 = []
error_rate3 = []
for i in range(20):
    error_rate1.append(randint(1, 10))
    error_rate2.append(randint(6, 15))
    error_rate3.append(randint(11, 20))
    
ypio.save_csv("Noise", noise, "Error-Rate1", error_rate1, "sim_result1.csv")
ypio.save_csv("Noise", noise, "Error-Rate2", error_rate2, "sim_result2.csv")
ypio.save_csv("Noise", noise, "Error-Rate3", error_rate3, "sim_result3.csv")


## READ tutorial
#x, y = ypio.get_csv("sim_result1.csv")
#print "X-list: "
#print x
#print "Y-list: "
#print y
#
#
#
#
## PLOT MultiCurve
#import matplotlib.pyplot as plt
#
#colors  = ["blue","red","green", "gray","black","orange"]
#markers = ["s" ,'o', 'D','^', '*', 'X']
#
#title_name = "Noise ratio vs. Error rate"
#file_names = ["sim_result1.csv", "sim_result2.csv", "sim_result3.csv"]
#label_names = ["Error-Rate-1", "Error-Rate-2", "Error-Rate-3"]
#
#plt.figure(figsize=(8,8))
#plt.xlabel("Noise Ratio", fontsize=18)
#plt.ylabel("Error Rate", fontsize=18)
#plt.title(title_name, fontsize=18)
#plt.grid(linestyle='--')
#
#for i in range(0, len(file_names)):
#    ypmc.plot_csv(file_names[i], label_names[i], colors[i], markers[i])
#
#plt.show()


