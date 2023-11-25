import streamlit as st


def create_quiz():
    # Define the questions and their options
    questions = {
        "What is the capital of France?": {"A": "Paris", "B": "London", "C": "Berlin", "D": "Madrid"},
        "What is 2 + 2?": {"A": "3", "B": "4", "C": "5", "D": "6"},
        "Who wrote 'Hamlet'?": {"A": "Shakespeare", "B": "Dickens", "C": "Chaucer", "D": "Austen"},
        "Which planet is closest to the sun?": {"A": "Earth", "B": "Venus", "C": "Mercury", "D": "Mars"},
        "What is the largest ocean on Earth?": {"A": "Atlantic", "B": "Pacific", "C": "Indian", "D": "Arctic"},
        "Who painted the Mona Lisa?": {"A": "Van Gogh", "B": "Da Vinci", "C": "Picasso", "D": "Rembrandt"},
        "What is the chemical symbol for Gold?": {"A": "Au", "B": "Ag", "C": "Fe", "D": "Cu"},
        "What is the hardest natural substance on Earth?": {"A": "Diamond", "B": "Gold", "C": "Iron", "D": "Ruby"},
        "Which country is known as the Land of the Rising Sun?": {"A": "China", "B": "Australia", "C": "Japan", "D": "India"},
        "What is the longest river in the world?": {"A": "Nile", "B": "Amazon", "C": "Yangtze", "D": "Mississippi"}
    }
    user_responses = {}
    stAnswerlst = []

    # Display each question and its options
    for i, (question, options) in enumerate(questions.items()):
        selected_label = st.radio(question, list(options.keys()), format_func=lambda x: f"{x}: {options[x]}", key=f"question_{i}", index=None)
        user_responses[question] = selected_label
        stAnswerlst.append(selected_label)

    return user_responses, stAnswerlst

def calculate_score(user_responses):
    # Correct answers labeled
    correct_answers = {
        "What is the capital of France?": "A",
        "What is 2 + 2?": "B",
        "Who wrote 'Hamlet'?": "A",
        "Which planet is closest to the sun?": "C",
        "What is the largest ocean on Earth?": "B",
        "Who painted the Mona Lisa?": "B",
        "What is the chemical symbol for Gold?": "A",
        "What is the hardest natural substance on Earth?": "A",
        "Which country is known as the Land of the Rising Sun?": "C",
        "What is the longest river in the world?": "A"
    }

    # Calculate score
    score = sum(1 for question, response in user_responses.items() if response == correct_answers[question])
    return score, correct_answers

def main():
    st.title("Quiz Application")

    # Create the quiz
    user_responses, stAnswerlst = create_quiz()
    # Button to submit responses
    if st.button('Submit Answers'):
        if all(response != "" for response in stAnswerlst):
            # Calculate total score
            total_score,corectans= calculate_score(user_responses)
            st.write(f"Your Total Score: {total_score} out of {len(user_responses)}")
            st.write(f"List of student answer: {stAnswerlst}")
            st.write(f"Corect Answers List: {list(corectans.values())}")
        else:
            st.error("Please answer all questions before submitting.")

if __name__ == "__main__":
    main()
