---
title: 基于表的强化学习
date: 2019-09-16 12:00:00 +0800
categories: blogs
tags: [reinforcement-learning, machine-learning]
---


当一个强化学习问题里的状态数和动作数都相对比较小，状态-动作关系就可以**写成一个表** (table, array or tabular)，表的数值对应的是在某个状态&动作下的**价值函数** (value function)。这种情况下通常我们可以找到**精确解**，即**可以精确得到一个最优的价值，及其对应的最优策略**。与之相对的，如果状态或动作空间太大，就只能用求出**估计解**(approximate solutions)，可能是局部最优，或者最终的价值只是一个估计值。复杂的问题更广泛一些，但是这个页面我们先看看能精确求解的简单问题。

<!-- more -->

**文章大概分为三部分**：

- [第一部分](https://www.zybuluo.com/pluto-the-lost/note/1510806)介绍一个最简单的情况，即只有一种状态，这个问题叫做**多臂赌博机**(Multi-armed Bandits)问题
- 第二部分介绍强化学习的理论框架——**有限马尔可夫决策过程**(finite Markov Decision Process, MDP)，以及三种求解MDP的基本方法——**动态规划(dynaminc programming, DP)，蒙特卡洛方法(Monte Carlo method, MC)，时序差分方法(temporal difference, TD)**。
- 第三部分是上面三种方法的**复杂应用**，基本是TD和其他两者的混合使用

