# DIODESIM
## PURPOSE
The purpose of this short project is to learn how to extract the parameters most important for modelling the static characteristcs of the dio
## INTRODUCTION
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

For our purposes we will use the third diode model, where $V_{D}=N\cdot V_{TH}\cdot ln\left(\frac{I_{D}}{I_{S}}\right)$ is the command function and $V_{F}=V_{D}+R_{S}\cdot I_{D}$ is the voltage drop experienced by the diode.

<p align="center">
<img src="https://user-images.githubusercontent.com/127757267/232333208-b7d00b4a-22c4-4c32-a231-d9e6f69350a3.png" width="290" height="91" />
</p>

## EXTRACTING THE PARAMETERS:
Known values: The thermal voltage $V_{TH}$ is 26mV as the test temperature is presumed to be 300K.

| $V_{F}\quad[V]$  | $I_{F}\quad[mA]$ | 
| ------------- | ------------- | 
| 1.25|1 |
| 1.5|30 |
| 2.875| 1000|

According to the diode model in use the voltage drop across the diode is $V_{F}=ESR\cdot I_{D}+N\cdot V_{TH}\cdot ln\left(\frac{I_{D}}{I_{S}}\right)\\; (1)$.
<br></br>
We write (1) for each of the three voltages in the table above:
$$V_{F1}=ESR\cdot I_{D1}+N\cdot V_{TH}\cdot ln\left(\frac{I_{D1}}{I_{S}}\right)\\; (1.1)$$
$$V_{F2}=ESR\cdot I_{D2}+N\cdot V_{TH}\cdot ln\left(\frac{I_{D2}}{I_{S}}\right)\\; (1.2)$$
$$V_{F3}=ESR\cdot I_{D3}+N\cdot V_{TH}\cdot ln\left(\frac{I_{D3}}{I_{S}}\right)\\; (1.3)$$

To simplify the equations we introduce several coefficients:
$$V_{F1}=A_{1}\cdot ESR+B_{1}\cdot N$$
$$V_{F2}=A_{2}\cdot ESR+B_{2}\cdot N$$
$$V_{F3}=A_{3}\cdot ESR+B_{3}\cdot N$$

$$V_{F1}=A_{1}\cdot ESR+B_{1}\cdot N\quad ||\quad \cdot (-B{2})
$$V_{F2}=A_{2}\cdot ESR+B_{2}cdot N$$


