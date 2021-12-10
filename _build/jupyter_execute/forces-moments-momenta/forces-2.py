#!/usr/bin/env python
# coding: utf-8

# # Momentum: Linear and Angular

# ## Introduction
# 
# This chapter discusses linear momentum and angular momentum of particles and rigid bodies. These are key concepts that:
# - merge what we have learned 
# - the various aspects knowledge of kinematics and mass/inertia scalars; and
# - underpin Newton's second law of motion, which is the centerpiece to finally deriving equations that describe the motion of engineering systems using the particle and rigid body approximations.

# ## Linear Momentum
# 
# It is a vector quantity. 
# - Particle: The linear momentum of a single particle is the product of its mass and velocity. As velocity of a prticle (as it is essentially a point with mass) is defined relative to a certain frame, linear momentum is also defined relative in a certain frame.
# 
# ### Notation
# 
# ${}^{N}L^{P}$ is the linear momentum of particle P in frame N. The mathematical definition is:
# 
# ```{figure} ./images/12.png
# ---
# name: 12
# ---
# ```
# 
# ### System of particles
# 
# The linear moemntum for a system of $n$ particles is the sum of the linear momenta of individual particles.
# 
# #### Notation
# 
# ${}^{N}L^{S}$ is the linear momentum of system of particles $S$ in frame $N$. It is given by:
# 
# ```{figure} ./images/13.png
# ---
# name: 13
# ---
# ```
# 
# By virtue of mass center definition, this reduces to a much simpler equation.
# 
# ```{figure} ./images/14.png
# ---
# name: 14
# ---
# ```
# 
# ${}^{N}L^{S} = m^{N}v^{S^{*}}$ 
# 
# where
# 
# - $m$ is the mass of the system given by $\sum_{i} m_{i}$. 
# - $v^{S^{*}}$ is the velocity of the system's mass center $S^{*}$.
# 
# ### Rigid bodies
# 
# The linear momentum of a rigid body (or, more generally, a continua) is similar to that of a system of particles; except we make use of the integral in its definition.
# 
# ```{figure} ./images/15.png
# ---
# name: 15
# ---
# ```
# 
# where,
# 
# - $m$ is the mass of the body.
# - $^{N}v^{B^{*}}$ is the velocity of the body's mass center $B^{*}$

