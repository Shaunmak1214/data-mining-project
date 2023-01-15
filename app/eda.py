from re import S
import pandas as pd
import streamlit as st
import numpy as np

def app():
    st.title("Explanatory Analysis of the Dataset")
    dataset = pd.read_csv('./dataset.csv')
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Overview", "Missing Values & Cleaning", "Association", "Correlation", "Likelihood of chooing certain washer or dryer"])
    
    with tab1:
        st.subheader("Overview")
        dataset = pd.read_csv('./dataset_w_weather&rwi&city.csv')
    
        st.write("#### The Dataset that we're working with:")
        st.dataframe(dataset)
        st.write("The dataset contains",len(dataset), "rows and", len(dataset.columns), "columns")
        st.write("*The dataset provided here has been cleaned and merged with the external datasets*")
        st.write("Head over to the [External Dataset](/External_Datasets) page to see what sorts of external datsets we used")
        
        st.write("##### Datatypes of the datasets")
        st.write(dataset.dtypes)
        
        st.write("##### Description of the datasets")
        st.write(dataset.describe(include='object'))
        
        st.write("##### Unique values in each column")
        st.write(dataset.nunique())
        
        # plot location map
        st.write("##### Location of the customers")
        st.map(dataset)
    
    with tab2:
        st.subheader("Cleaning the datasets")

        st.write("First of all let's plot the nan values in the dataset")
        # display image 
        st.image('./nanvalues_plot.png')
        
        st.write("##### Since the dataset is quite large, we can't just drop the rows with nan values. So we'll have to impute the values. We'll be using the SimpleImputer to impute the values.")
        st.write("##### But just before we do that, for the columns Race, Gender, latitude and longitude, since they are columns that are very important, without them we can't really do much, we'll just drop the rows with nan values for these columns.")
        st.write("#### Dropping the rows with nan values")
        st.code('''p_df = p_df.dropna(subset=['Race', 'Gender', 'latitude', 'longitude'], inplace=False)''')
        
        st.write("#### Imputing the values")
        st.code('''imp = SimpleImputer(missing_values=np.nan, strategy='most_frequent')''')
        
        st.write("#### After imputing the values, we can see that there are no more nan values in the dataset")
        st.image('./after_imputing.png')
        st.write("*The data is then saved as a csv file and ready for exploration*")
    
    with tab3:
        association_rules_csv = pd.read_csv('./association_rules.csv')
        st.subheader("Association Rules")
        st.write("Association rules are a type of frequent itemset mining that is used to find relationships between variables in large databases. Association rules are if-then statements that show how frequently an itemset appears in a database. For example, if a customer buys a certain item, they are likely to buy another item. Association rules are used to find relationships between variables in large databases. Association rules are if-then statements that show how frequently an itemset appears in a database. For example, if a customer buys a certain item, they are likely to buy another item.")
        st.write("##### The association rules that we found are as follows:")
        st.dataframe(association_rules_csv)
        st.write("*The association rules are then visualized using the apyori library*")
        st.write("")
        st.write("As you can see in the table, the amount of support, confidence and lift are quite low. This means that the rules are not very strong. We belive this is because the dataset is quite large and there are many different combinations of items. So it is quite hard to find strong rules.")

    with tab4:
        st.subheader("Correlation")
        st.write("Correlation is a statistical measure that expresses the extent to which two variables are linearly related (meaning they change together at a constant rate). Correlation is a statistical measure that expresses the extent to which two variables are linearly related (meaning they change together at a constant rate).")
        st.write("##### The correlation between the numerical columns are as follows:")
        st.image('./correlation_matrix.png')
        st.write("As you can see, the correlation between the numerical columns are quite low. This means that there is no strong correlation between the columns. We belive this is because the dataset is quite large and there are many different combinations of items. So it is quite hard to find strong rules.")
        st.write("*Each of the data points which do not contain numerical values are label encoded and then the correlation is plotted*")
        
        st.write("")
        st.write("")
        
        st.write("#### Finding more relationships between variables")
        
        st.image('./weather_distribution.png')
        st.write("As you can tell with the distribution plot, the customer counts spikes when the weather is good. This means that the customers are more likely to use the laundry service when the weather is good.")
        st.write("")
        
        st.image('./rwi_distribution.png')
        st.write("With the above rwi distirbution we see two peaks are from 75 - 140, thus we can lighly conclude that the larger the rwi, the more likely the customer will use the laundry service.")
        st.write("")
        
        st.image('./Coordinate.png')
        st.write("The above scatter plot shows a distribution of the coordinates of the customers, which will be useful to train our clustering model later on.")
        st.write("")
        
        st.image('./relationship-between-race-and-time.png')
        st.write("The above plot shows the relationship between race and time,for instance, we can see that chinese customers are more likely to use the laundry service during the night, while the malays tend to use the laundry service in the morning.")
        st.write("")
        
        st.image('./Distplot of Age_Range.png')
        st.write("The above plot shows the distribution of the age range of the customers, the distribution is quite normal, with the range of 20-60.")
        st.write("")
        
    with tab5:
        st.subheader("Likelihood of choosing certain washer or dryer")
        st.write("To anwser the question, we first need to filter out the rows that contain the washer or dryer that we're interested in. Then we can find the likelihood of choosing certain washer or dryer by selected the most frequent value.")
        
        st.write("")
        st.write("##### The likelihood of choosing certain washer or dryer are as follows:")
        
        st.code('''
                User who are likely to use washer No2, and dryer No3

Race: malay
Gender: male
Body_Size: thin
Age_Range: 60.0
With_Kids: yes
Kids_Category: young
Basket_Size: small
Basket_colour: yellow
Attire: traditional
Shirt_Colour: yellow
shirt_type: short_sleeve
Pants_Colour: yellow
pants_type: short
Wash_Item: clothes

                ''')
        

    st.write(" ")
    st.markdown('''Made with ❤️ by **TDS3301 Group 30** ''')