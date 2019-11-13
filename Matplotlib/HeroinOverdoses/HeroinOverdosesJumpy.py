# 使用Python生成动态图表
# 用到的数据是由美国疾控中心和药物滥用研究所收集的

# 除了用 Matplotlib 和 Seaborn 来作图我们还用到了 Numpy 和 Pandas 来处理数据。先把需要的库都 import 进来
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 把数据从下载的Excel文件读进来，我们用Pandas来读所以读进来就是一个DataFrame
# 还写了一个传入行数只读取一行数据的函数。这是为了以后给不同药物分别做图的时候读数据方便一些
overdoses = pd.read_excel('overdose_data_1999-2015.xls',sheet_name='Online',skiprows=6)
def get_data(table, rownum, title):
    data = pd.DataFrame(table.loc[rownum][2:]).astype(float)
    data.columns = {title}
    return data

# get_data 函数把因为海洛因死亡的人数读出来。这个 DataFrame 有两列，分别是年份和死亡人数
# 用 Jupyter Notebook的 话记得加图表页内显示的命令 %matplotlib notebook
# %matplotlib notebook
title = 'Heroin Overdoses'
d = get_data(overdoses, 18, title)
x = np.array(d.index)
y = np.array(d['Heroin Overdoses'])
overdose = pd.DataFrame(y,x)
XN, YN = augment(x, y, 10)
augmented = pd.DataFrame(YN, XN)
overdose.columns = {title}

# 初始化一个 ffmpeg 输出流。这里我设置帧率 20 码率 1800 ，当然你自己可以改帧率和码率。
Writer = animation.writers['ffmpeg']
writer = Writer(fps=20, metadata=dict(artist='Me'), bitrate=1800)

# 创建图表和横纵坐标。
# 这里要把数据范围定死不然数据更新的时候 Matplotlib 会自动更新数据范围我们的动图数据范围就会来回变
fig = plt.figure(figsize=(10,6))
plt.xlim(1999, 2016)
plt.ylim(np.min(overdose)[0], np.max(overdose)[0])
plt.xlabel('Year', fontsize=20)
plt.ylabel(title, fontsize=20)
plt.title('Heroin Overdoses per Year', fontsize=20)

# 绘图中最重要的就是下面这个 animate 函数，它的参数 i 指的是帧数
# 通过参数 i 来选择这一帧应该显示的数据然后用 Seaborn 来画一个折线图。
# 最后两行改改字体和折线的宽度让图好看一点
def animate(i):
    data = overdose.iloc[:int(i+1)]   # select data range
    p = sns.lineplot(x=data.index, y=data[title], data=data, color='r')
    p.tick_params(labelsize=17)
    plt.setp(p.lines, linewidth=7)

# 要让图表动起来我们得把刚才定义的 animate 函数传给 matplotlib.animation.FuncAnimation。
# 除了animate，FuncAnimation还有一个参数frames，这个参数的意思是说我们这段动画想一共要多少帧。
# 这里 frames 的值是 17 帧，所以 animate 函数会被调用17次。
ani = matplotlib.animation.FuncAnimation(fig, animate, frames=17, repeat=True)

# 给数据点中间插点值。插值可以用下面的 augment 函数
def augment(xold, yold, numsteps):
	xnew = []
	ynew = []
	for i in range(len(xold)-1):
		difX = xold[i+1]-xold[i]
		stepsX = difX/numsteps
		difY = yold[i+1]-yold[i]
		stepsY = difY/numsteps
		for s in range(numsteps):
			xnew = np.append(xnew, xold[i]+s*stepsX)
			ynew = np.append(ynew, yold[i]+s*stepsY)
	return xnew, ynew

# 给图片加点背景色
sns.set(rc={'axes.facecolor':'lightgrey', 'figure.facecolor':'grey', 
	'figure.edgecolor':'black','axes.grid':False})

# 先看看效果，可以用plt.show()
plt.show()

# 把这段动画存成 mp4 格式就行了
# ani.save('HeroinOverdosesJumpy.mp4', writer=writer)