import streamlit as st
import pandas as pd
import numpy as np

data = {
    'Round': [1, 2, 3, 4, 5],
    'Level': np.random.randint(1, 100, 5)
}

df = pd.DataFrame(data)
st.title("Welcome to Week 5 Streamlit App")
st.write(df)
with st.container(border=True):
    round = st.select_slider(
        "Select number of rounds to display",
        options=[1, 2, 3, 4, 5],
    )
    st.write (f"You selected {round} rounds.")
st.line_chart(df.head(round),y='Level',x = 'Round')
