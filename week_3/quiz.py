def display_question(question):
    print("\n" + question["question"])

    for option in question["options"]:
        print(option)


def validate_answer(answer):
    return answer.upper() in ["A", "B", "C"]


def check_answer(answer, correct_answer):
    return answer.upper() == correct_answer


def update_score(score, correct):
    if correct:
        score += 1
    return score


def display_results(score, total):
    percentage = (score / total) * 100

    print("\nCorrect answers:", score)
    print("Incorrect answers:", total - score)
    print("Final score:", score, "/", total)
    print("Percentage:", percentage, "%")

    if percentage >= 80:
        print("Result: Excellent")
    elif percentage >= 50:
        print("Result: Good")
    else:
        print("Result: Keep practicing")


def play_quiz():
    questions = [
        {
            "question": "1. Which language are we learning?",
            "options": ["A. Python", "B. HTML", "C. CSS"],
            "answer": "A"
        },
        {
            "question": "2. Which symbol starts a comment in Python?",
            "options": ["A. //", "B. #", "C. &"],
            "answer": "B"
        },
        {
            "question": "3. Which type stores True or False?",
            "options": ["A. str", "B. int", "C. bool"],
            "answer": "C"
        },
        {
            "question": "4. Which keyword defines a function?",
            "options": ["A. def", "B. for", "C. if"],
            "answer": "A"
        },
        {
            "question": "5. Which loop can repeat through a list?",
            "options": ["A. if", "B. for", "C. return"],
            "answer": "B"
        }
    ]

    score = 0

    for question in questions:
        display_question(question)

        answer = input("Enter A, B, or C: ")

        while not validate_answer(answer):
            print("Invalid option. Try again.")
            answer = input("Enter A, B, or C: ")

        correct = check_answer(answer, question["answer"])

        if correct:
            print("Correct!")
        else:
            print("Incorrect.")

        score = update_score(score, correct)

    display_results(score, len(questions))


while True:
    play_quiz()

    again = input("\nPlay again? (yes/no): ").lower()

    if again != "yes":
        print("Thank you for playing!")
        break