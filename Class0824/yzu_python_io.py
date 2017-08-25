# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 23:40:54 2017

@author: AnCheTeng
"""

def save_csv(x_name, x_list, y_name, y_list, filename):
    if(len(x_list)!=len(y_list)):
        print "The length of x-list and y-list are not the same!"
        return
    
    filename = filename
    content = x_name + "," + y_name + "\n"
    for i in range(0, len(x_list)):
        content += str(x_list[i]) + "," + str(y_list[i]) + "\n"
    
    with open(filename, "w") as f:
        f.write(content)
        

def get_csv(filename):
    x_list = []
    y_list = []

    with open(filename) as f:
        content = f.readlines()

    for each_line in content:
        templist = each_line.split(",")
        try:
            x_list.append(float(templist[0]))
            y_list.append(float(templist[1]))
        except:
            pass

    return x_list, y_list