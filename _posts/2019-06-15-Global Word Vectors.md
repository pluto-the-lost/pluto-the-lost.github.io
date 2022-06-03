---
title: 词向量模型
date: 2019-06-15 12:00:00 +0800
categories: blogs
tags: [representation-learning, NLP, machine-learning, matrix-decomposition]
---



# Global Word Vectors

These series of methods, including **LSA, PLSA, LDA and GloVe**, are based on statisticscalled **topic models**. They are not specifically designed for word representation, however, LSA, PLSA and GloVe do obtain word vectors during the training.

<!-- more -->

- Technically, differ from Word2vec-like methods that "learn" word representation using training corpus, topic models get representationlearn them through a **[matrix decomposition](to.be.continue)** way. There are mainly two kinds of matrices to be decomposed:
    
    - Word-document matrix: rows for words or terms, columns for different documents in the corpus, $W_{ij}$ stand for how many times the word $i$ appears in the document $j$. LSA uses this strategy
    - Word-word matrix: rows and columns both represent terms, numbers coorespond to the number of times a given word occurs in the context of another given word, HAL utilizes matrices like this
    - Basically, any matrix decomposition method can be applied to both these two kind of matrices, so we mainly focus on decomposition methods

## **[Matirx decomposition](to.be.continue)




## Latent semantic analysis ([LSA](http://www.cs.bham.ac.uk/~pxt/IDA/lsa_ind.pdf))**: 

Also called Latent semantic index (LSI). LSA uses a SVD method to decompose a word-document matrix. 

- Why word-document matrix: 
    - The original goal of LSA is to build a query of documentation while take **synonym** into consideration
$$$$
- Why do matrix decomposition
    - if we just use bag-of-words to represent a document, some sentences with same meaning but different expression will not be found
    - assuming that words with similar meaning are more likely to appear in one document
    - SVD can achive denoising to documents and find latent semantic structure
$$$$
- **Why LSA is also a representation of word**
    - when doing SVD, a word-document $X_{m\times n}$ is decomposed to three distinct matrices:
        - $X_{m\times n}=T_{m\times r}S_{r\times r}D_{r\times n}$ , where $r$ is a hyperparameter
        - if combining $S$ and $D$, we will have a $r\times n$ matrix, it is a continuous representation of documents, where each column is a document
        - meanwhile, $T_{m\times r}$ is a continuous representation of words, where each row is a word

## PLSA, LDA
These two method bring "topic" into their models, so they are also called "topic models". Basically they assume that documents will have one or more topics, and under different topic will yield different probability of words appearance. 

