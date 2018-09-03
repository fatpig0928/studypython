import math
import matplotlib.pyplot as plt
import numpy as np

def sigmoid(x):
    output = []
    for i in x:
        output.append(1/(math.exp(-i)+1))
        
    return output

if __name__ =='__main__':
    '''类似与range()
    Args:
        -10.:起点
        10. :终点
        0.2 :间隔
    '''
    x = np.linspace(-1.00,1.00,100000000)
    #print(x)
    '''使用数据画图
    Args:
        x是横坐标的数据
        sigmoid(x)是纵坐标的参数
    '''
    plt.plot(x,sigmoid(x))
    processed_sigmoid = sigmoid(x)
    '''画网格
    Args:
        linestyle = '-.'表示用虚线画背景网格
        linewidth = 0.5 表示每条虚线的宽度,越大虚线越粗
    '''
    plt.grid(linestyle = '-.',linewidth = 0.5)
    #显示所画的图
    plt.show()