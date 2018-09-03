# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
from mpl_toolkits.mplot3d import Axes3D
import os

def get_sim_name_array(text_path):
    name_array = []
    result_dict = defaultdict(list)
    
    try:
        f = open(text_path, "r")
        all_data = f.readlines()
        for i, line in enumerate(all_data):
            if not line.split('\t')[1] in name_array:
                name_array.append(line.split('\t')[1])
        print("The length of " + text_path + " is: ", i)
        for line in all_data:
            for name in name_array:
                if line.split('\t')[1] == name:
                    result_dict[name].append(float(line.split('\t')[2].split('\n')[0]))
        f.close()
    except:
        print("Unalbe to read txt file, check txt file and execute again.")
        
    return name_array,result_dict

def get_every_sim_sum(result_dict):
   
    len_array = []
    sub_len_array = np.zeros(11)
    
    for index,name in enumerate(result_dict):
        for sim in result_dict[name]:
            for ind,i in enumerate(np.linspace(0.3,0.4,11)):
                if sim >i:
                    sub_len_array[ind] += 1
        len_array.append(sub_len_array)
        #print(sub_len_array)
        sub_len_array = np.zeros(11)
    return len_array

def draw(x,y,z):
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap='rainbow')
    ax.set_xlabel('name')
    ax.set_ylabel('sim')
    ax.set_zlabel('number of every sim and name')
    #plt.show()
    plt.savefig('1.jpg',dpi=120)

   

if __name__ == '__main__':
    text_path = 'all_result.txt'
    name_array,result_dict = get_sim_name_array(text_path)
    name_array_number = []
    
    
    len_array = get_every_sim_sum(result_dict)   
    print('this is len_array:',len_array)
    
    sim_array = np.linspace(0.3,0.4,11)  
    for i, name in enumerate(name_array):
        name_array_number.append(i)

    
    name_array_number, sim_array = np.meshgrid(name_array_number, sim_array)
             
    draw(name_array_number,sim_array,np.transpose(np.array(len_array)))
    
    

    
