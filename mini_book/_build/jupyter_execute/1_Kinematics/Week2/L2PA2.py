#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Overview-of-Practice-Activity-L2PA2" data-toc-modified-id="Overview-of-Practice-Activity-L2PA2-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Overview of Practice Activity L2PA2</a></span></li><li><span><a href="#Create-scalars-using-&quot;symbols&quot;" data-toc-modified-id="Create-scalars-using-&quot;symbols&quot;-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Create scalars using "symbols"</a></span></li><li><span><a href="#Creating-Reference-Frames" data-toc-modified-id="Creating-Reference-Frames-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Creating Reference Frames</a></span></li><li><span><a href="#Create-the-vectors-in-B-frame-(slightly-modified-from-L2PA1)" data-toc-modified-id="Create-the-vectors-in-B-frame-(slightly-modified-from-L2PA1)-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Create the vectors in B-frame (slightly modified from L2PA1)</a></span></li><li><span><a href="#L2PA2:-Use-the-trignometric-functions-sine-and-cosine-to-rewrite-the-vectors-in-the-A-frame" data-toc-modified-id="L2PA2:-Use-the-trignometric-functions-sine-and-cosine-to-rewrite-the-vectors-in-the-A-frame-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>L2PA2: Use the trignometric functions sine and cosine to rewrite the vectors in the A-frame</a></span><ul class="toc-item"><li><span><a href="#Exercsie:-Can-you-write-the-same-for-the-vector-e?" data-toc-modified-id="Exercsie:-Can-you-write-the-same-for-the-vector-e?-5.1"><span class="toc-item-num">5.1&nbsp;&nbsp;</span>Exercsie: Can you write the same for the vector e?</a></span></li></ul></li></ul></div>

# # Overview of Practice Activity L2PA2
# <img src="Figures/Door_Wall.png">
# 
# This notebook continues to build your dynamics knowledge using the door-wall example (see figure above), that was used in L2PA1. This is an interactive notebook that is a companion to the in-class lectures; specifically this notebook addresses the Practice Activity L2PA2, which was first presented in the file "4 Rigid body kinematics: orientations.pdf". 
# 
# The code in Sections 2 and 3 of this notebook are repeated from L2PA1. Section 4 is adapted from L2PA1; the modifications in this notebook are to the variable names for the vectors $\bf v$ and $\bf e$. The remaining content specifically addresses L2PA2.

# # Create scalars using "symbols"

# In[1]:


from sympy import symbols


# In[2]:


v, theta, e = symbols('v theta e')


# In[3]:


v


# In[4]:


theta


# In[5]:


e


# # Creating Reference Frames
# A and B are reference frames. Let's create them using SymPy!

# In[6]:


from sympy.physics.mechanics import ReferenceFrame


# In[7]:


A = ReferenceFrame('A')


# In[8]:


B = ReferenceFrame('B')


# # Create the vectors in B-frame (slightly modified from L2PA1)

# In this section, we use the variable names `v_vec_B` and `e_vec_B` for $\bf v$ and $\bf e$ expressed in the unit vectors of the B referenece frame.

# In[9]:


v_vec_B = v*B.x


# In[10]:


v_vec_B


# In[11]:


e_vec_B = -e*B.y


# In[12]:


e_vec_B


# # L2PA2: Use the trignometric functions sine and cosine to rewrite the vectors in the A-frame

# We first import the trignometric functions for sine and cosine from sympy; these are written in their short forms as `cos` and `sin`. The importing from `sympy` is done in the following line: 

# In[13]:


from sympy import sin, cos


# Then, we define the vector $\bf v$ as expressed in the unit vectors attached to the frame A using the variable name `v_vec_A` in the following manner:

# In[14]:


v_vec_A = v * (cos(theta)*A.x + sin(theta)*A.y)


# In[15]:


v_vec_A


# ## Exercsie: Can you write the same for the vector e?

# Can you define the vector $\bf e$ expressed in the unit vectors attached to the frame A? You should use a variable name `e_vec_A` to do so in the cell below:

# In[ ]:




