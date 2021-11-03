# Key Theorems for computing <span style="color:violet"> $[I]^{S/O}$ </span>

There are three useful theorems to compute moments of inertia. They are:

1. __Rotation theorem__
2. __Parallel axis theorem__ (or translation theorem)
3. __Composite theorem__

Let us examine them in further detail.


## 1. Rotation theorem


<img src="2_Inertia/theory_img2/im1.png">


- In the figure __X-Y-Z__ make up a cartesian coordinate system. O is the origin.
<span style="color:violet"> n<sub>x</sub>,  n<sub>y</sub>,  n<sub>z</sub>  </span> are unit vectors directed along __X,Y__ and __Z__ respectively. The unit vectos represent a reference frame <span style="color:violet"> N </span>.

- Also, the figure shows a rocket which has a reference frame <span style="color:green">R</span> attached to it. You are given the inertia matrix of the rocket <span style="color:green"> R </span> about O along the unit vectors of frame N.
Naturally, this reference frame also has 3 mutually orthogonal unit vectors: 
<span style="color:green"> r<sub>x</sub>,  r<sub>y</sub>,  r<sub>z</sub>  </span>


So far, given 


<img src="2_Inertia/theory_img2/eq1.png">


- Now, we can define another inertia matrix for <span style="color:green"> R </span> about O along the newly introduced rotating reference frame's unit vectors <span style="color:green"> r<sub>x</sub>,  r<sub>y</sub>,  r<sub>z</sub>  </span>. This matrix and its elements are:




<img src="2_Inertia/theory_img2/eq2.png">


<span style="color:red"> Question:  </span>
How are the two matrices related?


- We begin by assuming that <span style="color:green"> R  </span> is a particle of mass, m<sub>R</sub>.
    
- let us consoder a product of inertia from each matrix.



<img src="2_Inertia/theory_img2/eq3.png">


- P* is a position vecotr from O to the origin of the frame <span style="color:green"> R </span>.

We know from our discussion on direction cosine matrices that the unit vectors of <span style="color:green"> R </span> can be related to the unit vectors of <span style="color:violet"> N </span> as: 




<img src="2_Inertia/theory_img2/eq4.png">


<sup><span style="color:green"> R </span></sup>C<sup><span style="color:violet"> N </span></sup> is the direction cosine matrix of <span style="color:green"> R </span> in <span style="color:violet"> N </span>. It is a 3-by-3 matrix, which we shall assume has the following elements.


<img src="2_Inertia/theory_img2/eq5.png">


So, we can now easily derive:


<img src="2_Inertia/theory_img2/eq6.png">


And then, we can rewrite the product of inertia <span style="color:green"> J<sub>xy</sub><sup>R/O</sup> </span> as: 


<img src="2_Inertia/theory_img2/eq7.png">


This leads to


<img src="2_Inertia/theory_img2/eq8.png">


or in terms of matrix multiplication.


<img src="2_Inertia/theory_img2/eq9.png">


More generally, it can be shown that


<img src="2_Inertia/theory_img2/eq10.png">


## 2. Parallel axes theorem


In the previoussection we presumed that the rocket was a point mass. What happens if this assumption is relaxed and rockets are better approximated as a system of particles?

- P* is a position vector from O to <span style="color:green"> R* </span>,the origin of the frame <span style="color:green"> R </span>

-  <span style="color:green"> R* </span> is he mass center of the rocket

- P<sub>i</sub> is a position vector from o to <span style="color:red"> P<sub>i</sub> </span>, the i<sup>th</sup> particle on the rocket body.

- r<sub>i</sub> is a position vector from <span style="color:green"> R* </span> to <span style="color:red"> P<sub>i</sub> </span>. So,

P<sub>i</sub> = P* + r<sub>i</sub> 



<img src="2_Inertia/theory_img2/im2.png">


Now, we know that the product of inertia for this system of particles along the <span style="color:red"> n<sub>x</sub>, n<sub>y</sub>  </span>  directions given by:


<img src="2_Inertia/theory_img2/eq11.png">


The terms highlighted in green go to zero because $$\sum_im_ir_i = 0$$ by the definition of mass centers.


<img src="2_Inertia/theory_img2/eq12.png">


<span style="color:violet"> I<sub>xy</sub><sup><span style="color:green"> R/R* </span></sup> </span> is the product of inertia of <span style="color:green"> R </span> about the mass center <span style="color:green"> R* </span>.

<span style="color:violet"> I<sub>xy</sub><sup><span style="color:green"> R* /O </span></sup> </span> is the product of inertia of <span style="color:green"> R* </span> about O.

Some comments:
1. This result extrapolates to the moment of inertia scalars. For example,


<img src="2_Inertia/theory_img2/eq13.png">


2. This result extrapolates to the inertia matrix


<img src="2_Inertia/theory_img2/eq14.png">


3. This rule is only valid when going through the mass center.


## 3. Composite theorem


<img src="2_Inertia/theory_img2/im3.png">
