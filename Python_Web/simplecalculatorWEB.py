import streamlit as st


st.title("My Simple Calculator")
st.subheader("This is my calculator app")


st.number_input(label="Add a number", placeholder="Type here...",
               key="number1", value=None)

st.number_input(label="Add a number", placeholder="Type here...",
               key="number2", value=None)
result = ""
col1, col2, col3, col4 = st.columns(4)
with col1: 
     add_button = st.button("Addition (+)", key="add")
with col2:
    sub_button = st.button("Subtraction (-)", key="sub")
with col3:
    multi_button = st.button("Multiplication(*)", key="multi")
with col4:
    div_button = st.button("Division(/)", key="div")
    st.markdown("</div>", unsafe_allow_html=True)

if add_button:
    
    result = st.session_state.number1 + st.session_state.number2
    
if sub_button:
    result =  st.session_state.number1 - st.session_state.number2
    
if multi_button:
    result =  st.session_state.number1 * st.session_state.number2

if div_button:
    if st.session_state.number2 == 0:
        
        st.markdown(f"<h2 style='font-size: 50px; color: white;'>You can not divide by 0</h2>", unsafe_allow_html=True)
    else:
        result =  st.session_state.number1 / st.session_state.number2


st.markdown(f"<h1 style='font-size: 50px; color: white;'>The result is: {result}</h1>", unsafe_allow_html=True)

st.write(st.session_state)
    