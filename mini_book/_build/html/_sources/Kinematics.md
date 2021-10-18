# Introduction
In the most general sense, $'\text{dynamics}'$ is the study of properties or parameters that evolve or change with respect to some other parameter. For example, the field of population dynamics studies the change of animal or human populations.

In the context of this text and class, we will study the parameters the describe the motion of bodies. More often than not, the changes in these parameters with respect to time will be of interest.

At a physical level, our focus will be on the motion of bodies, which we assume can be categorized under two classes: 

1. **Particles** : These are objects that can be modelled as point masses. They have negligible dimension. 

2. **Rigid bodies** : These objects that have some shape. Also, these objects do not deform when a force is applied to them. 

This module could also be called Rigid Body Dynamics. 

## Two parts
Studying the dynamics involving the motion of particles and bodies has two distinct parts: 

1. **Kinematics** : the study of the geometry or mathematics of motion, 

without taking into consideration any forces that cause 

motion. The parameters of interest here are positions, 

velocities, and accelerations. This is also called _rigid_ 

_body motion_ or _rigid body kinematics_. 

2. **Kinetics** : the study of motion while accounting for any forces 

causing the motion by using Newton's laws. 

Kinematics 

---

**4T** 

**pin** 

**Useful fundamental concepts** 

The following definitions are used in kinematics: 

1. **Particles** : Objects that can be modelled as point masses, having 

negligible dimension. 

2. **Point** : A massless particle. 

3. **Rigid bodies** : Objects that have some shape. They can have a mass or 

be massless. Also, these objects do not deform when a 

force is applied to them. 

4. **Reference frame** : A massless rigid body with respect to which an 

analyst observes and measures motion of objects. 

**Pictorial representation of these newly defined quantities** 

P is a particle of mass _m_ 

B is a rigid body of mass _M_ 

R is a reference frame 

- **Goal** : In rigid body kinematics, we aim to mathematically describe the motion of B and P in R. 

- This requires pre-requiste knowledge on: - (i) **vectors** : unit vector, general vector, component form (ii) **vector algebra** : addition of vectors multiplication of vectors (iii) **vector calculus** : vector differentiation 

---

 or 

an 

or of 

 a O N 

 a O 

