import streamlit as st
import pandas as pd
import numpy as np
import pickle
st.write("""
# STATISTICS FOR LIFE GRADES

STUDNET GRADE ANALYTICS

""")
user_input = st.number_input("NUMBER OF ASSIGNMENTS COMPLETED")
user_input=int(user_input)+1
st.sidebar.header('User Input Features')

st.sidebar.markdown("""
[Example CSV input file](https://raw.githubusercontent.com/dataprofessor/data/master/penguins_example.csv)
""")

# Collects user input features into dataframe
uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
# if uploaded_file is not None:
if uploaded_file is not None:
    input_df = pd.read_csv(uploaded_file)
    st.write(input_df.head())
    st.write(input_df.select_dtypes('object').nunique())
    c=['Username',
        'ASSIGNMENT # 1 [Total Pts: 100 Score] |1344236',
       'ASSIGNMENT # 2 [Total Pts: 100 Score] |1344237',
       'ASSIGNMENT # 3 [Total Pts: 100 Score] |1344238',
       'Assignment # 4 [Total Pts: 100 Score] |1344239',
       'Assignment # 5 [Total Pts: 100 Score] |1344240',
       'ASSIGNMENT # 6 [Total Pts: 100 Score] |1344241',
       'ASSIGNMENT # 7 [Total Pts: 100 Score] |1344242',
       'ASSIGNMENT # 8 [Total Pts: 100 Score] |1344243',
       'ASSIGNMENT # 9 [Total Pts: 100 Score] |1344244',
       'ASSIGNMENT # 10 [Total Pts: 100 Score] |1344245']

    st.write(input_df[c].isna().sum().rename("No. OF STUDNETS WHO DID NOT SUBMIT THE ASSIGNEMNT"))
    grouped_df=input_df.groupby('Username')
    grp=grouped_df.first()
    st.write(grp.isnull().sum(axis=1).rename("Number of assignments not submitted"))
    st.write(input_df["ASSIGNMENT # 1 [Total Pts: 100 Score] |1344236"].isna().groupby(input_df['Username']).sum())
    df = input_df[c[0:user_input]].copy()
    st.write(df)
    st.write(input_df[input_df[c[user_input]].isna() == 1]["Username"].rename("STUDNETS NAMES"))
    
                                                 
else:
    st.write("""
# Penguin Prediction App

This app predicts the **Palmer Penguin** species!

Data obtained from the [palmerpenguins library](https://github.com/allisonhorst/palmerpenguins) in R by Allison Horst.
""")
 


# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
# tickerSymbol = 'GOOGL'
#get data on this ticker
# tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
# tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

# st.write("""
# ## Closing Price
# """)
# st.line_chart(tickerDf.Close)
# st.write("""
# ## Volume Price
# """)
# st.line_chart(tickerDf.Volume)
