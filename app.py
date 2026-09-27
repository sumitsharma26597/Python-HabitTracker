import streamlit as st

st.title("Habit Tracker")

st.write("Track your daily habits and stay consistent!")

name = st.text_input("Enter your name: ")

if name:
    st.success(f"Welcome {name}.")
    habit = st.text_input("Enter a habit: ")

    if st.button("Add Habit"):
        if habit:
            st.write(f"Added habit: {habit}")
        else:
            st.warning("Please enter a habit.")