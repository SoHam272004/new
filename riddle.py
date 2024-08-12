# Riddle App

riddles = [
    {"riddle": "What has keys but can't open locks?", "answer": "A piano"},
    {"riddle": "What starts with an E, ends with an E, but only contains one letter?", "answer": "An envelope"},
    {"riddle": "What is always coming but never arrives?", "answer": "Tomorrow"},
    # Add more riddles here...
]

def play_riddle_game():
    score = 0
    for riddle in riddles:
        print(f"Riddle: {riddle['riddle']}")
        user_answer = input("Your answer: ")
        if user_answer.lower() == riddle["answer"].lower():
            print("Correct!")
            score += 1
        else:
            print(f"Sorry, the correct answer is {riddle['answer']}")
        print("")  # Add a blank line for readability
    print(f"Your final score is {score} out of {len(riddles)}")

def main():
    print("Welcome to the Riddle App!")
    print("You will be presented with a series of riddles.")
    print("Type your answer and press Enter.")
    print("Good luck!")
    print("")  # Add a blank line for readability
    play_riddle_game()

if __name__ == "__main__":
    main()
