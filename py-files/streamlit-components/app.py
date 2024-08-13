import streamlit as st
import pandas as pd 
import numpy as np

"""
### block comments

you can use python's block comment syntax in order to put some text on your app 
using markdown 


* Bullet point
* Bullet point 2
* Bullet point 3


1. Enumerate 1
2. Enumerate 2
3. Enumerate 3

"""


df = pd.DataFrame({
    'first column': [1, 2, 3, 4], 
    'second column': [10, 20, 30, 40]})

df



st.write("A magnical method to write different types on screen.")

st.write(df)
st.table(df)


st.write("you can use streamlit to draw charts and maps.")


chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
st.line_chart(chart_data)


map_data =pd.DataFrame(
    np.random.randn(1000,2)/[50,50]+[37.76, -122.4],
    columns=['lat', 'lon'])


st.map(map_data)


st.write("### streamlit widgets:")


st.write("### slider")

slider = st.slider(
    label="number x",
    min_value=1,
    max_value=100,
    value=3,
    step=1
)





dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
st.table(dataframe)



chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)






map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)






x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)





st.text_input("Your name", key="name")

# You can access the value at any point with:
st.session_state.name




if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data






df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option




# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)








left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")