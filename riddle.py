python
# Riddle App with Streamlit

import streamlit as st
import random

# List of riddles and their answers
riddles = [
    {"riddle": "What has keys but can't open locks?", "answer": "A piano"},
    {"riddle": "What starts with an E, ends with an E, but only contains one letter?", "answer": "An envelope"},
    {"riddle": "What is always coming but never arrives?", "answer": "Tomorrow"},
    # Add more riddles here...
]

def play_riddle_game():
    score = 0
    riddle_count = len(riddles)
    random_riddles = random.sample(riddles, riddle_count)

    for i, riddle in enumerate(random_riddles, start=1):
        st.write(f"Riddle {i} of {riddle_count}:")
        st.write(riddle["riddle"])
        user_answer = st.text_input("Your answer: ")

        if st.button("Submit"):
            if user_answer.lower() == riddle["answer"].lower():
                st.write("Correct!")
                score += 1
            else:
                st.write(f"Sorry, the correct answer is {riddle['answer']}")
            st.write("")  # Add a blank line for readability

    st.write(f"Your final score is {score} out of {riddle_count}")

def main():
    st.title("Riddle App")
    st.write("Welcome to the Riddle App!")
    st.write("")

    if st.button("Play"):
        play_riddle_game()

if __name__ == "__main__":
    main()
