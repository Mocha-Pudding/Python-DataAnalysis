# :cactus:Python-DataAnalysis
</br>
<h1 align="center">:whale:Python数据分析学习记录:whale:</h></br>
</br>
<p align="center">🍭🍭🍭👋👋👋</p>

> <h5>生命苦短，我用Python！</h5>
> <h5>Python Data Analysis Demos.</h5>

## 简易结构
学习路线
```
├─── CLASSDATA_Chapter00基础语言
│    └── CLASSDATA_Chapter00基础语言练习
│         ├── .ipynb_checkpoints
│         ├── CLASSDATA_Chapter00基础语言练习.ipynb
│         └── 参考代码
│               ├── .ipynb_checkpoints
│               ├── CH06函数.ipynb
│               ├── CH07模块与包.ipynb
│               ├── CH08数据读写.ipynb
│               ├── 项目01商铺数据加载及存储.ipynb
│               └── 项目02基于Python的算法函数创建
│     
├─── CLASSDATA_Chapter01重点工具：数据解析
│    ├── CH01科学计算工具：Numpy
│    │    ├── .ipynb_checkpoints
│    │    ├── 【个人笔记】CH01科学计算工具：Numpy.ipynb
│    │    └── 参考代码
│    │          ├──  .ipynb_checkpoints
│    │          ├──  CH01科学计算工具：Numpy.ipynb
│    │          └──  CH01科学计算工具：Numpy_课程作业答案.ipynb
│    │
│    ├── CH02数据分析工具：Pandas
│    │    ├── .ipynb_checkpoints
│    │    ├── 【个人笔记】CH02数据分析工具：Pandas_Part01.ipynb
│    │    ├── 【个人笔记】CH02数据分析工具：Pandas_课程作业.ipynb
│    │    └── 参考代码
│    │          ├──  .ipynb_checkpoints
│    │          ├──  CH02数据分析工具：Pandas__Part01.ipynb
│    │          ├──  CH02数据分析工具：Pandas__Part02.ipynb
│    │          ├──  CH02数据分析工具：Pandas__Part03.ipynb
│    │          └──  CH02数据分析工具：Pandas_课程作业答案.ipynb
│    │
│    ├── CH03图标绘制工具：Matplotlib
│    │    ├── CH03图表绘制工具：Matplotlib__Part01.ipynb
│    │    ├── CH03图表绘制工具：Matplotlib__Part02.ipynb
│    │    └── CH03图表绘制工具：Matplotlib__Part03.ipynb
│    │
│    ├── CH04空间分析工具：GIS
│    │    ├── 
│    │    └── 
│    │
│    └── END 
│
├─── CLASSDATA_Chapter02进阶算法学习：统计分析
│    ├── CH01
│    │    ├── 
│    │    └── 
│    │
│    ├── CH02
│    │    ├── 
│    │    └── 
│    │
│    ├── CH03
│    │    ├── 
│    │    └── 
│    │
│    └── END  
│
├─── CLASSDATA_Chapter03数据表大逻辑：结果输出与美化
│    ├── CH01
│    │    ├── 
│    │    └── 
│    │
│    ├── CH02
│    │    ├── 
│    │    └── 
│    │
│    ├── CH03
│    │    ├── 
│    │    └── 
│    │
│    ├── CH04
│    │    ├── 
│    │    └── 
│    │
│    └── END 
│
├─── Demo_BecomeALeader 
│    ├── 数据分析Demo-成为领导人的秘诀
│    │    ├── .ipynb_checkpoints
│    │    ├── 数据资料
│    │    ├── matplotlib颜色表lFZum.png
│    │    ├── matplotlib颜色表lnCk6u.jpg
│    │    ├── .ipynb_checkpoints
│    │    └── 【个人笔记】F02_案例一_成为领导的秘诀.ipynb
│    │
│    └── END 
│
├─── Matplotlib 
│    ├── 利用Matplotlib绘制图形
│    │    ├── Sandian_demo
│    │    │    ├── 01.csv
│    │    │    ├── matplotlib_test.ipynb
│    │    │    └── sandian.py
│    │    ├── 
│    │    │
│    │    ├── 
│    │    │
│    │    ├── 
│    │    │
│    │    └──
│    │
│    └── END 
│
├─── Python数据分析精英训练营(系列) 
│    ├── 三个案例来了解数据分析基本流程和步骤，熟悉真实应用场景
│    │    ├── 课件 6.12 - 小试牛刀——足球运动员分析
│    │    │    ├── 牛刀小试——足球运动员分析.ipynb
│    │    │    └── 
│    │    ├── 课件 6.13 - 循序渐进——AQI分析与预测
│    │    │    ├── 循序渐进——AQI分析与预测.ipynb
│    │    │    └── 
│    │    └── 课件 6.14 - 登堂入室——文本分析实现新闻推荐
│    │         ├── 登堂入室——文本分析实现新闻推荐.ipynb
│    │         └── 
│    │
│    └── END 
│
├─── Python数据分析职业发展路线.jpg
│
├─── .gitattributes
│
├─── README.md
│
└─── END
```

补充说明：</br>
1.关于matplotlib颜色表</br>
可参照网站：https://stackoverflow.com/questions/22408237/named-colors-in-matplotlib
</br>
</br>
2.关于matplotlib中文问题</br>
方法一：</br>
（平台：windows,python3.5）</br>
1）：打开设置文件，输入以下代码会显示matplotlibrc文件的地址</br>
import matplotlib </br>
matplotlib.matplotlib_fname() </br>
2）：修改matplotlibrc文件</br>
将文件中的#font.family: sans-serif去掉注释，修改为font.family: Microsoft YaHei </br>
3）：重启jupyter notebook可显示为中文</br>
</br>
方法二：加上两行代码</br>
plt.rcParams['font.sans-serif']=['SimHei'] </br>
plt.rcParams['axes.unicode_minus']=False </br>



