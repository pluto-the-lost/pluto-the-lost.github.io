---
html:
    toc: true

title: UniCoord资料汇总
date: 2022-06-01 21:58:00 +0800
---

# UniCoord资料汇总


# 之前的biorxiv

word版本

[20210907\_UniCoordManu4bioRxiv.docx](file/20210907_UniCoordManu4bioRxiv_P1WRpJubt1.docx)

pdf版本

[2021.09.09.459281v1.full.pdf](file/2021.09.09.459281v1.full_pWOdADpEeV.pdf)

# 当前源代码

[Github链接](https://github.com/pluto-the-lost/unicoord "Github链接")

使用方法已经更新到Github首页下方的readme里

# 之前的演讲ppt

[20201022_组会1](./file/Building%20a%20Universal%20Coordinate%20Method%20for%20scRNA-seq%20Data.pptx)
[20210908_给Katy讲的](./file/20210908_UniCoord_pre.pptx)
[20220310_组会2](./file/Unicoord.pptx)

# 近期实验结果

## 跨数据集预测细胞类型

这里使用了四个单细胞数据集，分别是hECA的子集hECA_2000，hECA筛选出来的肺部细胞hECA_lung，肺腺癌的数据LUAD，肝细胞性肝癌的数据HCC。

预测的内容都是细胞类型，但几个数据集的细胞类型注释并不一致，所以计算正确率的时候都是把亚型归为几个粗的细胞类型。

详情见[预测细胞类型](./subpages/cross-dataset_predict/cell_type_prediction.html)

## 非监督的维度用作低维表示，同时去batch

这个功能的效果目前挺差的，所以在之前的talk里都没提过，但是实验做了一些。

详情见[非监督表示](./subpages/embedding/embedding.html)

## 生成数据，同时改变隐层维度

这块主要是做了一些动图，改变隐层时、输出会发生相应改变

详情见[生成定制细胞](./subpages/generate_cells/generate_cells.html)

## 选择一组enrichment score作为隐层

尝试了几种方法，从GOBP的几千个gene sets里选出30个能表示细胞的通路，计算了AUCell富集分数

详情见[AUC富集通路](./subpages/AUC_enrichment/AUC_enrichment.html)

## 做了三个预训练模型

分别用Tabula Muris, Tabula Sapiens, hECA三个数据集做了预训练模型，下载链接在[清华云盘](https://cloud.tsinghua.edu.cn/d/13021decce6c40ad9c4e/ "清华云盘")，

训练时的notebook如下
[pretrain_TBMU.html](./file/pretrain_TBMU/pretrain_TBMU.html)
[pretrain_TBSP.html](./file/pretrain_TBSP/pretrain_TBSP.html)
[pretrain_hECA_SeqtechAndCelltype.html](./file/pretrain_hECA_SeqtechAndCelltype/pretrain_hECA_SeqtechAndCelltype.html)