# Mass/Inertia Scalars

- __Mass__: measure of amount of materia in a body. Units of measurement: Kg, lb.
- __Mass center__: consider a set of particles as shown below which together make up the system of particles S.:


The _i<sup>th</sup>_ particle has a mass _m<sub>i</sub>_


<img src="2_Inertia/theory_img/im1.png">


[[/2_Inertia/theory_img/im1.png]]


__S<sup>*</sup>__ is a fictitious particle such that:


  


<img src="2_Inertia/theory_img/eq1.png">


This fictitious particle is called __mass center__.


How does one locate the mass centre from a point <span style="color:violet">__O__</span>?


<img src="2_Inertia/theory_img/im2.png">

<!-- #region -->
<span style="color:violet"> r* </span>:  Position  vector from <span style="color:violet">__O__</span> to S*

<span style="color:violet"> q<sub>n</sub> </span> position vector from <span style="color:violet">__O__</span> to  P<sub>n</sub>


So, we have

P<sub>n</sub> = <span style="color:violet"> r* </span> - <span style="color:violet"> q<sub>n</sub> </span>        

So, expanding __8.1__


<!-- #endregion -->

<img src="2_Inertia/theory_img/eq2.png">


For a continuum:


<img src="2_Inertia/theory_img/im3.png">


<img src="2_Inertia/theory_img/eq3.png">


where _dm_ is elemental mass that can be obtained from density _$\rho$_ and elementar volume _dV_


## Composite theorem for mass centre


<img src="2_Inertia/theory_img/im4.png">


<img src="2_Inertia/theory_img/eq4.png">


r*<sub>i</sub> is the position vector locating the mass centre of S<sub>i</sub>, the i<sup>th</sup> system of particles

m<sub>s<sub>i</sub></sub> is the mass of i<sup>th</sup> system

r* is the mass centre of the composite system <span style="color:red"> S </span>


### Example


<img src="2_Inertia/theory_img/im5.png">


<span style="color:red"> Given </span>:

<span style="color:violet"> F </span> and R are the bodies of mass density $\rho$ _Kg/m<sub>2</sub>_ and $\sigma$ _Kg/m_ respectively.

<span style="color:purple"> P </span> is a particle of mass _m_.
Dimension are as shown on figure.

<span style="color:red"> Find </span>:
mass centre of the combined system.


### Example

<!-- #region -->
<span style="color:violet"> F </span> is split into two: <span style="color:violet"> F<sub>1</sub> </span> and <span style="color:violet"> F<sub>2</sub> </span>

m<sub>F<sub>1</sub></sub>  = $\rho$ <span style="color:green"> H<sub>a</sub> </span> is mass of <span style="color:violet"> F<sub>1</sub> </span>

m<sub>F<sub>2</sub></sub> = $\rho$ <span style="color:green"> B<sub>a</sub> </span> is mass of <span style="color:violet"> F<sub>2</sub> </span>


Also

m<sub>R</sub>  = $\sigma$ <span style="color:green"> L </span> is mass of R
<!-- #endregion -->

Then,


<img src="2_Inertia/theory_img/eq5.png">


Similarly,


<img src="2_Inertia/theory_img/eq6.png">


and


<img src="2_Inertia/theory_img/eq7.png">


## Inertia scalar


For a particle,P, of mass m, we can define a parameter called the inertia scalar. This is defined relative to an arbitrary point, O. There are two such inertia scalars:


<img src="2_Inertia/theory_img/im6.png">


### 1. __Product of inertia__

<span style="color:red"> Notation </span>:

_I<sup>P/O</sup><sub>ab</sub>_ is the product of inertia of P along two lines through point O that are parallel to unit vectors n<sub>a</sub> and n<sub>b</sub>.



<img src="2_Inertia/theory_img/eq8.png">


__8.5__ can be extended for both systems of particles and continua.



- Product of inertia of system particles. 


<img src="2_Inertia/theory_img/eq9.png">


- Product of inertia of continua.


<img src="2_Inertia/theory_img/eq10.png">


<img src="2_Inertia/theory_img/im7.png">


<span style="color:red"> NOTE </span>: 

In all cases, _I<sub>ab</sub>_= _I<sub>ba</sub>_ because the formula relies on the dot product of vectors.


### 2. Moment of inertia




<img src="2_Inertia/theory_img/im8.png">


<span style="color:red"> Notation </span>:

_I<sup>P/O</sup><sub>aa</sub>_ is the moment of inertia of P about a line through point O which is parallel to the unit vector n<sub>a</sub>.


<img src="2_Inertia/theory_img/eq12.png">


__8.8__ can be extended to both systems of particles and continua.

- Product of inertia of system of particles


<img src="2_Inertia/theory_img/eq13.png">


- Product of inertia of continua


<img src="2_Inertia/theory_img/eq14.png">


<img src="2_Inertia/theory_img/im9.png">


### Example


<img src="2_Inertia/theory_img/im10.png">


- <span style="color:red"> P </span> is a particle of mass m
- <span style="color:red"> n<sub>x</sub>, n<sub>y</sub>, n<sub>z</sub> </span>   are unit vecotrs that are mutually orthogonal.
- _r = x <span style="color:red">n<sub>x</sub></span> + y <span style="color:red">n<sub>y</sub></span> + z <span style="color:red">n<sub>z</sub></span>_


<span style="color:red"> Find </span>: 

_I<sup>P/O</sup><sub>xx</sub>_,  _I<sup>P/O</sup><sub>xy</sub>_,  _I<sup>P/O</sup><sub>xz</sub>_


<img src="2_Inertia/theory_img/eq15.png">


## From inertia scalars to inertia matrix


- From the previous example, we now have some insight that we will be interested in computing the moments of inertia and products of inertia about a set of unit vectors that make up a reference frame.

- For this discussion, we assume that the unit vectors are: <span style="color:red"> n<sub>x</sub>, n<sub>y</sub>, n<sub>z</sub> </span>


- The inertia scalars can be used to define a square matrix called the <span style="color:red"> inertia matrix </span>.


<span style="color:red"> Notation </span>:

<span style="color:red"> _[I]<sup>S/O</sup>_ </span>  is the inertia matrix of S, a system of particles about the point O.

- The diagonal elements of this matrix are the moments of inertia.
- The off-diagonal elements are the products of inertia.
- So, the inertia matrix is represented as:


<img src="2_Inertia/theory_img/eq16.png">


<span style="color:green"> REMINDER </span>

In all cases,  _I<sub>ab</sub>_= _I<sub>ba</sub>_, because the formula relies on the dot product of vectors.


- Rigid body/ continua: The inertia scalars of a rigid body can also be arranged into an inertia matrix.






