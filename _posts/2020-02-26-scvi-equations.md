---
title: scVI equations
date: 2020-02-26 12:00:00 +0800
categories: blogs
tags: [single-cell, machine-learning]
---

# scvi equations

<!-- more -->

---
# the scVI generative model

$$
\begin{aligned}
&w_{n g} \sim \operatorname{Gamma}\left(\rho_{n}^{g}, \theta\right)\\
&y_{n g} \sim \operatorname{Poisson}\left(\ell_{n} w_{n g}\right)\\
&h_{n g} \sim \text { Bernoulli }\left(f_{h}^{g}\left(z_{n}, s_{n}\right)\right)\\
&x_{n g}=\left\{\begin{array}{l}
{y_{n g} \text { if } h_{n g}=0} \\
{0 \text { otherwise }}
\end{array}\right.
\end{aligned}
$$

# derivation of ELBO
### 1. 
$$
\begin{align}
\log P_\theta(x) =& \log P_\theta(x)\int q_\phi(x|z)dz \\
=& E_{q_\phi(z|x)}\log P_\theta(x)
\end{align}
$$
because the integration is not related with x
### 2. 
$$
\begin{align}
\log P_\theta(x)=&\log \frac{P_\theta(x,z)}{P_\theta(z|x)}\\
=&\log \frac{P_\theta(x,z)}{q_\phi(z|x)}\frac{q_\phi(z|x)}{P_\theta(z|x)}\\
=&\log P_\theta(x|z)-\log \frac{q_\phi(z|x)}{P_\theta(z)} + \log \frac{q_\phi(z|x)}{P_\theta(z|x)}
\end{align}
$$
### 3. 
if we combine the 2 above equations:
$$
\begin{align}
\log P_\theta(x) =& E_q\log P_\theta(x|z) - D_{KL}(q_\phi(z|x)||P_\theta(z)) + D_{KL}(q_\phi(z|x)||P_\theta(z|x))\\\\
\log P_\theta(x) \geq& E_q\log P_\theta(x|z) - D_{KL}(q_\phi(z|x)||P_\theta(z))
\end{align}
$$

## 4. meanfield assumption
$$
D_{KL}(q_\phi(z,l|x,s)||P_\theta(z,l)) = D_{KL}(q_\phi(z|x,s)||P_\theta(z))+D_{KL}(q_\phi(l|x,s)||P_\theta(l))
$$



