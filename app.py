import streamlit as st
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
#title of the application
st.title("CSV DATA ANALYZER")
#content below title
st.write("welcome to my application❤️,here you can upload and analyze the CSV file")
data={
    "Name":['A','B','C','D','E'],
    "Age":[20,18,19,19,20],
    "salary":[30000,35000,40000,45000,50000],
    "city":['sln','lucknow','jhansi','pbh','lucknow']
}
df=pd.DataFrame(data)
df.to_csv("sampledata.csv")



def load_csv():
    return st.file_uploader("Choose a CSV file", type="csv")



uploaded_file = load_csv()

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    if 'Unnamed: 0' in df.columns:
        df.drop('Unnamed: 0', axis=1, inplace=True)

    
    
    st.write(df)
    
    st.write("(rows,columns)=",df.shape)
    st.write("column names")
    st.write(df.columns)
    
    options=["summary statistics","filter data","search data","chart"]
    choice=st.selectbox("select analysis type",options)
    st.write(f"according to {choice} analysis type,brief analysis is provided below:")
    if choice=="summary statistics":
                 numeric_data=df.select_dtypes(include="number") 
                 newdf=numeric_data 
                 st.dataframe(newdf.describe())
        
                # st.write(f"mean of the data :{newdf.mean()}")
                # st.write(f"median of the data:{newdf.median()}")
                 #st.write(f"maximum value of dataset:{newdf.max()}")
                 #st.write(f"minimum value of dataset:{newdf.min()}")
    elif choice=="filter data":
            
                numeric_dt=df.select_dtypes(include="number")
                df2=numeric_dt
                st.write(df2)
                
                
                
                choice=st.selectbox("choose the column",df2.columns)
                selected_column=choice
                min_value=df2[choice].min()
                max_value=df2[choice].max()
                st.write(min_value)
                st.write(max_value)
                slider_value= st.slider(choice,min_value,max_value)
                filtered_df = df[df[selected_column] >= slider_value]
                st.write("filtered dataframes",filtered_df)
    elif choice=="search data":
        name=st.text_input("enter your name")
        search_clicked=st.button("search")
        if search_clicked:
         st.write("searching for",name)
            
         search_result = df[df["Name"] == name]
         st.dataframe(search_result)
    elif choice == "chart":

        numeric_dt = df.select_dtypes(include="number")

        selected_column = st.selectbox(
        "Choose column for chart",
        numeric_dt.columns
        )
 
        chart_type = st.radio(
        "Choose chart type",
        ["Line Chart", "Bar Chart"]
     )

        if st.button("Generate Chart"):

            if chart_type == "Line Chart":
               st.line_chart(df[selected_column])

            elif chart_type == "Bar Chart":
               st.bar_chart(df[selected_column])
    
        
        
        
            
                
                
                        
                
                
                