**[http://www.C](http://www.C)** 

so 

NOTE 

 DEN 4108 preferred notation 

**Revision: Vectors Fundamentals** 

- **scalar** : A quantity described purely by a number. e.g. 1, 2, 3....; one pint of beer 

- **vector** : a quantity characterised by both magnitude and direction.     ‣ **Notation** : commonly, written using Letters from the English and Greek alphabets. 

 Conversely, by the same rule, a clockwise vector will have a negative direction and points into the plane of the paper. The convention is shown below for a vector : 

- **REPRESENTATION:** Vectors are drawn as a directed line segment (i.e., a line segment with an     arrow at one end). They are typically represented for two cases: 

 Case 2: is a vector pointing out of the plane of the paper, by using right hand rule. The direction is counter clockwise, which is the positive direction by right hand rule, as shown below: 

 Case 1: is a vector in the plane of the paper at angle with horizontal: 

 The inclination of clockwise and counterclockwise vectors is with respect to the plane of the paper. 

---

 NOTATION r n b n Hill o 

I JE 

R 

 Dar f i 

Ix'T I 

 j I i Iti J R 

**Unit vector** A vector of unit magnitude (i.e., its magnitude is 1). 

 Unit vectors are commonly written with a caret (^) over a letter in the alphabet. 

Z 

 For example, is a unit vector and says that magnitude of is. 

X-Y-Z 

X 

Y 

 The set of unit vectors are right-handed (also known as a “dextral set”), which means the following relationships hold true: 

 The set of unit vector form a reference frame 

 Reference frames are useful for studying moving objects. This will become apparent in the coming weeks of lectures. 

**Reference Frame-** Is a set of three unit vectors that are mutually orthogonal. 

 In the figure below, form a Cartesian coordinate system. are a set of unit vectors that are mutually orthogonal and directed along respectively. 

---

 e r ax nay 

In 

 any az 

 A a tenXdy Az r a n ay Az 

 an or a azXage ay n au Xaz ay na x n a ay an a n ay x an az Componentformofwritingavector 

orn asbc 

 r c I 

 i a b 

abc 

 rn e a n or autbJtck 

Z 

 An alternate notation for unit vectors that make up a reference frame commonly used for dynamics is shown in the figure below; it makes use of subscripts in x, y, and z directions to make it explicit along which coordinate axis the unit vectors are aligned. We will (almost always) see (and use) such subscript-based notations in these notes for sake of clarity. 

Y 

Y 

X 

 This is a dextral set of unit vectors, which form a reference frame 

 is the unit vector along the X-direction. is the unit vector along the Y-direction. is the unit vector along the Z-direction. 

In the figure below, is a vector with coordinates in X-Y-Z,^ respectively. 

X 

Z 

 are scalars. 

The component form of is given by: 

This is the “component form” of expressing vectors, which makes use of scalars and unit vectors. 

---

 Please review addition andmultiplication of 

vetoes 

Cis 

 ii p typed code 

**Vector algebra using a CAS (Computer Algebra Systems)** 

 In this module on dynamics, we will exploit a computer algebra system (CAS, for short) to perform some key vector algebra operations. A CAS is a software that allows manipulation of non-numerical as well as numerical mathematical expressions in a manner similar to that done manually, by humans. 

 SymPy (logo to the left) is a free CAS that we will use in studying dynamics. It has many advanced features that are particularly useful in studying rigid body dynamics. 

 This set of notes is accompanied by an “interactive textbook” that you can utilise on a web browser; this is enabled by Porject Jupyter. 

 The textbook has activities that are to be performed on JupyterLab; these activities have the Jupyter icon next to them: 

 Written content: This similar to any textbook. The textbook style portion is rendered on the browser as shown to the right: 

 Code cells : Within this one performs relevant computations by writing “line of code”. A code cell appears on the browser as shown below: 

 When using the JupyterLab interface, you can type click within the code cell to enter some text. 

 This interactive textbook on the JupyterLab platform has two types of content:

---

Your coursework will be assigned on this platform by instructors. You will complete and submit all your coursework here. 

PLEASE PROCEED TO THE JUPYTER NOTEBOOK THAT REVIEWS VECTOR ALGEBRA. 

---

 A 1 paz 

on 

**a** 

 if A 1 

A 

 A B O 

 Y B 

**ggBB** 

**fBz** 

 y B A I A B 

 a Y O A 

O Y A 

GAO 

E 

B 

y 

O 

 by E 

 E o n E A B bu 

A B 

Y E 

 In feting 

where v III 

e let 

 Vectors and Reference Frames 

 The figure shows a reference frame and vector 

 is said to be fixed in the frame if and only ifnone of the characteristics of 

 are seen to change when it is observed from 

 is a wall and a door swings relative to it. The angle subtended by the door and wall is 

 So, is fixed in 

 is a vector along the top edge of the door. 

 but it is not fixed when seen from 

 and are reference frames. 

 is said to be a vector function of the scalar variable 

 in frame because one (or more) of its characteristics depends on when is observed from 

 Example 1: 

 Example 2: 

 is a vector along the vertical edge of door 

 Notice that the vector remains oriented in the same manner as the door swings. In other words, the vector is unrelated to (or unchanged by) the angle. 

 Thus, is fixed in both and 

 In summary, in Example 2 above, we have: two reference frames 

 two vectors 

 and 

 By observation, we can also write the component form of these two vectors as: 

 and 

---

 In Toy B Tsa Tn By 

A kn dyandz 

jae 

GAO 

 n r so a v by n Y E 

 na n BO n bu 

 vO e A B Y E 

 Notice that I have introduced the unit vectors and for the reference frame but is not shown though it is orthogonal to both and 

For sake of developing subsequent discussions, we will now also introduce a dextral set of unit vectors for frame 

 and and and 

 PRACTICE ACTIVITY 1 (L2PA1) For the illustrated example above, do the following: 

- Create symbols for 

- Create the reference frames 

- Create the vectors in their component as given in 

---

**if** 

t 

**og** 

i 

Cii 

 h aw no M ifw r I 

 n un ME 

 Kinematics or Rigid body kinematics is the study of motion while ignoring the cause of motion. 

 In kinematics, we are interested in "position", "velocity " , and “acceleration" and the relationship between them. 

 In other words, using the figure below, we are interested in describing the motion of B in A. 

 Classification of Rigid Body Motion 

 Rigid body motion 

 Translation 

 Rotation 

 General 3-D Rotation Simple Rotation 

**Translation:** the motion of B in A is a translation if and only if any straight line segment embedded in B remains parallel to itself when observed from A when B moves in A. If this condition is not met, then we have to consider the motion as rotation. 

**Simple rotation:** the motion of B in A is a simple rotation if and only if there exists a unit vector that remains fined in both B and A, as B moves in A. Examples in figures below: 

 Rolling disk: Rotating shaft: 

**Rigid Body Kinematics: Orientations** 

---

iii 

**jaz** 

**FA** 

 n s O n n 

 r v a by Y E 

n n a 

 an bn 

 by by A 

h by 

a 

 ri aj 

r n 

by ay 

 y E o 

 Te i To i firn y^2 

ai Ii 

 Coming back to our old example of a door hinged to a wall. 

 Here, is a unit vector that is fixed in both B and A.' Using our definition for simple rotation tells us that is. So, in mathematical notation, we can say: 

 But we must now pause to ask ourselves if there is any other unit vector that is also fixed in both B and A? It turns out that there is, indeed, another one fixed in both B and A: 

 So we can now also write: 

 So, from and , we get: 

 Why is establishing useful and critical? 

 So far, we have written the vectors and in terms of the B frame. As a result, they were not functions of Expressing the vectors in the unit vectors attached to the A frame requires us to derive relationships between and 

 allows us to derive a relationship between and 

 which then provides a basis for developing the rigid body kinematics. 

---

E I 

**jaz** 

**FA** 

 r so V a by Y E n n a an bn 

 q ebay 

q edy 

O 

v 

Y Vfa 

 n 

r n d r **IA** n Vaz osC9oO r^10 oi by^1 **IL** 

 in tan coso y E cosC9oto n a or an bn n n a bn coolant since az Plvaine from n singa t cosotz 70 top bz An 

 a 5 an y vfosoointsino.az lo n O n be bn n n a az by y 

 From the second of Equations in , we have 

 From we also get 

 in the prior example is an angle that describes the orientation of B relative to A (and vice versa). Thus, it is also called an angular position. Other common ways of referring to it are orientation angle or attitude angle. 

 Now, we come to a more involved example, where we will express in terms of the unit vectors of the A frame using the first of Equations as the starting point. 

 We can now examine the relationships between the unit vectors by drawing only the unit vectors with the vector out of the plane (see figure below this passage). 

 we have 

 Let us explore how to derive these relationships for the vectors and in the doorwall example (figure is shown again below): 

 We can then derive the following relationships by examining the lower figure, comprising only unit vectors: 

 Therefore from 

 Also from 

---

 In coso since ein 

b **ocfoff.at** 

Iz Sind 

coso Iz 

 a a 

###### fi 

**osoooo.si 7** 

## l 

 a n bye Sind 

Cosa az 

by Ey 

 by Ey 

 We can take this work one step further and write the relationships in matrix form as follows: 

 Now, we have derived the complete relationships between the unit vectors that make up the B frame in terms of the unit vectors of the A frame. 

PRACTICE ACTIVITY 2 

 In Practice Activity 1 , you used sympy to write out the vectors in the B-frame’s unit vectors. Now, write the same vectors in the A-frame. Compare their magnitudes of in the 2 frames. Are they different? 

 Let’s focus on the second row of the above matrix equation (this is highlighted in yellow below): 

 This tells us that 

Visually, this can be interpreted to mean that the door B swings relative to the wall A about the axis, which also coincides with the axis.In other words, this represents what is know an simple rotation about the y-axis. Similar relationships can also be derived for simple rotations about x-axis or z-axis. 

---

 go g 

sin 

 L tea 

so 

bz sin 

0 Cosa of 

BCA 

**Bca oil** 

 BCA too 

final 

sin^0 Cosa 

 In cosdoint cosC9o O Iz 

 In cosdoint since 

daz 

 In Tainanin Badyraytda oh t cos^90 O 

**Direction cosine matrix (abbreviated as DCM)** 

 This serves as the foundation for a more general description of orientations for General 3-D Rotation. 

 Continuing with the matrix representation of the door-wall example, the 3×3 matrix (highlighted in green above) relates the B-frame’s unit vectors to the A-frame’s unit vectors. It is called the direction cosine matrix of A in B. The symbolic notation of it is. This is for a rotation about y-axis, as mentioned on the previous page. 

 Simple notations about z-axis would result in the following DCM 

 Simple notations about x-axis would result in the following DCM: 

 Why does the term DCM have "cosine” in it? 

 Return to Equations and , you can observe that they were derived purely using the cosine of angles between different unit vectors. For example, consider the x-unit vector of the B-frame as represented in the A-frame: 

 can be written in a more generic form using only dot products (as this product is defined using cosine terms), as shown below: 

 which then becomes 

---

**i** 

 a n n n na 

in 

am but an byt anby 

**Y** 

n r 

 ai int 

 n r az but byte 

be 

In an 

Te n by anbz bn 

#### az be Is 

**act** 

Note ACB BCA 

**General 3-D Rotation and DCM** 

 Below, body B is moving freely relative To frame A. 

From the preceding discussion on dot products and DCM (direction cosine matrices), we can write the following relationships between two reference frame A and B. 

 can then also be written in the matrix form as shown below: 

 which can also be written more succinctly as: 

 is the direction cosine matrix of B in A. 

 is different from 

---

m **T** EM **I** 

**I** 

 t.no it 

ca rsI 

 A key property of DCM: 

 A very important property of DCM is that it is an orthogonal matrix. Mathematically, this means that the inverse of the DCM is the same as the transpose of the matrix. In other words, if the DCM is given by a matrix M, then: 

 This is a very useful result because it is considerably easier to compute the transpose of a matrix than it is to compute its inverse. 

 How is this property useful? At this point, we two that we can express the same vector in different reference frames. This property allows us to do so in a very easy manner. Below we show how you can easily convert (or express) a vector given in the B-frame to its equivalent in the Aframe. 

 In fact, when one compares to one sees that 

---

 Nn s 

N 

**Igf** 

 a a n ng a ant nu ay^1 Nz Az 

AdgokEffmJant 

**oafaytfgzagaa.d** 

**jaz** 

f 

A 

 NOTATION l n so 

 d dE V DE a by hi y E 

 na n BO E Lbj hay n b u 

 d de haj Q F fewvector 

C 

 The area of calculus we are concerned with is the time derivatives of vectors which result in velocities and accelerations. 

 In the case of vector, it is critical to consider the reference frame when computing derivatives. This is not the case for scalars. 

 Computing the time derivative from frame A of any arbitrary vector we must express the vector in unit vectors attached 

RULE: 

 If the component form of is given in the frame A by: 

 then 

 Door-wall example: 

 is the time derivative of the vector 

 when observed from the reference frame A. So, 

 Therefore, 

 So, how can we compute the derivative of a vector using SymPy? 

 Step 1: Create the vector 

 Step 2: Call a method on it that allows you to take a time derivative. 

Vector Calculus 

---

 az A O C DandP I r O l p nD lo i 

by 

C h CidAdf CiiBdnf y r It It I o n bn 

 adf nci .se dt 

I 

L **dat** L^7 any **Ta z** 

I Of Oft CND DI 

honey C (^1) bit tan hdytC^1 cosointsinced than **AdI** lO sindoin Cosonaz At Barn **Iii** dt I C **Int** C **Igt** C Tsz **Lbj** e **Intlfosiba** sin.bg B dI L **Of** sincebn Coso **Tz** At are points as shown in the figure. ‘l’ and ‘h’ are the length and height of the door. is timevarying. You are asked to find (i.e., compute symbolic expressions) the following: All final answers are to be expressed in unit vectors attached to the A-frame. Computing Then, we can compute the time derivative quite simply as: Another example: This is done through the following steps: requires expressing the vector in the A-frame unit vectors. In other words: which is given by: requires expressing the vector in B-frame unit vectors. In other words: So, we can get: 

---

 byAy n n a a bn bag be 

(^10) In coso 0 since o a na o o 

##### 4 

 Tfkkmof be Bu Y Iz Iz sino o coso Equation 

 B o DI n ft 

LO az 

aibnk 

 Qd2,8 t 

Ddgffqtkf 

**Ddggatddgkciicda.ua** 

**E antifdatan** 

 Ciii ddzlq.ba Edgar but g Edggh 

Civ otdcaxk fjd.am xktax k 

D8^8 

D8 

 Thus, we get: 

The above example demonstrated the difference between taking time derivatives of the same vector from two frames. 

 are scalars. 

**Properties of Vector Derivatives** 

 In the following, are arbitrary vectors. 

 is scalar time. 

---

jaz 

 FA l p n r 

 D lo a by C w Y r 

 I o n bn 

 i tdrCiiBdq It It 

0 

**Practice Activity 3:** Implement the preceding door-wall example in SymPy. Figure is provided below for reference: 

 You can use some of your prior work in Practice Activity 2 as a starting point for this activity. 

 Find: 

 HINT: You will use a new feature to make a time-varying function. This feature is called dynamicsymbols. 

---

AwB 

rA 

**it** 

h 

 O itwB I8n t in^0 

i 

AwgD **8h** 

to A 

WAKE 

Cii 

 4 I.heradls r r 

 I un AwB 4n 

**Rigid Body Kinematics:** 

**Angular Velocity and Angular Acceleration** 

 Rotating shaft 

 Angular velocity: 

 Notation: 

 This is defined as the time rate of change of orientation. 

 Case 1: Simple Rotation 

 REVIEW : the motion of B in A is a simple rotation if and only if there exists a unit vector that remains fixed in both B and A as B moves in A. Mathematically, simple rotation leads to 

 if 

 if 

 rotation of B in A increases rotation of B in A decreases 

 Rolling disk 

 Angular velocity is denoted using the greek letter omega. For example, in the figure below, is the angular velocity of B in A 

 Examples 

---

r A WBO 

## i 

TsaToy be 

Wu 

B 

## E AdgIby^5 but Adak 

## B by AdgIba By Iz 

n n n 

 AWB Wa 

 bn t Wy 

 by t wz bz 

Wn wywz 

## i 

# 8 E3 

Nw 

N 

## wit Aig Big 

**Case 2: General 3-D Rotation** 

 Below, body B is moving freely relative to frame A. 

 are rigidly fixed to B. 

 The angular velocity of body B in frame A is mathematically defined as 

 which can then be written in a more compressed form as: 

 where are scalar components of the angular velocity vector in the x, y, and zdirections respectively. 

 CHAIN RULE FOR ANGULAR VELOCITY 

---

r A WBO 

 As B N 

A B Ad_Aw 

B 

at 

 kz C g 

A 

**f** 

n r p^0 

 ay by yo n r an b p n f B 

 Asa Iie DE 

 Angular acceleration is the time rate of change of angular velocity vector. 

In the figure above, B is moving freely in A. The angular acceleration of B in A is denoted as 

 Notation: We use the greek letter alpha (lower-case) to represent angular acceleration. 

It is defined as 

Indeed, one must be careful to express the angular velocity in the appropriate reference frame prior to computing its time derivative. Unfortunately, it is not always convenient (or desirable and might even be impossible) to switch between reference frames before computing the derivative. So, some special results are presented to tackle such scenarios, which are presented after the next example. 

The door-wall example is modified to have an additional object: a cat flap C which makes an angle with the door's y-axis. 

 You are asked to compute the angular acceleration of the cat flap C with respect to A. The angular acceleration of the cat flap C with respect to A is given by 

 Example 

 Solution: 

 This means we have to first determine the angular velocity of C in A. Then we can take its time derivative from frame A. This angular velocity of C in A can be computed using the chain rule given by Equation 6.1 as: 

---

Auge 

Aw **BE** 6.1 

Cag 

A B 

w (^8) **by E dy** N lb A **Bwc** of bn Of sonant since d A C Age **AEE** DE cosoint sinceiz Of since'antcoso Iz O **dy** di Ci ny y r A WBO ricin a w I y t vBatVz bytb Bdq O Vi VzY 3 I dt Aday AwBxy B is in simple rotation relative to A. So, C is in simple rotation relative to B. So, Then, we compute the angular acceleration as: **Special results involving time derivatives** are the scalar components of As before, A is a fixed reference frame with unit vectors rigidly attached to it, i.e., **KEY RESULT 1** Likewise, B is a rigid body with unit vectors rigidly attached to it, i.e., is an arbitrary vector that is fixed in B and given in its component form by: in frame B and as it is fixed in B it follows From examining the figure, we can easily say that: 

---

 GUEN Naz v 

by 

A WBO 

 i a'iCi my^2 an af bz n bicix.y.ec bn 

 Aw B Iz 

 n I I Vibe A 

Few 

AwB y 

 on 

Y Vibe V antSinay 

 Itb riff sinoantcosoayJAW 

BXY 

O.az Yc Lo s 0 a n t s i n d ay v8fsinoa Costas 

 We will prove key result 1 (boxed in red above) is true for a trivial case: simple rotation. 

 Likewise, B is a rigid body with unit vectors rigidly attached to it, i.e., 

 B is hinged to A such that it is in simple rotation, such that: 

 is an arbitrary vector that is fixed in B and given in its component form by: 

 Prove that: 

 So 

 And 

 Hence, proved. 

 As before, A is a fixed reference frame with unit vectors rigidly attached to it, i.e., 

 Solution: 

---

ai.ci 

 n ToiCi xy^2 

V N 

Y 

E VBa 

**tvzbytvzbzaaa.vn** 

 Bday t wBx if 

 Addzy A A A VBatikby tibbett d batvzd.by Vzdbz dt dt dt 

 d Bd I flywe 

use keyresul 

dt 

vtwBxbatvzwBxbytvgtw 

### Bxbzltn 

w.by Ba^1 VzbytVzbz 

 11 v AugBy V N 

As before, A is a fixed reference frame with unit vectors rigidly attached to it, i.e., 

 KEY RESULT 2 

Likewise, B is a rigid body with unit vectors rigidly attached to it, i.e., 

 is an arbitrary vector that is moves relative to both A and B. It is given in its component form by: 

 Proof: 

 This is a very powerful formula. However, it relies on our ability to derive an expression for the angular velocity vector in an appropriate frame. We will now use it in our cat flap example. 

---

 a z C f 

A 

 r l O T 

**ay** 

 by yo 

 n r g an b u 

B 

A C 

Age **ADE** 

dE 

B A C A C 

Age 

 d Wn the't 

Wa 

de 

Auge 

Aw **BE**^6 

i 

Awf Oi by of **Tn** 

Oo A o a 

Age O by lobn^88152 

 Example 

You are asked to find angular acceleration of the cat flap C with respect to A **using key result 2**. **Solution:** 

we may then invoke KEY RESULT 2 to rewrite the right hand-side as 

This angular velocity of C in A can be computed using the chain rule given by Equation 6.1 as: 

---

**jaz** 

 C IA 

n n^70 a by y f 

 na n a n buy B 

**Practice Activity 4** 

---

we 

**To** 

a 

**go.PT** 

of 

A P 

N 

**Ayp Adf** 7.1 

At 

w 

I E 

t I E I 

7 I 

to 

deadass E z 

40 T. i s 

**E IE** 

**Particle Kinematics: Position, Velocity, Acceleration** 

So far, we have analyzed changes in orientations of reference frames and the resulting parameters of angular velocity and angular acceleration. In other words, these parameters measure the changes in angles (or angular positions). Now, we will study changes in positions of points. This topic is also called **translational kinematics**. A pictorial representation of the problem is shown and then described below. 

We utilize a position vector to locate Pthe vector has its tail fixed in A and its tip (or head) tracks P. 

**Position of P in A** 

O is a point rigidly attached to the reference frame A. 

P is a particle of mass m and is moving along the dashed path. It is said to be translating relative to frame A. 

 Note: From the figure to the right, it easy to infer: 

 From the definition of velocity (Equation ) 

 Therefore, 

**Velocity of P in A** 

Mathematically, this velocity of P in A is defined as 

 Notation 

---

 A p a n 

 AA p Aap 

 de d I 7. 2 n at 

w 

m 

o 

 o a pgp n lo 

 n n an ay 0 Oz 

 i up App N N 

 ciYYPndmiEgmirtnw A.mn dt 

So 

prop 109 q9P 

Therefore 

**hoist** 

R cosdiagsingian 

**IEEE** 

iccosoiaysinoiadta.ie 

inqagcosoEa 

sinOz geckosG 

 naatlicosaz Roisin nay 

**Acceleration of P in A** 

 Mathematically, this acceleration of P in A is defined as 

N is a fixed reference frame to which link A is attached at a point O. B is a second link attached to A at point Q. This system is commonly called a double pendulum. We assume that both links are of the same length ‘l’. 

P is a particle that is sliding on B, the second link of the double pendulum. It is located from point Q by a scalar time-varying parameter. 

The two angles that describe the double pendulum’s two links are also shown in the figure, namely: and. You are to compute: 

 Notation 

**Example** 

 Solution 

---

Also NWA 8 I 2 

Therefore 

 A q 

 P E Iz X Lait 

x cosdiagSingen 

48 

too cosg in 

 8 asindzaj 

So 

YP Is 

in Oz t k 2 cosOz 

(^8) Lt cos I In cos Oz 2e IesinOz b n since rag A p A p SP Lii if de de I sinceztnozcos.dz ate or cos Oz a 82 since^2 ay 

---

 w w g 

Ayp Ay'S AugB x **IBP** 7.3 

Age Aad ftp.BxqOP tLAwBxAwBxnf0P 

App 

Apd 

AWB 

 p BP 

Aap 

Aad 

Afb 

**Two key velocity/acceleration transfer theorems** 

 This theorem is useful for determining the velocity (and/or acceleration) of one point on a rigid body by using (or transferring to) another point on the same rigid body. 

 In the adjoining figure, P and Q are two points that are rigidly fixed to the same rigid body, B. Further, B is in freemotion relative to A. In other words, B is moving freely in A; in other words, it is rotating and translating when viewed from A. 

 In such a scenario, the following two relationships can be used to compute the velocity and acceleration of P in A. 

 Notation in above equations 

 is the velocity of P in A. 

 is the velocity of Q in A. 

 is the angular velocity of B in A. 

 is the position vector with tail at Q and tip at P. 

 is the acceleration of P in A. 

 is the acceleration of Q in A. 

 is the angular acceleration of B in A. 

 There are two theorems that are useful in particle kinematics that allow us to compute velocities and accelerations by transferring them to another point. They are discussed below. 

**Theorem 1: Two-point theorem** 

---

AugB A 

 B o 

**Ayp** Ay'S 

 A P A Q a a 

o 

 w N p N NwnAxq v v 

P 

NqP 

**NIJtnf** xq.HNwfxfNwnAxri9 

F NAO 

pp 

Pa on 

PB 

**Some special cases of theorem 1** 

 Case 1: If B is purely in translation 

 Thus, 7.3 reduces to 

 and 7.6 reduces to 

 Here, 7.3 reduces to 

 and 7.6 reduces to 

 Case 2: If B is in simple rotation about a fixed axis. E.g., a simple pendulum, (see figure). 

 Case 3: Rolling without slip Consider the case shown in the adjoining figure containing two discs, A and B. The two discs are rolling on each other and maintain a single point of contact P. Their motion is observed from a fixed frame N. 

 As the point P is clearly shared between the 2 bodies, we introduce the following notation: 

 is the contact point belonging to body A. 

 is the contact point belonging to body B. 

---

My 

 PA NyPB 

Find **Ay** 

P 

P 

r y w 

Oe 

**THE** 

Ay 

is AyesA 

SA 

Ay 

 8D O AIS 

AY P Aye Aug 

 D ISP 

 If it is said that A rolls without slip on B, then the following assumption can be made in tackling a problem: 

**Common example for rolling without slip** 

In the figure below, the disk D rolls without slip on A. P is a point on the disk’s circumference. 

**Solution** 

 Step 1: To solve this problem, you need to identify a special point shared between the bodies D and A; this is the contact point Q. 

 Step 2: Then, because of the no-slip condition, we have: 

 is a point on the ground, and is fixed to it. Thus it has zero velocity on the ground and, at that instant, it also has zero velocity on D. So, we have 

 Step 3: Then we can use the two-point theorem to compute the velocity of P in A. 

---

we 

7.5 

Ay 

 P By 

 P A yd Aug 

 B 19 

 P 7 s 

 B P v 

76 

A nap Bna AgathaEBx 10 

P 

tCtwxAwfx (^107) t2Awf **xj**^6 **I** BP A B BP a nap na AgathaEBx^10 P tCtwxAwfx 107 **the** x it **r l Theorem 2: One-point theorem** In the figure , P is a point that translates relative to body, B. Point Q is rigidly attached to B. The one-point theorem allows computation of the velocity and acceleration of P relative to the frame A, while accounting for the relative motion of P as seen from B. The velocity formula is given by Equation is the velocity of P in B. This term is also called relative velocity. The acceleration in this scenario is computed from Equation (also called five-term beast) The highlighted term is referred to as coincident point velocity. This highlighted set of terms are identical in form to that seen in the two-point theorem. transport acceleration relative acceleration Coriolis acceleration The terms in the acceleration equation have special terminology; these are shown below. Also, note that the ‘transport acceleration’ term below is identical in form to the two-point theorem acceleration formula. 

---

3. 

7.3 7. 4 

as 76 

**f** 

 Find y and.AYP 

**woo** 

o 

 O ftp.s 

BO 

**G** Oz 

2. Derive the relationships given by and using the figure below. You will need to draw TWO more position vectors for the derivation. In the figure, O is rigidly attached To A; Q is rigidly attached to B; P moves along a path on B; and B moves freely relative to A. 

 Also, prove that if P were rigidly fixed to B, then the onepoint theorem relations result in the the two-point theorem relationships. 

 for the particle sliding on the double pendulum using the relevant velocity transfer theorems, as appropriate. 

1. Derive relationships and. You need to make use of key result 2 (derivative theorem) and the definitions of velocities and accelerations. 

**Student Activities** 

