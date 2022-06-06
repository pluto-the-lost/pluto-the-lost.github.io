# 生成定制细胞

在decoder生成还原数据时，改变隐层的维度，会的得到不一样的输出。

这里做了几个生成实验，分别测试了改变organ, trajectory, functional score的影响

提到的数据集：

* EC: 小鼠内皮细胞图谱数据，选了其中的4个器官
* HCC: 肝细胞性肝癌
* hECA_lung: hECA的肺部数据
* hECA_AUC: hECA随机选取5万个细胞的子集，同时标注了30个gene sets的富集分数，标记方法见[AUC富集通路](./subpages/AUC_enrichment/AUC_enrichment.html)

## EC

来自四个器官的小鼠内皮数据，已经被标记上动脉-毛细-静脉trajectory。两次实验分别改变了器官和trajectory pseudotime。结果是将细胞设置为哪个器官，生成的细胞就会更像那个器官的数据。trajectory改变时也会在umap上看到明显的数据流动

[generation_EC.html](./file/generation_EC/generation_EC.html)

## HCC

在肝癌数据上生成细胞，将这些细胞当成真细胞的原始数据，做标准的scanpy分析流程，画出umap。生成数据的umap图看着还不错。

然后生成细胞时，将部分原本是其它细胞类型的细胞设置细胞类型为T细胞或fibroblast（CAF），然后发现设定细胞类型的细胞会和其被设定类型的细胞聚在一起，而且同样表达该类型的marker genes，对T细胞来说是CD3E，对fibroblast来说是COL1A1。

[generation_liverCancer.html](./file/generation_liverCancer/generation_liverCancer.html)

## hECA lung

在hECA肺数据集上主要设置了seq_tech，以证明即使是来自不同测序平台的数据，通过设置隐层的方式也可以让输出数据融合在一起，而且不至于过分损失细胞类型分类能力

[generation_hECA_lung.html](./file/generation_hECA_lung-Copy1/generation_hECA_lung-Copy1.html)

## hECA_AUC

30个重点通路的AUCell score作为隐层，通过逐个改变每个通路的值生成细胞，这个实验的notebook文件特别大，始终下载不了……但是总之结论是虽然30个通路的score都学习得很准，但仅有2个通路的score改变后看到了明显的生成细胞变化