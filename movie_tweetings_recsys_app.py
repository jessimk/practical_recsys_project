
import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_json(
    "https://raw.githubusercontent.com/jessimk/practical_recsys_project/main/top10charts.json")

chosen_list = st.selectbox(
        "Choose a List", list(df.columns),index=28)

data=df[chosen_list]['movie_title']

data=pd.DataFrame(data, index=['Title']).T
data.index=np.arange(1,11,1)


st.title('🍿 MovieTweetings Recommendations!')
st.markdown('Movie recommendations are made using recent MovieTweetings ratings with a rating of 6 or higher.')

st.markdown('MovieTweetings is a dataset of Twitter movie reviews: https://github.com/sidooms/MovieTweetings')

st.write("### "+chosen_list+" Movies You Should Watch!", data)
