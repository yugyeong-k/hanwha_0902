import streamlit as st

from days import day01, day02, day03
menu = st.sidebar.selectbox(
    label="Select a day",
    options=["Day 01", "Day 02", "Day 03"]
)


pages = {
    "Day 01": day01.show,
    "Day 02": day02.show,
    "Day 03": day03.show,
   }

pages[menu]()