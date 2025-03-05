import streamlit as st
import random

# 🌟 Streamlit Page Config
st.set_page_config(page_title="Number Guessing Game", page_icon="🎯")

# 🎯 Title
st.title("🎯 Number Guessing Game")
st.write("Guess the number between 1 and 100! 🚀")

# 🎲 Generate Random Number (Session State to keep it fixed)
if 'target_number' not in st.session_state:
    st.session_state.target_number = random.randint(1, 100)
    st.session_state.attempts = 0

# 📝 User Input: Guess the Number
guess = st.number_input("🔹 Enter your guess:", min_value=1, max_value=100, step=1)

# 🚀 Check Guess
if st.button("🔍 Check Guess"):
    st.session_state.attempts += 1
    if guess < st.session_state.target_number:
        st.warning("📉 Too low! Try again.")
    elif guess > st.session_state.target_number:
        st.warning("📈 Too high! Try again.")
    else:
        st.success(f"🎉 Congratulations! You guessed the correct number {st.session_state.target_number} in {st.session_state.attempts} attempts.")
        st.balloons()
        st.session_state.target_number = random.randint(1, 100)
        st.session_state.attempts = 0  # Reset attempts for a new game

# 📌 Footer
st.markdown("---")
st.caption("Powered by Streamlit 🚀 | Happy Coding! 😃")
