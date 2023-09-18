import matplotlib.pyplot as plt
import os
import numpy as np
import pandas as pd
from scipy.interpolate import CubicSpline

url = input('输入表格地址')
url = url[1:-1]

df = pd.read_excel(url)
index_x = input('x轴数据')
index_y = input('y轴数据')
x_data = df[index_x]
y_data = df[index_y]

cs = CubicSpline(x_data, y_data)

# 是否只描点不连线
answer = input('----------是否自己连线--------------\n 在这里输入y/n\t')
if answer == 'y':
    a = 0
else:
    a = 500
x_smooth = np.linspace(x_data.min(), x_data.max(), a)
y_smooth = cs(x_smooth)

# 画图
plt.figure(figsize=(8, 6))
plt.rcParams['font.sans-serif'] = ['SimHei', ]
plt.rcParams['axes.unicode_minus'] = False
plt.plot(x_smooth, y_smooth, markerfacecolor='none')
plt.scatter(x_data, y_data, marker='o', facecolor='none', edgecolor='blue')

# 设置x y轴名称
name_x = input('x轴名称')
name_y = input('y轴名称')
plt.xlabel(name_x)
plt.ylabel(name_y)

plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

name = input('折线图名称')
plt.title(name)
plt.grid(False)

# 保存到桌面
desktop_path = os.path.expanduser("~/Desktop")
name = name+'.jpg'
file_path = os.path.join(desktop_path, name)
plt.savefig(file_path)

plt.show()
