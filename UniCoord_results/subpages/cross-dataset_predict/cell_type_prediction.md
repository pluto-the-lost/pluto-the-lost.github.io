---
html:
    toc: true
---

# 跨数据集的细胞类型预测
这部分是用一些数据集来训练UniCoord模型，再在其它数据集上做预测，来验证UniCoord的泛化性。

提到的几个数据集:

* hECA_2000: hECA中每个celltype选出2000个细胞组成的数据集
* hECA_lung: hECA的肺部数据
* HCC: 肝细胞性肝癌
* LUAD: 肺腺癌
* TBMU: Tabula Muris
* TBSP: Tabula Sapiens

训练方法：从训练集中取80%的数据作为训练集，剩下20%作为测试集，用训练集训练10-100个epoch（每次试验不完全一样）。然后在测试集上测试准确率、证明训练有效后，到其它数据集上预测细胞类型。

跨数据集计算正确率时，由于各个数据集的标注体系不一样，我是将细胞类型归为几个大类，再比较大类的正确率。

## hECA_2000 

以hECA_2000作为训练集，预测了LUAD数据和hECA_lung，计算了confusion matrix和正确率

[20220303_anndata_hECA.html](./file/20220303_anndata_hECA/20220303_anndata_hECA.html)

## LUAD

以LUAD为训练集，预测hECA_lung和HCC，并计算了正确率

[20220303_anndata_LUAD.html](./file/20220303_anndata_LUAD/20220303_anndata_LUAD.html)

## HCC

以HCC为训练集，预测hECA_lung和LUAD

[20220303_anndata_HCC.html](./file/20220303_anndata_HCC/20220303_anndata_HCC.html)