Since they do not obtain a word representation, so we are not discussing them thoroughly. You can study them [here](https://blog.csdn.net/lmm6895071/article/details/74999129).

**[PLSA](https://blog.csdn.net/thriving_fcl/article/details/50878845)** believes that **each document $d$ has a topic $z$**, which is unobservable but can be discribed as $p(z|d)$. Different topic correspoding to different probability distribution of words $p(w|z)$. The problem to be solve is
$$
\arg \max _{\theta} Q(\theta)=\arg \max _{\theta} \sum_{d} \sum_{w} n(d, w) \sum_{z} p(z | d, w) \operatorname{logp}(w | z) P(z | d)
$$
, where $\theta$ is parameters to be estimated, including parameters in $p(z|d)$ and in $p(w|z)$. Considering $z$ is a latent variable, if $z$ is known, $\log \sum_{z} p(w | z) p(z | d)$ becomes $\log \prod_{z} p(w|z)^{I(z=z_d)}=\sum_z I(z=z_d)\log p(w|z)$. MLE is easier to achieve under this situation. **[EM algorithm](to.be.continue)** can be applied to solve this problem.

**[LDA](https://en.wikipedia.org/wiki/Latent_Dirichlet_allocation)** makes another assumption that each word in a document is sampled under different topic. In other words, there is a **latent topic assignment matrix $Z_{M\times N}$**, where $M$ is the number of documents and N is the number of words in each document (without loss of generality, let they have the same length). The probability model for LDA is 
$$
P(\boldsymbol{W}, \boldsymbol{Z}, \boldsymbol{\theta}, \boldsymbol{\varphi} ; \boldsymbol{\alpha}, \beta)=\prod_{i=1}^{K} P\left(\varphi_{i} ; \beta\right) \prod_{j=1}^{M} P\left(\theta_{j} ; \alpha\right) \prod_{t=1}^{N} P\left(Z_{j, t} | \theta_{j}\right) P\left(W_{j, t} | \varphi_{Z_{j t}}\right)
$$
the meaning of symbols in the equation:
- $\boldsymbol{W}_{M\times N}$: the corpus matrix, word identity for word $n$ in document $m$
- $\boldsymbol{Z}_{M\times N}$: latent topic assignment matrix, topic identity for topic $n$ in document $m$
- $\boldsymbol{\theta}_{M\times K}$: posterior probability for document $m$ to have topic $k$, **document representation**
- $\boldsymbol{\psi}_{K\times V}$: posterior probability for topic $k$ to generate word $v$, **word representation**
- $\alpha_{[K]}$: prior probability of topicx, paramters for a Dirichlet distribution
- $\beta_{[V]}$: prior probability of words, paramters for another Dirichlet distribution

**Collapsed Gibbs sampling** is used to solve this problem by sampling $\boldsymbol{Z}|\boldsymbol{W};\alpha,\beta$. When $\boldsymbol{Z}$ is clear, it will be easy to calculate $\boldsymbol{\theta}$ and $\boldsymbol{\psi}$.

## **Global Vectors for Word Representation ([GloVe](https://www.aclweb.org/anthology/D14-1162))**

The work was published in 2014 by Google. Briefly, it decomposes a  **weighted log-word-word co-occurrence matrix**. More specifically, it minimize a cost function
$$
J=\sum_{i, j=1}^{V} f\left(X_{i j}\right)\left(w_{i}^{T} \tilde{w}_{j}+b_{i}+\tilde{b}_{j}-\log X_{i j}\right)^2
$$
where the symbols are:
- $X$: word-word co-occurrence matrix
- $w_{i}$: distributed representation for the $i_{th}$ word, calculated through $X$
- $\tilde{w}_{j}$: distributed representation for the $j_{th}$ word, calculated through $X^T$, also called "separate context word vectors"
- $b_i$, $\tilde{b}_j$: bias specific for word $i$ or $j$

The derivation of this model start from an assumption, that a "probe" word $k$ can be a bridge to compare two words $i$ and $j$. 
    
- There are two words of interest, say $i$ and $j$, and a probe word $k$. If $k$ is closer to $i$ than to $j$, it will appear more frequently in $i$'s context than in $j$'s context, and we will see $P_{ik}/P_{jk}\gt 1$
- Similarly, if $k$ is more similar to $j$, $P_{ik}/P_{jk}\lt 1$. If equally similar or dissimilar, $P_{ik}/P_{jk}\approx 1$
- Our word embedding should keep this feature:
    - $F\left(w_{i}, w_{j}, \tilde{w}_{k}\right)=\frac{P_{i k}}{P_{j k}}$
- The **embedding space should be linear**, so the similarity is function of difference:
    - $F\left(w_{i}-w_{j}, \tilde{w}_{k}\right)=\frac{P_{i k}}{P_{j k}}$
- Also for **linearity**, the argument of $F$ should be a scalar:
    - $F\left(\left(w_{i}-w_{j}\right)^{T} \tilde{w}_{k}\right)=\frac{P_{i k}}{P_{j k}}$
- There are still many possible $F$, we want it to be **homomorphism**, which means $f(x \cdot y)=f(x) \cdot f(y)$:
    - $F\left(\left(w_{i}-w_{j}\right)^{T} \tilde{w}_{k}\right)=\frac{F\left(w_{i}^{T} \tilde{w}_{k}\right)}{F\left(w_{j}^{T} \tilde{w}_{k}\right)}$
- Obviously, $F=exp$ is a good solution
    - $F(w_i^T\tilde{w}_{k})=\exp{w_i^T\tilde{w}_{k}}=P_{i k}=\frac{X_{i k}}{X_{i}}$
    - $w_{i}^{T} \tilde{w}_{k}=\log \left(P_{i k}\right)=\log \left(X_{i k}\right)-\log \left(X_{i}\right)$
- Since $\log{X_i}$ is not relevant to $k$, we can regard it as a const, also with a const only correlated to $i$ to restore the **symmetry**:
    - $w_{i}^{T} \tilde{w}_{k}+b_{i}+\tilde{b}_{k}=\log \left(X_{i k}\right)$
- This is really close, however, the author thought that not all co-occurence pairs are equally important. **Those rare pairs are more likely to bring noise and carry less information**, while rare pairs occupy 75%~90% of the co-occurance matrix. Then a weight is brought in and this is the final **cost function**:
    - $J=\sum_{i, j=1}^{V} f\left(X_{i j}\right)\left(w_{i}^{T} \tilde{w}_{j}+b_{i}+\tilde{b}_{j}-\log X_{i j}\right)^{2}$
- Where weighting function $f(X_{ij})$ should satisfy three condition:
    - $f(0)=0$
    - $\lim_{x->0} f(x)\log{x}=0$
    - $f(x)$ should be relatively small when $x$ is large
- After trying many functions, the author decided to use:
$$
f(x)=\left\{\begin{array}{cc}{\left(x / x_{\max }\right)^{0.75}} & {\text { if } x<x_{\max }} \\ {1} & {\text { otherwise }}\end{array}\right.
$$

This is how the authors constructed the cost function and what assumption did they make during the derivation of the function.
