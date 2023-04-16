# DIODESIM
# PURPOSE
The purpose of this short project is to learn how to extract the parameters most important for modelling the static characteristcs of the diode.

# INTRODUCTION
We seek to use the data available in the datasheet of the diode to determine the numerical values of:
1. Series Resistance (ESR)
2. Ideality Factor ($\eta$)
3. Saturation Current ($I_{S}$)

A regular datasheet does not usually mention the values of the aforementioned parameters. To obtain the necessary values we must take a graphical approach and analyse the data being provided by the Forward Current vs Forward Voltage graphic (see below).
<p align="center">
<img src="https://user-images.githubusercontent.com/127757267/232328332-909f3a11-a167-4e87-95b3-3ff342c7d82c.png" width="250" height="250" />
</p>

By taking the values of $V_{F}$ and $I_{F}$ in three different points spaced reasonably apart (to minimize errors) we will obtain with help from the Shockley Diode Equation a solvable system of two equations and three unknowns.

As a brief aside, it is necessary to discuss the various diode models in existance and how they relate to our small project.
1. LVL 1: The diode has a set voltage drop which is presumed to not vary significantly in most scenarios
2. LVL 2: The diode is replaced by a fixed voltage drop in series with a fixed resistance 
3. LVL 3: The diode is replaced by a dependent voltage source in series with a fixed resistance

For our purposes we will use the third diode model, defined below:

<p align="center">
<img src="https://user-images.githubusercontent.com/127757267/232333208-b7d00b4a-22c4-4c32-a231-d9e6f69350a3.png" width="290" height="91" />
</p>

