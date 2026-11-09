class Question:
    def __init__(self, question, options, correct_answer):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer

    def display_question(self):
        print("\n" + self.question)

        for option in self.options:
            print(option)


class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def start_quiz(self):
        for question in self.questions:
            question.display_question()

            answer = input("Enter your answer (A/B/C/D): ").upper()

            if answer == question.correct_answer:
                print("Correct answer!")
                self.score += 1
            else:
                print("Wrong answer!")
                print("Correct answer:", question.correct_answer)

        self.display_result()

    def display_result(self):
        total = len(self.questions)

        print("\n===== QUIZ RESULT =====")
        print("Total Questions:", total)
        print("Correct Answers:", self.score)
        print("Wrong Answers:", total - self.score)
        print("Final Score:", self.score, "/", total)


# Creating questions
q1 = Question(
    "1. Which language is used for Python programming?",
    ["A. Java", "B. Python", "C. C++", "D. HTML"],
    "B"
)

q2 = Question(
    "2. Which keyword creates a class in Python?",
    ["A. function", "B. object", "C. class", "D. define"],
    "C"
)

q3 = Question(
    "3. Which function displays output in Python?",
    ["A. input()", "B. print()", "C. display()", "D. output()"],
    "B"
)

# Creating quiz
questions = [q1, q2, q3]

quiz1 = Quiz(questions)

# Starting quiz
quiz1.start_quiz()
