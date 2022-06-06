# 用非监督维度作为embedding

这块就是在监督某些batch维度的情况下，同时加上30维非监督连续维度，把这些维度拿出来，当成PCA用，做下面的UMAP、聚类等。但效果比较差，去batch的时候经常就把细胞类型信息去没了，就算没有去掉细胞类型信息，画出来的umap也非常奇怪。

提到的数据集

* hECA_lung: hECA的肺部数据
* HCC: 肝细胞性肝癌

## hECA_lung数据

[embedding_hECA_lung.html](./file/embedding_hECA_lung/embedding_hECA_lung.html)

## HCC数据

[embedding_LiverCancer.html](./file/embedding_LiverCancer/embedding_LiverCancer.html)

