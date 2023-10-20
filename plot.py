import numpy as np
import pandas as pd
import altair as alt
import streamlit as st
import plotly.express as px
import plotly.figure_factory as ff

# Altair Scatter plot
st.header('1. Altair Scatter Plot')
chart_data = pd.DataFrame(np.random.randn(500,5), columns = ['a','b','c','d','e'])
chart = alt.Chart(chart_data).mark_circle().encode(x = 'a', y = 'b', size = 'c',
                                                tooltip = ['a','b','c','d','e'])
st.altair_chart(chart)


# Interective Line Plot
st.header('2. Interective Line Plot')
st.subheader('2.1 Line Chart')
df = pd.read_csv('C:/Users/Aaquib/Desktop/Programming of data science/Streamlit/lang_data.csv')
lang_list = df.columns.tolist()
lang_choices = st.multiselect('Choose your Language', lang_list)
new_df = df[lang_choices]
st.line_chart(new_df)

st.subheader('2.1 Area Chart')
st.area_chart(new_df)


# Data-Visualization with plotly
st.header('3. Data-Visualization with Plotly')
st.subheader('3.1 Displaying the Dataset')
df = pd.read_csv('C:/Users/Aaquib/Desktop/Programming of data science/Streamlit/tips.csv')
st.dataframe(df.head())

st.subheader('3.2 Pie Chart')
fig = px.pie(df, values = 'total_bill', names = 'day')
st.plotly_chart(fig)

st.subheader('3.3 Pie Chart with parameters')
fig = px.pie(df, values = 'total_bill', names = 'day', opacity = .7, color_discrete_sequence = px.colors.sequential.RdBu)
st.plotly_chart(fig)

st.subheader('3.4 Histogram')
x1 = np.random.randn(100)
x2 = np.random.randn(100)
x3 = np.random.randn(100)

hist_data = [x1,x2,x3]
group_label = ['Group - 1', 'Group - 2', 'Group - 3']
fig = ff.create_distplot(hist_data, group_label, bin_size = [.1,.25, .5])
st.plotly_chart(fig)

# Distribution Plot
