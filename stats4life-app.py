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
    data=input_df.dropna(axis=1, how='all')
    #filtering columns that starts with specific names and converted into a dataframe
    colsToScale=["Username","ASSIGNMENT", "LAB", "Assignment"]
    assign_df=data[data.columns[data.columns.str.startswith(tuple(colsToScale))]]
    st.write(assign_df)
    
    # lets check the percentage of missing data in each columns present in the data

    no_of_rows = assign_df.shape[0]
    percentage_of_missing_data = assign_df.isnull().sum()
    st.write(percentage_of_missing_data)
    
    #get stats based on assignemtn number
    inp = st.number_input("ASSIGNMENTS NUMBER")
    inp=int(inp)
    x=assign_df.columns
    print(x[inp-1])
    no_of_rows = assign_df.shape[0]
    sum_of_missing_data = assign_df[x[inp-1]].isnull().sum()
    st.write("NUMBER OF STUDENTS WHO DID NOT SUBMIT",sum_of_missing_data)
    
    #Total assignmetns
    assign_user_df =  assign_df[["Username"]]
    assign_user_df["Number of assignments not submitted"] = assign_df.isnull().sum(axis=1)
    st.write(assign_user_df)
    
    #User
    user_input = st.text_input("Name")
    assign_user_df.loc[assign_user_df['Username'] == user_input]
    st.write(assign_user_df)

#     c=['Username',
#         'ASSIGNMENT # 1 [Total Pts: 100 Score] |1344236',
#        'ASSIGNMENT # 2 [Total Pts: 100 Score] |1344237',
#        'ASSIGNMENT # 3 [Total Pts: 100 Score] |1344238',
#        'Assignment # 4 [Total Pts: 100 Score] |1344239',
#        'Assignment # 5 [Total Pts: 100 Score] |1344240',
#        'ASSIGNMENT # 6 [Total Pts: 100 Score] |1344241',
#        'ASSIGNMENT # 7 [Total Pts: 100 Score] |1344242',
#        'ASSIGNMENT # 8 [Total Pts: 100 Score] |1344243',
#        'ASSIGNMENT # 9 [Total Pts: 100 Score] |1344244',
#        'ASSIGNMENT # 10 [Total Pts: 100 Score] |1344245']

#     st.write(input_df[c].isna().sum().rename("No. OF STUDNETS WHO DID NOT SUBMIT THE ASSIGNEMNT"))
#     grouped_df=input_df.groupby('Username')
#     grp=grouped_df.first()
#     st.write(grp.isnull().sum(axis=1).rename("Number of assignments not submitted"))
#     st.write(input_df["ASSIGNMENT # 1 [Total Pts: 100 Score] |1344236"].isna().groupby(input_df['Username']).sum())
#     df = input_df[c[0:user_input]].copy()
#     st.write(df)
#     st.write(input_df[input_df[c[user_input]].isna() == 1]["Username"].rename("STUDNETS NAMES"))
    
                                                 
else:
    st.write("""
# STATS LAB App

This app Give STATS FOR STATS LAB
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
