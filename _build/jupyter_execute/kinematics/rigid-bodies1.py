#!/usr/bin/env python
# coding: utf-8

# ## Classification of Rigid Body Motion
# 
# ```{figure} ./images/14.png
# ---
# name: 14
# ---
# ```
# 
# Translation: the motion of $B$ in $A$ is a translation if and only if any straight line segment embedded in $B$ remains parallel to itself when observed from $A$ when $B$ moves in $A$. If this condition is not met, then we have to consider the motion as rotation.
# 
# Simple rotation: the motion of $B$ in $A$ is a simple rotation if and only if there exists a unit vector $\hat{n}$ that remains fined in both $B$ and $A$, as $B$ moves in $A$. Examples in figures below:
# 
# ```{figure} ./images/15.png
# ---
# name: 15
# ---
# ```
# 
# Coming back to our old example of a door hinged to a wall.
# 
# ```{figure} ./images/16.png
# ---
# name: 16
# ---
# ```
# 
# Here, $\hat{b}_y$ is a unit vector that is fixed in both $B$ and $A$. Using our definition for simple rotation tells us that $\hat{b}_y$ is $\hat{n}$. So, in mathematical notation, we can say:
# 
# ```{figure} ./images/17.png
# ---
# name: 17
# ---
# ```
# 
# But we must now pause to ask ourselves if there is any other unit vector that is also fixed in both $B$ and $A$? It turns out that there is, indeed, another one fixed in both $B$ and $A$: $\hat{a}$.
# 
# So we can now also write:
# 
# ```{figure} ./images/18.png
# ---
# name: 18
# ---
# ```
# 
# So, from $2$ and $3$, we get:
# 
# ```{figure} ./images/19.png
# ---
# name: 19
# ---
# ```
# 
# :::{admonition} Why is establishing $4$ useful and critical?
# :class: tip, dropdown
# So far, we have written the vectors $\vec{v}$ and $\vec{e}$, in terms of the $B$ frame. As a result, they were not functions of $\theta$.
# 
# Expressing the vectors in the unit vectors attached to the A frame requires us to derive relationships between $\hat{a}_i$ and  $\hat{b}_i$:
# 
# $$
# <i = x,y,z>
# $$
# 
# $4$ allows us to derive a relationship between $\hat{a}_i$ and $\hat{b}_i$, which then provides a basis for developing the rigid body kinematics.
# :::
# 
# Let us explore how to derive these relationships for the vectors $\vec{e}$ and $\vec{v}$ in the doorwall example (figure is shown again below):
# 
# ```{figure} ./images/16.png
# ---
# name: 16
# ---
# ```
# 
# From the second of Equations in $1$, we have $\vec{e} = -e\hat{b}_y$.
# 
# From $4$ we also get $\vec{e} = -e\hat{a}_y \:\:\:(5)$
# 
# 
# $\theta $in the prior example is an angle that describes the orientation of $B$ relative to $A$ (and vice versa). Thus, it is also called an angular position. Other common ways of referring to it are _orientation angle_ or _attitude angle_.
# 
# 
# Now, we come to a more involved example, where we will express $\vec{v}$ in terms of the unit vectors of the $A$ frame using the first of Equations $1$ as the starting point:
# 
# $$
# \vec{v} = v\hat{b}_x
# $$
# 
# We can now examine the relationships between the unit vectors by drawing only the unit vectors with the vector $\hat{n}$ out of the plane (see figure below this passage). We can then derive the following relationships by examining the lower figure,  comprising only unit vectors:
# 
# ```{figure} ./images/20.png
# ---
# name: 20
# ---
# ```
# 
# ```{figure} ./images/21.png
# ---
# name: 21
# ---
# ```
# 
# Therefore from $6$:
# 
# $$
# \vec{v} = v(\cos{\theta}\hat{a}_x + \sin{\theta}\hat{a}_z)
# $$
# 
# Also from $5$, we have: $\hat{b}_y=\hat{a}_y$
# 
# Now, we have derived the complete relationships between the unit vectors that make up the $B$ frame in terms of the unit vectors of the $A$ frame.
# 
# We can take this work one step further and write the relationships in matrix form as follows:
# 
# ```{figure} ./images/22.png
# ---
# name: 22
# ---
# ```
# 
# Let’s focus on the second row of the above matrix equation (this is highlighted in yellow below):
# 
# ```{figure} ./images/23.png
# ---
# name: 23
# ---
# ```
# 
# This tells us that: $\hat{b}_y=\hat{a}_y$
# 
# Visually, this can be interpreted to mean that the door B swings relative to the wall $A$ about the $\hat{b}_y$-axis, which also coincides with the $\hat{a}_y$-axis. In other words, this represents what is know a simple rotation about the $y$-axis. Similar relationships can also be derived for simple rotations about $x$-axis or $z$-axis. 

