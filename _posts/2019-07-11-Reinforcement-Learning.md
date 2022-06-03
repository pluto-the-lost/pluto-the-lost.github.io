---
title: Reinforcement Learning
date: 2019-07-11 12:00:00 +0800
categories: blogs
tags: [reinforcement-learning, machine-learning]
---


The book *[Reinforcement Learning: An introduction](http://www.incompleteideas.net/book/the-book-2nd.html)* is written by Richard S. Sutton, firstly in 2015 and the second edition just came out in 2017. 

<!-- more -->

## 1. Definition & Problem

### 1.1 Definition

#### 1.1.1 Simply speaking
- Reinforcement learning is a kind of machine learning methods that are **goal-directed** and **learn from interaction**
- RL is about **how to map situations to actions** so as to maximize a **reward signal**

#### 1.1.2 Formulation (MDP)
- Markov Decision Process
- For most of RL cases, the states and actions spaces are finite, and the MDP is called finite MDP
- **to be continue**

### 1.2 Characteristics
- RL problems are:
    - **closed-loop**: the action is decided by input, then action will influence the next input
    - **no direct instruction**: the learner must try each policy to discover which yield the best reward
    - **delayed reward**: actions may affect not only the next reward but all the subsequent rewards
$$$$
- MDP suggests that the learning machine must:
    - be able to **sense the state**
    - be able to take actions that **affect the state**
    - have a goal or goals that **related to the state**
$$$$
- RL differs from:
    - supervised learning: in supervised learning, each sample (or called situation) is labeled by a specification - the label (or called the correct action), while in RL there **doesn't exist a "correct instruction of actions"**
    - unsupervised learning: RL does not learn **hidden structures** in unlabeled data
- These differences make RL a **third paradigm of machine learning**, instead part of supervised or unsupervised learning

### 1.3 Challenges and Pros

- trade-off between exploitation (already known, greedy) and exploration (unknown, global)
- consider the whole problem, instead split it apart and study subproblems

### 1.4 Examples

- A master chess
- An adaptive controller
- Learning how to run
- A robot decides whether to enter a room to collect trash
- Preparing for a breakfast

These cases share features that they contain **interaction** with theri environment, in order to achieve a **goal** despite **uncertainty** about the environment

### 1.5 Elements of RL

- **policy**: given the environment, what will the agent do
- **reward**: defines the goal. A status gives a number, and the total sum of rewards should be maximized
- **value function**: total sum of rewards, indicating the long term goodness
- **(optional)model of the environment**: infering how environment will behave

## 2. Methods
### 2.1 [Tabular Solution](https://www.zybuluo.com/pluto-the-lost/note/1507344)
Simplest forms of RL: the state and action spaces are small enough for the approximate value functions to be represented as a tabular (array).

- Dynamic Programming
- Monte Carlo methods
- Temporal-difference learning (TD)
- Ensemble of Above Three

### 2.2 Approximate Solution

- When the state or the action space is enormous, we cannot expect finding a optimal solution to the policy or value function. Instead, we find a good approximate solution