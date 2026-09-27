import streamlit as st

st.title("Habit Tracker")

st.write("Track your daily habits and stay consistent!")

name = st.text_input("Enter your name: ")

if name:
    st.success(f"Welcome {name}.")

    # Create habits list only once
    if "habits" not in  st.session_state:
        st.session_state.habits = []


    habit = st.text_input("Enter a habit: ")

    if st.button("Add Habit"):
        if habit:
            st.session_state.habits.append(habit)
        else:
            st.warning("Please enter a habit.")

    st.subheader("Your Habits:")

    for habit in st.session_state.habits:
        st.write(f"{habit}")