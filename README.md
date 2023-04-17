# DIODE MODEL PARAMETER EXTRACTION
## PURPOSE
The purpose of this short project is to learn how to extract the parameters most important for modelling the static characteristcs of the diode.
The diode simulated in this project is in fact the LED [VSLY5940](https://www.vishay.com/docs/84240/vsly5940.pdf).
## INTRODUCTION
We seek to use the data available in the diode datasheet to determine the numerical values of:
1. Series Resistance (ESR)
2. Ideality Factor ($\eta$)
3. Saturation Current ($I_{S}$)

A regular datasheet does not usually mention the values of the aforementioned parameters. To obtain the necessary values we must take a graphical approach and analyse the data being provided by the Forward Current vs Forward Voltage graphic (see below).
<p align="center">
<img src="https://user-images.githubusercontent.com/127757267/232343543-f7283861-69a8-41be-b0f5-b377fe8b1c5a.png" width="400" height="400" />
</p>



By taking the values of $V_{F}$ and $I_{F}$ in three different points spaced reasonably apart (to minimize errors) we will obtain with help from the Shockley Diode Equation $\left( I_{D} = I_{S}\cdot exp\left(\frac{V_{D}}{N\cdot V_{TH}}\right)\right)$ a solvable system of two equations and three unknowns.

As a brief aside, it is necessary to discuss the various diode models in existance and how they relate to our small project.
<p align="center">
  <img src="https://user-images.githubusercontent.com/127757267/232345998-da2d026d-b055-4da6-98bb-db2576a8db06.png" />
</p>
1. LVL 1: The diode has a set voltage drop which is presumed not to vary significantly in most scenarios
<p align="center">
  <img src="https://user-images.githubusercontent.com/127757267/232345634-fc61e80c-bbc5-488c-9ed4-62b5f34587e7.png" />
</p>
3. LVL 2: The diode is replaced by a fixed voltage drop in series with a fixed resistance 
<p align="center">
  <img src="https://user-images.githubusercontent.com/127757267/232345529-a4ecc151-9b80-482a-82ca-bcdc2f1a24bd.png" />
</p>
3. LVL 3: The diode is replaced by a dependent voltage source in series with a fixed resistance
<p align="center">
<img src="https://user-images.githubusercontent.com/127757267/232333208-b7d00b4a-22c4-4c32-a231-d9e6f69350a3.png" width="290" height="91" />
</p>

For our purposes we will use the third diode model, where $V_{D}=N\cdot V_{TH}\cdot ln\left(\frac{I_{D}}{I_{S}}\right)$ is the command function and $V_{F}=V_{D}+ESR\cdot I_{D}$ is the voltage drop experienced by the diode.




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
$$V_{F1}-V_{F2}=A_{1}\cdot ESR+B_{1}\cdot N$$
$$V_{F1}-V_{F3}=A_{2}\cdot ESR+B_{2}\cdot N$$

where: $A_{1}=I_{D1}-I_{D2}$ ; $B1=V_{TH}\cdot ln\left(\frac{I_{D1}}{I_{D2}}\right)$ for the first equation and $A_{2}=I_{D1}-I_{D3}$ ; $B2=V_{TH}\cdot ln\left(\frac{I_{D1}}{I_{D3}}\right)$ for the second equation
<br></br>
$$V_{F1}-V_{F2}=A_{1}\cdot ESR+B_{1}\cdot N\quad ||\quad \cdot (-B_{2})$$

$$V_{F1}-V_{F3}=A_{2}\cdot ESR+B_{2}\cdot N\quad ||\quad \cdot (B_{1})$$

$$B_{1}\cdot (V_{F1}-V_{F3})-B_{2}\cdot (V_{F1}-V_{F2})=ESR\cdot (A_{2}B_{1}-A_{1}B_{2})$$
<br></br>
$$ESR = \frac{B_{1}\cdot (V_{F1}-V_{F3})-B_{2}\cdot (V_{F1}-V_{F2})}{A_{2}B_{1}-A_{1}B_{2}}$$
<br></br>
We do the same thing to find N.

$$N = \frac{A_{1}\cdot (V_{F1}-V_{F3})-A_{2}\cdot (V_{F1}-V_{F2})}{B_{2}A_{1}-A_{2}B_{1}}$$

And to find $I_{S}$ we simply introduce the newly found values in the Shockley equation.

$$I_{S}=I_{D1}\cdot exp\left(-\frac{V_{F1}-ESR\cdot I_{D1}}{N\cdot V_{TH}}\right)$$

The code:
```python
A1 = Id1-Id2
B1 = Vth * np.log(Id1/Id2)

A2 = Id1-Id3
B2 = Vth * np.log(Id1/Id3)


'''
Ideality factor (N)
'''
N = (A1 * (V1-V3) - A2 * (V1-V2)) / (A1*B2 - A2*B1)


'''
Internal series resistance (Rs)
'''
Rs = (B1 * (V1-V3) - B2 * (V1-V2)) / (A2*B1 - A1*B2)


'''
Saturation current
'''
Isat = Id1 * np.exp(-(V1-Rs*Id1)/(N*Vth))
```

For the values provided in the table above we obtain:
$ESR = 1.1884\\; \Omega,\quad N = 2.4467,\quad I_{S} = 2.7641\\; pA$

And with these values we obtain the following static characteristic, clearly very close to the original datasheet one:
<p align="center">
<img src="https://user-images.githubusercontent.com/127757267/232346258-3a94c56b-c2c9-4171-aabf-c992a5276aa7.png" width="800" height="600" />
</p>

## Testing and matching the new diode model
Now that we've found the necessary parameters, we input known voltages/ currents and gauge the correctness of the output and to make things more interesting we'll use the Lambert W function.

Given that we know $ESR,\\; N,\\; I_{S}$ find the corresponding currents for $V_{F}=2V$ and $V_{F}=2.5V$.

$$V_{F}-ESR\\; I_{D}-\eta\\; V_{TH}\\; ln\left(\frac{I_{D}}{I_{SAT}}\right)=0$$
$$\frac{V_{F}}{\eta\\; V_{TH}}-\frac{ESR\\;I_{D}}{\eta\\; V_{TH}}=ln\left(\frac{I_{D}}{I_{SAT}}\right)$$
$$exp\left(\frac{V_{F}}{\eta\\; V_{TH}}-\frac{ESR\\;I_{D}}{\eta\\; V_{TH}}\right)=\frac{I_{D}}{I_{SAT}}$$

$$exp\left(\frac{V_{F}}{\eta\\; V_{TH}}\right)=\frac{I_{D}}{I_{SAT}}\cdot exp\left(\frac{ESR\\; I_{D}}{\eta\\; V_{TH}}\right)$$

$$\frac{ESR\\; I_{SAT}}{\eta\\;V_{TH}}\cdot exp\left(\frac{V_{F}}{\eta\\; V_{TH}}\right)=\frac{ESR\\; I_{D}}{\eta\\; V_{TH}}\cdot exp\left(\frac{ESR\\; I_{D}}{\eta\\; V_{TH}}\right)$$
We set $w=\frac{ESR\\; I_{D}}{\eta\\; V_{TH}}$

$$w\\;e^{w}=\frac{ESR\\; I_{SAT}}{\eta\\;V_{TH}}\cdot exp\left(\frac{V_{F}}{\eta\\;V_{TH}}\right)$$

$$w=LambertW\left(\frac{ESR\\; I_{SAT}}{\eta\\;V_{TH}}\cdot exp\left(\frac{V_{F}}{\eta\\;V_{TH}}\right)\right)$$

$$\frac{ESR\\; I_{D}}{\eta\\; V_{TH}}=LambertW\left(\frac{ESR\\; I_{SAT}}{\eta\\;V_{TH}}\cdot exp\left(\frac{V_{F}}{\eta\\;V_{TH}}\right)\right)$$

$$I_{D}=\frac{\eta\\; V_{TH}}{ESR}\cdot LambertW\left(\frac{ESR\\; I_{SAT}}{\eta\\;V_{TH}}\cdot exp\left(\frac{V_{F}}{\eta\\;V_{TH}}\right)\right)$$

The code for doing the math:

```python
VFt = np.array([2,2.5])
Idt = np.real(N * Vth / Rs * lambertw((ESR*Isat)/(N*Vth)*np.exp(VFt/(N*Vth))))
#Idt[0]=0.323859  A
#Idt[1]=0.703234  A
```
We obtain $I=0.323859$ for $V_{F}=2V$ and $I_{D}=0.703234$ for $V_{F}=2.5V$, which are very close to the values presented in the datsheet, as you can see below:
<p align="center">
  <img src="https://user-images.githubusercontent.com/127757267/232427182-3d39725d-ddb7-4654-a686-a60139518ed7.png" />
</p>

## Bibliography and Notes
This project is based on [this](https://electronics.stackexchange.com/questions/601136/ltspice-modeling-an-led) post on electronics.stackexchange.

Other great resources:
1.  https://ltwiki.org/files/SPICEdiodeModel.pdf
2.  https://electronics.stackexchange.com/questions/480311/basic-diode-question-about-voltage-drop
3.  https://web.ece.ucsb.edu/Faculty/rodwell/Classes/ece2c/labs/CurveFittinginExcel.pdf
4.  Semiconductor device modeling with SPICE
by Massobrio, Giuseppe

All custom plots are done in matplotlib.

All schematics if not otherwise specified are done in draw.io.
