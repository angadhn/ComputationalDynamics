#!/usr/bin/env python
# coding: utf-8

# # Key Theorems for computing $\left[I\right]^{S/O}$

# There are three useful theorems to compute moments of inertia. They are:
# 
# 1. __Rotation theorem__
# 2. __Parallel axis theorem__ (or translation theorem)
# 3. __Composite theorem__
# 
# Let us examine them in further detail.

# ## Rotation theorem

# ```{figure} ./images/26.png
# ---
# name: 26
# ---
# ```
# 
# - $X-Y-Z$ make up a cartesian coordinate system. 
# - $O$ is the origin.
# - $\hat{n}_x,\;\hat{n}_y,\;\hat{n}_z$ are unit vectors directed along $X-Y-Z$ respectively. The unit vectos represent a reference frame $N$.
# 
# Also, the figure shows a rocket which has a reference frame $R$ attached to it. You are given the inertia matrix of the rocket $R$ about $O$ along the unit vectors of frame $N$. Naturally, this reference frame also has $3$ mutually orthogonal unit vectors: 
# 
# $$
# \hat{r}_x \qquad \hat{r}_y \qquad \hat{r}_z
# $$
# 
# ```{figure} ./images/27.png
# ---
# name: 27
# ---
# ```
# 
# Now, we can define another inertia matrix for $R$ about $O$ along the newly introduced rotating reference frame's unit vectors $\hat{r}_x, \; \hat{r}_y, \; \hat{r}_z$. This matrix and its elements are:
# 
# ```{figure} ./images/28.png
# ---
# name: 28
# ---
# ```
# 
# :::{admonition} Question: How are the two matrices related?
# :class: tip, dropdown
# 
# We begin by assuming that $R$ is a particle of mass, $m_R$.
#     
# Let us consider a product of inertia from each matrix.
# 
# ```{figure} ./images/29.png
# ---
# name: 29
# ---
# ```
# 
# $P^*$ is a position vector from $O$ to the origin of the frame $R$.
# 
# We know from our discussion on direction $\text{cosine}$ matrices that the unit vectors of $R$ can be related to the unit vectors of $N$ as:
# 
# ```{figure} ./images/30.png
# ---
# name: 30
# ---
# ```
# 
# ${}^{R}C^{N}$ is the direction $\text{cosine}$ matrix of $R$ in $N$. It is a $3\times3$ matrix, which we shall assume has the following elements:
# 
# ```{figure} ./images/31.png
# ---
# name: 31
# ---
# ```
# 
# So, we can now easily derive:
# 
# ```{figure} ./images/32.png
# ---
# name: 32
# ---
# ```
# 
# And then, we can rewrite the product of inertia $J^{R/O}_{xy}$ as: 
# 
# ```{figure} ./images/33.png
# ---
# name: 33
# ---
# ```
# 
# This leads to
# 
# ```{figure} ./images/34.png
# ---
# name: 34
# ---
# ```
# 
# or in terms of matrix multiplication.
# 
# ```{figure} ./images/35.png
# ---
# name: 35
# ---
# ```
# 
# More generally, it can be shown that
# 
# ```{figure} ./images/36.png
# ---
# name: 36
# ---
# ```
# :::

# ## Parallel axes theorem

# 
# In the previoussection we presumed that the rocket was a point mass. What happens if this assumption is relaxed and rockets are better approximated as a system of particles?
# 
# - $P^*$ is a position vector from $O$ to $R^*$, the origin of the frame $R$.
# 
# - $R^*$ is he mass center of the rocket.
# 
# - $\vec{P}_i$ is a position vector from $O$ to $\vec{P}_i$, the $i^{\text{th}}$ particle on the rocket body.
# 
# - $r_i$ is a position vector from $R^*$ to $\vec{P}_i$. So,
# 
# $$
# \vec{P}_i = P^* + r_i 
# $$
# 
# ```{figure} ./images/37.png
# ---
# name: 37
# ---
# ```
# 
# Now, we know that the product of inertia for this system of particles along the $\hat{n}_x,\;\hat{n}_y,\;\hat{n}_z$ directions given by:
# 
# ```{figure} ./images/38.png
# ---
# name: 38
# ---
# ```
# 
# The terms highlighted in green go to zero because $\sum_im_ir_i = 0$ by the definition of mass centers.
# 
# ```{figure} ./images/39.png
# ---
# name: 39
# ---
# ```
# 
# $I^{R/R^*}_{xy}$ is the product of inertia of $R$ about the mass center $R^*$.
# 
# $I^{R^*/O}_{xy}$is the product of inertia of $R^*$ about $O$.
# 
# This result extrapolates to the moment of inertia scalars. For example,
# 
# ```{figure} ./images/40.png
# ---
# name: 40
# ---
# ```
# 
# This result extrapolates to the inertia matrix,
# 
# ```{figure} ./images/41.png
# ---
# name: 41
# ---
# ```
# 
# This rule is only valid when going through the mass center.

# ## Composite theorem

# ```{figure} ./images/42.png
# ---
# name: 42
# ---
# ```
