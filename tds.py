import streamlit as st

st.title("Find largest number among below three numbers")
n1 = st.number_input("Enter the 1st number")
n2 = st.number_input("Enter the 2nd number")
n3 = st.number_input("Enter the 3rd number")

def largest(n1,n2,n3):
  if n1 > n2 and n1 > n3:
    return n1
  elif n2 > n1 and n2 > n3:
    return n2
  else:
    return n3

if calculate:
  largestn = largest(n1,n2,n3)
  st.write("The largest number is: ",largestn)