# ### Direction Cosine Matrix (DCM)

# ```{figure} ./images/24.png
# ---
# name: 24
# ---
# ```
# 
# Continuing with the matrix representation of the door-wall example, the $3\times3$ matrix (highlighted in green above) relates the $B$-frame’s unit vectors to the $A$-frame’s unit vectors. It is called the direction $\text{cosine}$ matrix of $A$ in $B$. The symbolic notation of it is ${}^{B}C^{A}$. This is for a rotation about $y$-axis, as mentioned on the previous page.
# 
# Simple notations about $z$-axis would result in the following DCM.
# 
# ```{figure} ./images/26.png
# ---
# name: 26
# ---
# ```
# 
# Simple notations about $x$-axis would result in the following DCM:
# 
# **Why does the term DCM have $\text{cosine}$ in it?**
# 
# Return to Equations $6$ and $7$, you can observe that they were derived purely using the $\text{cosine}$ of angles between different unit vectors. For example, consider the $x$-unit vector of the $B$-frame as represented in the $A$-frame:
# 
# $$
# \hat{b}_x = \cos{\theta}\hat{a}_x + \cos{(90-0)}\hat{a}_z
# $$
# 
# which then becomes
# 
# $$
# \hat{b}_x = \cos{\theta}\hat{a}_x + \sin{\theta}\hat{a}_z
# $$
# 
# This can be written in a more generic form using only dot products (as this product is defined using $\text{cosine}$ terms), as shown below:
# 
# $$
# \hat{b}_x = (\hat{b}_x\cdot{}\hat{a}_x)\hat{a}_x + (\hat{b}_x\cdot{}\hat{a}_y)\hat{a}_y + (\hat{b}_x\cdot{}\hat{a}_z)\hat{a}_z
# $$
# 
# where,
# 
# $$
# \hat{b}_x\cdot{}\hat{a}_y \Longrightarrow \cos{90^{\circ}} = 0
# $$
# 
# This serves as the foundation for a more general description of orientations for **General $3D$ Rotation**.

# ### General $3D$ Rotation and DCM

# Below, body $B$ is moving freely relative To frame $A$:
# 
# ```{figure} ./images/27.png
# ---
# name: 27
# ---
# ```
# 
# From the preceding discussion on dot products and DCM, we can write the following relationships between two reference frame $A$ and $B$.
# 
# ```{figure} ./images/28.png
# ---
# name: 28
# ---
# ```
# 
# $11$ can then also be written in the matrix form as shown below:
# 
# ```{figure} ./images/29.png
# ---
# name: 29
# ---
# ```
# 
# which can also be written more succinctly as:
# 
# ```{figure} ./images/30.png
# ---
# name: 30
# ---
# ```
# 
# ${}^{B}C^{A}$ is the direction $\text{cosine}$ matrix of $B$ and $A$.
# 
# :::{note}
# ${}^{A}C^{B} \neq {}^{B}C^{A}$
# ::: 
# 
# #### A key property of DCM
# 
# A very important property of DCM is that it is an orthogonal matrix. Mathematically, this means that the inverse of the DCM is the same as the transpose of the matrix. In other words, if the DCM is given by a matrix $M$, then:
# 
# ```{figure} ./images/31.png
# ---
# name: 31
# ---
# ```
# 
# This is a very useful result because it is considerably easier to compute the transpose of a matrix than it is to compute its inverse.
# 
# **How is this property useful?**:
# 
# At this point, we two that we can express the same vector in different reference frames. This property allows us to do so in a very easy manner. Below we show how you can easily convert (or express) a vector given in the $B$-frame to its equivalent in the $A$-frame.
# 
# ```{figure} ./images/32.png
# ---
# name: 32
# ---
# ```
# 
# In fact, when one compares $15$ to $8a$ one sees that:
# 
# $$
# {}^{B}C^{A} = {\left({}^{B}C^{A}\right)}^T
# $$
