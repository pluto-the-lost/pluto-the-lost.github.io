# 从GOBP中选出代表性通路

这里用的数据集是从hECA全集里随机采样的50000个细胞。目的是用这些细胞从GOBP通路中找到几十个最具有代表性的通路，作为细胞坐标的雏形。

首先将gene sets按照基因数量过滤，留下基因数在50-500之间的通路，这些通路全部算出AUCell富集分数后，用信息熵、logistic regression、随机森林等方法找到50个最有意义的通路，再通过通路之间的相关性进行去重，留下约30个相互之间较独立的通路。

[hECA_find_best_AUC.html](./file/hECA_find_best_AUC/hECA_find_best_AUC.html)

