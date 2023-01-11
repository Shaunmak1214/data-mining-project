from re import S
import pandas as pd
import streamlit as st
import numpy as np

def app():
    st.write("# Primary Findings")
    st.write("The dataset we been used in this project is called **'LaundryData\_2021\_T2.csv'**. After we read the dataset, there are 4000 rows and 22 columns. Below are some details of the Data :")
    st.image('Dataframe.png')
    st.image('Dataframe_dtypes.png')
    st.image('Dataframe_describe.png')
    st.image('Dataframe_describe1.png')
    st.write("Please use the navigation bar to navigate between different parts of the project!")

    #clusters
    st.write("# How can we cluster the customers? ")
    st.write("## K Means Clustering ")
    st.write('We applied K-Means clustering to the longitude and latitude data points, both of which had 4000 unique values, it means every customer had different sets of location data. Which helped us cluster them into 3 different sets, which means the customers in that shop all came from 3 distinct locations.')
    st.write('The clustering technique we used for our analysis is **K-Means Clustering**, we attempted to make use of the location data to cluster the data.')
    st.image(['Coordinate.png','K-Means.png'])

    st.write("# What kinds of associations can we find in the dataset?")
    st.write("## Apriori Algorithm")
    st.write('The apriori algorithm is a set of procedures that must be followed in order to determine the most frequent itemset in a database. We applied this technique and found that there are 50 rules in the data set and the rules had confidence of 0.10 to around 0.25 for most rules. Other than this, there are only 3 rules which are have support more than 0.0045, confidence more than 0.2, lift more than 3 and length more than 2.')
    st.write('We used **Apriori Algorithm**, for our purpose.')
    st.image(['Apriori.png', 'Apriori1.png'])
    st.image(['Apriori2.png', 'Apriori3.png', 'Apriori4.png'])

    st.write("# How many missing data points in the datasets?")
    st.write('We looked for missing values in each column. Among the 22 columns, 16 of the columns had missing data. Among the 16 columns only 4 columns had missing data in more than 200 rows. Which none of the columns had missing value in more that 5\% of the rows. After this exploration, we decided to impute the data using SimpleImputer, which is described in the next section.')
    st.image(['MissingData.png'])

    st.write("# How can we handle the missing values?")
    st.write('For the missing values, we have used the strategy called \'most_frequent\' from SimpleImputer. It will replace missing values using the most frequent value along each column. It can be used with strings or numeric data. If there is more than one such value, only the smallest is returned. The reason to choose this methods was because the number of missing columns were really low (less than 5%)')
    st.image(['Imputation.png', 'Imputation1.png'])

    st.write("# What were the ages of customers that visited the laundry shop?")
    st.write('The box plot shows that large majority of the customers in the shop age between 30 to 50 years old and the median age of the customers is around 40. Majority of the customers are middle aged people. There are no outliers in the Age\_Range and the data is normally distributed. We used boxplots because it is able to show us the distribution of data based on a five number summary (“minimum”, first quartile (Q1), median, third quartile (Q3), and “maximum”)')
    st.image(['Histogram.png', 'Boxplot_1.png'])

    st.write('We can also see the same data apparent in our histogram plot of the Age\_Range variable. There are only a little over 200 people out of 4000 data points who are either less that 20 years old or more than 60 years old.')

    st.write('# What is the correlation between variables?')
    st.write('The heatmap below shows us that the correlation between variables. Inside the diagram, it has shown us that the longitude has a very weak correlation with Age_Range and latitude. Other than that, the other variables has no correlation with each other.')
    st.image('Correlation.png')
    
    st.write('# Is there any relationship between basket size and race?')
    st.write('In the figure below, we have used the heatmap to show the correlation between basket size and race. The heatmap shown that the correlation between backet size and race is 0.05 which is very weak positive correlation.')
    st.image('Race_vs_Size.png')
    
    st.write('# What types of customers will likely to choose Washer No. 3 and Dryer No. 10')
    st.write('In the figure below, we have listed down the appearance of customers that would likely to choose Washer No. 3 and Dryer No. 10. There are 214 customers that choose Washer No. 3 and Dryer No. 10 and we have listed down the most common appearances in the figure below.')
    st.image('Customers.png')

