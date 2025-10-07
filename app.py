import streamlit as st

st.title('Powerful Calculator')
st.write('Enter number to calculate poers of square, cube & fifth')

n = st.number_input('enter integer', value=1, step=1)

square = n**2
cube = n**3
fifth = n**5

st.write(f'square of {n} is: {square}')
st.write(f'cube of {n} is: {cube}')
st.write(f'fifth of {n} is: {fifth}')