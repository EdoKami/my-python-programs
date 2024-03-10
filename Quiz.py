class Quiz:
    def __init__(self):
        self.fifth_Grade_questions = {
            "What is the process by which plants make their own food using sunlight?": "photosynthesis",
            'Which planet is known as the "Red Planet"?': "mars",
            "What is the basic unit of life?": "cell",
            "What is the force that pulls objects toward the center of the Earth?": "gravity",
            "Name the three states of matter.": ["liquid", "solid", "gas"],
            "What causes the Earth's seasons?": ["tilt" or "tilt of earth", "axis" or "axis of earth"],
            "Which human body system is responsible for pumping blood throughout the body?": ["nervous", "circulatory"],
            "What is the process by which water changes from a liquid to a gas?": ["evaporation", "vapourisation"],
            "What type of energy does the Sun provide to the Earth?": ["solar energy", "solar"],
            "What is the function of the chlorophyll in plant cells?": "photosynthesis"
        }
        self.fifth_grade_score = 0

    def ask_question(self, question, correct_answer):
        user_answer = input(f"{question} your answer: ").strip().lower()
        correct_answerl = str(correct_answer)
        correct_answerl = [ans.strip().lower() for ans in correct_answer.split(",")]
        return user_answer == correct_answerl or user_answer in correct_answer if isinstance(correct_answer, str) else user_answer in correct_answer

    def run_quiz(self):
        print("Welcome to the Science Quiz")
        print("")
        print("   level-1 (5th grade)")
        print("   level-2 (8th grade)")
        print("   level-3 (9th grade)")

        choose = input("Choose level: ").lower()
        if choose == "1":
            score = 0

            for question, answers in self.fifth_Grade_questions.items():
                if self.ask_question(question, answers):
                    print("Correct!\n")
                    score += 1
                else:
                    print(f"Wrong! The correct answer is {', '.join(answers)}.\n")

            print(f"Quiz completed! Your total score is {score} out of {len(self.fifth_Grade_questions)}.")
        elif choose == "2":
            pass
        elif choose == "3":
            pass
        else:
            print("Wrong choice!!!")


if __name__ == '__main__':
    science_quiz = Quiz()
    science_quiz.run_quiz()
