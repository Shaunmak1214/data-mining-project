from re import S
import pandas as pd
import streamlit as st
import numpy as np

def app():
    st.write("# Feedforward Network Classification")
    st.write("In many practical applications, feed-forward neural networks are the most popular and commonly used model. They go by a variety of names, including 'multilayer perceptrons' (MLP). Feed-forward neural networks are used to learn the relationship between independent variables that act as network inputs and dependent variables that function as network outputs. This is the reason why we choose to use Feedforward Neural Network.")
    st.write("We used the following parameters in the models for Num_of_Buckets - ")
    data = {
        "layers" : [3, 3],
        "nodes" : [
            '(32, 16, 3)',
            '(16, 8, 3)'
        ],
        "activation" : [
            '(Sigmoid, Sigmoid, Softmax)',
            '(RelU, RelU, Softmax)'
        ]
    }
    df = pd.DataFrame(data=data)
    st.table(df)
    st.write("Experiment 1: Sigmoid")
    st.image(['Baskets_NN_Accuracy_sigmoid.png', 'Baskets_NN_Loss_sigmoid.png'])

    st.write("Experiment 2: RelU")
    st.image(['Baskets_NN_Accuracy_relu.png', 'Baskets_NN_Loss_relu.png'])

    st.write("We used the following parameters in the models for Age_Range - ")

    st.table(df)
    st.write("Experiment 1: Sigmoid")
    st.image(['Age_NN_Accuracy_sigmoid.png', 'Age_NN_Loss_sigmoid.png'])

    st.write("Experiment 2: RelU")
    st.image(['Age_NN_Accuracy_relu.png', 'Age_NN_Loss_relu.png'])

