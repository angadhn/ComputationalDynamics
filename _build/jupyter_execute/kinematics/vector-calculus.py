#!/usr/bin/env python
# coding: utf-8

# ## Vector Calculus

# Kinematics or Rigid body kinematics is the study of motion while ignoring the cause of motion.
# 
# In kinematics, we are interested in "position", "velocity", and “acceleration" and the relationship between them.
# 
# In other words, using the figure below, we are interested in describing the motion of $B$ in $A$.
# 
# ```{figure} ./images/13.png
# ---
# name: 13
# ---
# ```
# 
# ### Classification of Rigid Body Motion
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

# The area of calculus we are concerned with is the time derivatives of vectors which result in velocities and accelerations.
# 
# In the case of vector, it is critical to consider the reference frame when computing derivatives. This is not the case for scalars.
# 
# :::{caution}
# Computing the time derivative from frame $A$ of any arbitrary vector $\vec{x}$, we must express the vector in unit vectors attached.
# 
# If the component form of $\vec{x}$ is given in the frame $A$ by:
# 
# ```{figure} ./images/33.png
# ---
# name: 33
# ---
# ```
# 
# $$
# \vec{x} = x_1\hat{a}_x + x_2\hat{y}_x + x_3\hat{a}_x
# $$
# 
# then
# 
# $$
# \frac{{}^{A}d\vec{x}}{d\theta} \triangleq \left(\frac{d\hat{x_1}}{d\theta}\right)\hat{a}_x + \left(\frac{d\hat{x_2}}{d\theta}\right)\hat{a}_y + \left(\frac{d\hat{x_3}}{d\theta}\right)\hat{a}_z
# $$
# ::: 
# 
# ### Doorwall example
# 
# ```{figure} ./images/16.png
# ---
# name: 16
# ---
# ```
# 
# **Notation**:
# 
# $$
# \frac{{}^{A}d\vec{e}}{dt} = \text{is the time derivative of the vector } \vec{e} \text{ when observed from the }\\ \text{reference frame } A\text{. So, } \vec{e}= h\hat{b}_y = h\hat{a}_y
# $$
# 
# Therefore, 
# 
# $$
# \frac{{}^{A}d\vec{e}}{dt} = \frac{{}^{A}d(h\hat{a}_y)}{dt} = 0 \text{ (zero vector)}
# $$
# 
# :::{admonition} So, how can we compute the derivative of a vector using `SymPy`?
# :class: tip, dropdown
# 
# ```{figure} ./images/35.png
# ---
# name: 35
# width: 600px
# ---
# ```
# :::
# 
# **Another example**:
# 
# ```{figure} ./images/36.png
# ---
# name: 36
# ---
# ```
# 
# $O$, $C$, $D$ and $P$ are points as shown in the figure. $l$ and $h$ are the length and height of the door. $\theta$ is timevarying. You are asked to find (i.e., compute symbolic expressions) for the following:
# 
# ```{figure} ./images/37.png
# ---
# name: 37
# ---
# ```
# 
# All final answers are to be expressed in unit vectors attached to the $A$-frame.
# 
# :::{admonition} Solution
# :class: tip, dropdown
# ```{figure} ./images/38.png
# ---
# name: 38
# ---
# ```
# 
# ```{figure} ./images/39.png
# ---
# name: 39
# ---
# ```
# 
# The above example demonstrated the difference between taking time derivatives of the same vector from two frames.
# :::

# ### Properties of Vector Derivatives
# 
# ```{figure} ./images/40.png
# ---
# name: 40
# ---
# ```
# 
# where,
# 
# * $\vec{a},\;\vec{b},\;\vec{c}$ are arbitrary vectors.
# * $\theta,\;\lambda,\;\alpha,\;\gamma$ are scalars.
# * $t$ is scalar time.
# 
# ```{figure} ./images/41.png
# ---
# name: 41
# ---
# ```
