from time import sleep 

import numpy as np 
import pandas as pd

import streamlit as st

from transformers import pipeline

@st.cache_data
def load_data(url:str) -> pd.DataFrame:
    return pd.read_csv(url)



df = load_data("https://www.github.com/plotly/datasets/raw/master/uber-rides-data1.csv")

st.dataframe(df)
st.button("Rerun")




@st.cache_resource
def load_model():
    return pipeline("sentiment-analysis")

model = load_model()

text = st.text_input("type some text:")

if text:
    output = model(text)[0]
    st.write(output)




@st.cache_data(ttl=20)
def get_data() -> int:
    sleep(3)
    return 5

st.write(get_data())



@st.cache_data(max_entries=3) # max integer is a upper limit that can be holded in memory, also max integer can be revized with every new input. 
def get_data(some_integer:int) -> np.ndarray:
    sleep(3)
    return some_integer * np.random.randn(1000,2)


some_integer = int(st.number_input("please give me an integer:"))
st.write(get_data(some_integer))




@st.cache_data(max_entries=3) # max integer is a upper limit that can be holded in memory, also max integer can be revized with every new input. 
def get_data(mean:float, std:float) -> np.ndarray:
    sleep(3)
    return mean + std * np.random.randn(1000,2)


mean = float(st.number_input("please give me a mean:",value=0.0))
std = float(st.number_input("please give me a std:",value=1.0))


st.write(get_data(mean, std))


# _std staff
@st.cache_data(max_entries=3) 
def get_data(mean:float, _std:float) -> np.ndarray:
    sleep(3)
    return mean + _std * np.random.randn(1000,2)


mean = float(st.number_input("please give me a mean:",value=0.0))
std = float(st.number_input("please give me a std:",value=1.0))


st.write(get_data(mean, std))



class SomeClass:
    def __init__(self,some_integer:int) -> None:        
        self.some_integer = some_integer

def hash_func(obj:SomeClass) -> int:
    return obj.some_integer


@st.cache_data(hash_func = {SomeClass:hash_func})
def multiply_with(obj:SomeClass, multiplier:int) -> int:
    return obj.some_integer * multiplier


some_integer = int(st.number_input("please give me an integer:"))
multiplier = 3 

my_class = SomeClass(some_integer)
st.write(multiply_with(my_class, multiplier))






