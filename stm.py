import streamlit  as st

import numpy as np
import matplotlib.pyplot as plt

st.title("Pressure Profile Application")

st.sidebar.title("Inputs")

## Taking inputs from the users

### Taking inputs as slider

k = st.sidebar.slider("Permeability (mD)", min_value =1, max_value =100, value =10)
mu = st.sidebar.slider("Viscosity (cp)", min_value =10, max_value =20, value =11)
q = st.sidebar.slider("Flow Rate (STB/day)", min_value =100, max_value =500, value =150)

### Taking inputs from number inputs

rw = st.sidebar.number_input("Wellbore Radius (ft)", min_value =1, max_value =10, value =1)
re = st.sidebar.number_input("Outer Radius of Reservoir (ft)", min_value =100, max_value =10000, value =4000)

pe = st.sidebar.number_input("Pressure at boundary of reservoir (psi)", min_value =100, max_value =10000, value =4000)
B = st.sidebar.number_input("Formation Volume Factor (bbl/STB)", min_value =1, max_value =2, value =1)
h = st.sidebar.number_input("Net Pay Thickness (ft)", min_value =10, max_value =100, value =50)

### logic

r = np.linspace(rw, re, 500)

pressure = pe - (141.2*q*mu*B*(np.log(re/r))/(k*h))

y_min = pressure.min()

### button

b = st.button("Generate Pressure Profile")

if b:

    plt.style.use("classic")
    plt.figure(figsize=(10, 5))
    
    # plotting the graph

    fig, ax = plt.subplots()

    ax.plot(r, pressure,linewidth=4)
    ax.axhline(y_min,linewidth=3,color="red")
    ax.grid(True)
    ax.set_xlabel("Distance from wellbore (ft)")
    ax.set_ylabel("Pressure at radius r, (psi)")
    ax.set_title("Pressure Profile")
    ax.set_ylim(0, pe+1000)
    ax.set_xlim(0, re+100)

    ## plotting the figure
    st.pyplot(fig)