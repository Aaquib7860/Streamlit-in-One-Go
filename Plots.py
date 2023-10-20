import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data_chart = pd.DataFrame(np.random.randn(20,3), columns = ['Line-1', 'Line-2', 'Line-3'])


st.header('1. Chart with Random Numbers')
st.subheader('1.1 Line Chart')
st.line_chart(data_chart)

st.subheader('1.2 Area Chart')
st.area_chart(data_chart)

st.subheader('1.3 Bar Chart')
st.bar_chart(data_chart)

st.header('2. Visualization using Matplotlib & Seaborn')
st.subheader('2.1 Loding DataFaram')
df = pd.read_csv('iris.csv')
st.dataframe(df)

st.subheader('2.2 Bar Graph using Matplotlib')
fig = plt.figure(figsize = (15,8))
df['species'].value_counts().plot(kind = 'bar')
st.pyplot(fig)

st.subheader('2.3 Distribution plot using Seaborn')
fig = plt.figure(figsize = (15,8))
sns.distplot(df['sepal_length'])
st.pyplot(fig)

st.header('3. Multiple Graphs in one Column')
col1, col2 = st.columns(2)
with col1:
    col1.header = 'KDE = False'
    fig1 = plt.figure(figsize = (6,5))
    sns.distplot(df['sepal_length'], kde = False)
    st.pyplot(fig1)
with col2:
    col1.header = 'Hist = False'
    fig2 = plt.figure(figsize = (6,5))
    sns.distplot(df['sepal_length'], hist = False)
    st.pyplot(fig2)

st.header('4. Changing the Style')
col1, col2 = st.columns(2)
with col1:
    col1.header = 'hist = False'
    fig1 = plt.figure(figsize = (6,5))
    sns.set_style('darkgrid')
    sns.set_context('notebook')
    sns.distplot(df['sepal_length'], hist = False)
    st.pyplot(fig1)
with col2:
    col1.header = 'Hist = False'
    fig2 = plt.figure(figsize = (6,5))
    sns.set_theme(style = 'darkgrid', context = 'notebook')
    sns.distplot(df['sepal_length'], hist = False)
    st.pyplot(fig2)

st.header('5. Exploring Different Graphs')

st.subheader('5.1 scatter-plot')
fig,ax = plt.subplots(figsize = (10,10))
ax.scatter(*np.random.random(size = (2,100)))
st.pyplot(fig)

st.subheader('5.1 Count-plot')
fig = plt.figure(figsize = (10,5))
sns.countplot(data = df, x = 'species')
st.pyplot(fig)

st.subheader('5.1 Box-plot')
fig = plt.figure(figsize = (10,5))
sns.boxplot(data = df, x = 'species', y = 'petal_length')
st.pyplot(fig)

st.subheader('5.1 violin-plot')
fig = plt.figure(figsize = (10,5))
sns.violinplot(data = df, x = 'species', y = 'petal_length')
st.pyplot(fig)