# ## Angular Momentum
# 
# Angular momentum is also a vector quantity. It is quite generally defined as the moment of the linear momentum vector. The letter $\text{H}$ (boldface is vector, when typed) to represent this quantity.
# 
# ### Particle
# 
# $^{N}H^{P/O}$ is the angular momentum of the particle $P$ with respect to the point $O$ in frame $N$. It is quite simply the moment of about $O$ of the linear momentum of $P$ in $N$:
# 
# ```{figure} ./images/16.png
# ---
# name: 16
# ---
# ```
# 
# ```{hint}
# The moment of a bound vector is defined relative to a certain point. In this case, we are taking moment of the _linear momentum_ of $P$ defined in frame $N$ (a bound vector) relative to the point $O$.
# ```
# 
# ### System of Particles
# 
# The angular momentum of a system of particles is quite simply the vector sum of the angular momentum of each particle in the system. For the figure below, for a system of particles $S$ with $n$ particles, the system’s angular momentum can be defined about the point $O$ as:
# 
# ```{figure} ./images/17.png
# ---
# name: 17
# ---
# ```
# 
# ### Rigid body
# 
# We can derive the angular momentum of a rigid body (or, more generally, a continuum) relative to $O$ in a similar fashion. This is done using $P$, a generic point of $B$ with an elementary mass $dm$.
# 
# ```{figure} ./images/18.png
# ---
# name: 18
# ---
# ```
# 
# Now, evaluating this integral is quite challenging. So can we come up with a much simpler expression for evaluations the angular momentum of a body? Indeed, this is possible. Let’s see how we can do this$\ldots$
# 
# First, we make use of the two-point theorem to rewrite the velocity of P in terms of the mass centre of the body:
# 
# ```{figure} ./images/19.png
# ---
# name: 19
# ---
# ```
# 
# So, we can see that the angular momentum is now the vector sum of two integrals. We will now examine the implication of each of these terms. We start with the term in green
# 
# ```{figure} ./images/20.png
# ---
# name: 20
# ---
# ```
# 
# Now, we can quite easily observer that this cross product is, in fact, the angular momentum of the mass centre $B^*$ about the point $O$ in the frame $N$. In other words,
# 
# ```{figure} ./images/21.png
# ---
# name: 21
# ---
# ```
# 
# Now, we examine the term that was highlighted in pink:
# 
# $$
# \int_m{\vec{r}dm} = 0
# $$
# 
# So,
# 
# ```{figure} ./images/22.png
# ---
# name: 22
# ---
# ```
# 
# By definition of a mass centre 
# 
# ```{figure} ./images/23.png
# ---
# name: 23
# ---
# ```
# 
# Now, if we examine the above cross product on the right-hand side and compare it to the definition of angular momentum of a rigid body, we can see that this is the angular momentum of the body B __about the mass centre $B^{*}$__. In other words,
# 
# ```{figure} ./images/24.png
# ---
# name: 24
# ---
# ```
# 
# $^{N}H^{B/B^{*}}$ is frequently called the central angular momentum; central refers to the calculation of angular momentum being done about the mass centre. Further, it can also be shown that the central angular momentum is easily calculated by the following formula:
# 
# ```{figure} ./images/25.png
# ---
# name: 25
# ---
# ```
# 
# This says that the central angular momentum is given by the product of the inertia matrix of $B$ about $B^*$ and the angular velocity of $B$ in $N$; this proof is not shown here. In summary, we can see that this second integral highlighted in pink eventually yields:
# 
# ```{figure} ./images/26.png
# ---
# name: 26
# ---
# ```
# 
# $[I]^{B/B^{*}}$ is the inertia matrix of $B$ about $B^*$; it is also called the __central inertia matrix__.
#  
# Indeed, one must be careful in ensuring that the the inertia matrix and the angular velocity were expressed in the same reference frames BEFORE taking the product.
# 
# Finally, we now return to Equation $10.1$ to write it in its most concise form as:
# 
# ```{figure} ./images/27.png
# ---
# name: 27
# ---
# ```
# 
# Equation $10.4$ is called the __Transfer theorem for angular momentum__. This is because it allows us to calculate the angular momentum of a body about any point external to the body by transferring to its centre of mass and then to the point of interest. 
# 
# ### Special case
# 
# Say that we want to evaluate $^{N}H^{B/Q}$, where $Q$ is an arbitrary point rigidly fixed on the rigid body. $Q$ is not an elementary particle.
#  
# ```{figure} ./images/28.png
# ---
# name: 28
# ---
# ```
# 
# Again, we make use of the two-point theorem to rewrite the velocity of P in terms of Q. So, the
# expression for angular momentum above is now:
# 
# ```{figure} ./images/29.png
# ---
# name: 29
# ---
# ```
# 
# which then becomes,
# 
# ```{figure} ./images/30.png
# ---
# name: 30
# ---
# ```
# 
# Now, it can be shown that the integral highlighted in pink reduces to the simpler result; it is the product of the inertia matrix of $B$ about $Q$ and the angular velocity of $B$ in $N$; as before, this proof is not shown here but can be easily derived. So, the above equation is written in short hand as,
# 
# ```{figure} ./images/31.png
# ---
# name: 31
# ---
# ```
# 
# Two key observations may now be made that make 10.5 far simpler:
# 
# __Observation 1__: If $Q$ is coincident with the mass centre $B^*$, then $r^{*} = 0$. Thus,
#  
# ```{figure} ./images/32.png
# ---
# name: 32
# ---
# ```
# 
# __Observation 2__: If Q is not the mass centre, but is a point that is fixed in both B and N, then we have the following circumstance where,
#  
# $$
# ^{N}v^{Q}=0
# $$
# 
# In this case, as well, we end up with the same result as case 1, where,
# 
# ```{figure} ./images/32.png
# ---
# name: 32
# ---
# ```
# 
# ### Composite theorem for Angular Momentum
# 
# Consider a system, $S$, is composed of a set of many smaller subsystems i.e., $<S_1, S_2, S_3,\ldots, S_n>$ as shown below.
# 
# ```{figure} ./images/33.png
# ---
# name: 33
# ---
# ```
# 
# The angular momentum of this system, $S$, about an arbitrary point $O$ is given by:
# 
# ```{figure} ./images/34.png
# ---
# name: 34
# ---
# ```
