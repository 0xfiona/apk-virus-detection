## 基于clamav和随机森林的安卓恶意代码检测器

#### 运行步骤

+ 使用随机森林训练器训练出一个model
+ 在分类api中调用model可以对apk文件进行检测
+ 安装clamav和clamtk后使用本项目中对应的文件`scanners.c`和`GUI.pm`进行替换



#### 检测原理

最终实现结果和原理见报告`report.pdf`


