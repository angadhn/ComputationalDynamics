#!/usr/bin/env python
# coding: utf-8

# # Introduction

# In the most general sense, $\mathrm{dynamics}$ is the study of properties or parameters that evolve or change with respect to some other parameter. For example, the field of population dynamics studies the change of animal or human populations.
# 
# In the context of this text and class, we will study the parameters the describe the motion of bodies. More often than not, the changes in these parameters with respect to time will be of interest.
# 
# At a physical level, our focus will be on the motion of bodies, which we assume can be categorized under two classes: 
# 
# 1. **Particles**: These are objects that can be modelled as point masses. They have negligible dimension. 
# 
# 2. **Rigid bodies**: These objects that have some shape. Also, these objects do not deform when a force is applied to them. 
# 
# This module could also be called _Rigid Body Dynamics_. Studying the dynamics involving the motion of particles and bodies has two distinct parts:
# 
# 1. **Kinematics**: the study of the geometry or mathematics of motion, without taking into consideration any forces that cause motion. The parameters of interest here are positions, velocities, and accelerations. This is also called rigid body motion or rigid body kinematics.
# 
# 2. **Kinetics**: the study of motion while accounting for any forces causing the motion by using Newton's laws.
# 
# ```{figure} ./images/1.png
# ---
# name: 1
# ---
# ```
