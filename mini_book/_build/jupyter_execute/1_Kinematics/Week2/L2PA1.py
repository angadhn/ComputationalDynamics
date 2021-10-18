#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Overview-of-Practice-Activity-L2PA1" data-toc-modified-id="Overview-of-Practice-Activity-L2PA1-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Overview of Practice Activity L2PA1</a></span></li><li><span><a href="#Create-scalars-using-&quot;symbols&quot;" data-toc-modified-id="Create-scalars-using-&quot;symbols&quot;-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Create scalars using "symbols"</a></span></li><li><span><a href="#Creating-Reference-Frames" data-toc-modified-id="Creating-Reference-Frames-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Creating Reference Frames</a></span></li><li><span><a href="#Create-the-vectors" data-toc-modified-id="Create-the-vectors-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Create the vectors</a></span></li></ul></div>

# # Overview of Practice Activity L2PA1
# 
# This is an interactive notebook that is a companion to the in-class lectures; specifically this notebook addresses the Practice Activity L2PA1 presented in the file "3 Vectors and reference frames.pdf".
# 
# <img src="Figures/Door_Wall.png">
# 
# This activity implements the door-wall example (see figure above) as an interactive textbook that works in JupyterLab. The activity is referred to as Practice Activty L2PA1 in your the handouts used during in-class lectures. Your goal is to implement the two handwritten equations (see Equation 1 below) into the code cells using sympy's feature set.
# 
# <img src="Figures/Equation1.png">

# # Create scalars using "symbols" 

# In[1]:


from sympy import symbols


# We begin by using sympy's `symbols` to create the scalars $v$, $e$ and $\theta$, as shown below:

# In[2]:


v, theta, e = symbols('v theta e') # These are scalar symbols.


# In[3]:


v


# In[4]:


theta


# In[5]:


e


# # Creating Reference Frames
# A and B are reference frames that make up the wall and the door, respectively. Let's create them. First, we need to gain access to the `ReferenceFrame` feature that is provided to us by `sympy.physics.mechanics` in the following way:

# In[6]:


from sympy.physics.mechanics import ReferenceFrame


# Then, we have to specifically create the wall A's reference frame to gain access to the set of 3 dextral unit vectors ${\hat {\bf a}_x}$, ${\hat {\bf a}_y}$, and ${\hat {\bf a}_z}$ as below:

# In[7]:


A = ReferenceFrame('A') # This creates the unit vectors that make up the wall's frame A


# The reference frame attahed to the door B can also be created in a similar fashion so that we gain access to the set of 3 dextral unit vectors ${\hat {\bf a}_x}$, ${\hat {\bf a}_y}$, and ${\hat {\bf a}_z}$. This is done as shown below:

# In[8]:


B = ReferenceFrame('B') # This creates the unit vectors that make up the door's frame A


# We can access the unit vectors by using the variable name that points to any reference frame (i.e. `A` or `B`) and appending `.x` or `.y` or `.z` to it. For example:

# In[9]:


B.x


# We will now combine all the information concerning the scalars and unit vectors to define the vectors ${\bf v}$ and ${\bf e}$ of the door-wall example in the next section.

# # Create the vectors
# 
# <img src="Figures/Equation1.png">
# 
# The final task of L2PA1 is to type in the above handwritten component form of ${\bf v}$ and ${\bf e}$ the scalars and unit vectors that we created in Sections 2 and 3 using SymPy. We will store the ${\bf v}$ and ${\bf e}$ as two variables `v_vec` and `e_vec`, respectively, as shown below:

# In[10]:


v_vec = v*B.x # v_vec stores the vector v that was handwritten in Equation 1 at the start of this notebook.


# In[11]:


v_vec


# In[12]:


e_vec = -e*B.y # v_vec stores the vector v that was handwritten in Equation 1 at the start of this notebook.


# In[13]:


e_vec

