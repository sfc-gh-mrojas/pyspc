import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from pyspc import *

st.title("Statistical Process Control (SPC) Chart")

a = spc(pistonrings) + cusum() + ewma() + rules()
a.make()
st.write(a.fig)

b = spc(pistonrings) + xbar_sbar() + sbar() + rules()
b.make()
st.write(b.fig)

# This chart still not working
#c = spc(viscosidade) + xmr() + mr() + cusum() + rules()
#c.make()
#st.write(c.fig)

d = spc(plastic) + Tsquare_single() + rules()
d.make()
st.write(d.fig)

e = spc(experiment) + Tsquare()
e.make()
st.write(e.fig)

f = spc(mewma_example) + mewma() + rules()
f.make()
st.write(f.fig)
