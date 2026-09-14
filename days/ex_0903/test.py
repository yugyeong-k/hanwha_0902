import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import time
import matplotlib.pyplot as plt
from numpy.random import default_rng as rng

'''
# Hello,
'''

st.write("*World!* :sunglasses:")

def stream_data():
    df = pd.DataFrame({"first": [1,2], "second": [10,20],})

    yield df 
    time.sleep(0.30)

    df = pd.DataFrame(rng(0).standard_normal((200,3)), columns=["A","B","C"])
    chart = (alt.Chart(df) .mark_square() .encode(x="A", y="B", size="C", color="C", tooltip=["A","B","C"]))

    yield chart

    arr = np.random.normal(3,3, size=20)
    fig, ax = plt.subplots()
    ax.hist(arr, bins=10)

    yield fig

if st.button("clik"):
    st.write_stream(stream_data)

st.markdown("*Hello* **Hello** ***Hello***")
st.markdown(''':red[H] :orange[E] :green[L] :blue[L] :violet[O] :rainbow[WORLD] :red-background[:tulip:]''')
multi = '''HELLO

WORLD'''
st.markdown(multi)

md = st.text_area('text',"")
st.markdown(md)

st.caption("caption")
st.badge("New")
st.badge("Success", color="orange")
st.markdown(":red-badge[🐷 pig]")
st.slider("slider", 0, 100, (0))