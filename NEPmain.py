import json
from difflib import get_close_matches
import time
import random

def load_knowledge_base(file_path: str) -> dict:
    try:
        with open(file_path, 'r') as f:
            data: dict = json.load(f)
        return data
    except (json.JSONDecodeError, FileNotFoundError):
        # Handle the case where the file is empty or not found
        return {"questions": []}

def save_knowledge_base(file_path: str, data: dict):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2)

def find_best_match(user_question: str, questions: list[str]) -> str | None:
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None

def get_answer_for_question(question: str, knowledge_base: dict) -> str | None:
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            if isinstance(q["answer"], list):
                return random.choice(q["answer"])
            else:
                return q["answer"]
    return None

def chat_bot(file_path: str):
    knowledge_base: dict = load_knowledge_base(file_path)

    while True:
        user_input: str = input("You: ")

        if user_input.lower() == "quit":
            break
        elif user_input.lower() == "bye":
            print("NEPBot: Bye, have a nice day")
            time.sleep(1)
            break
        elif not user_input.strip():
            print("NEPBot: Please enter a valid input.")
            continue

        best_match: str | None = find_best_match(user_input, [q["question"] for q in knowledge_base["questions"]])

        if best_match:
            answer: str = get_answer_for_question(best_match, knowledge_base)
            print(f"NEPBot: {answer}")
        else:
            print("NEPBot: I don't know the answer. Can you teach me?")
            new_answer: str = input("Type the answer or 'skip' to skip: ")

            if new_answer.lower() != "skip":
                knowledge_base["questions"].append({"question": user_input, "answer": new_answer})
                save_knowledge_base(file_path, knowledge_base)
                print("NEPBot: Thank you, I learned a new response!")

if __name__ == "__main__":
    knowledge_base_path = "D:\\Ravi's\\Python project\\Python Programs\\knowledge_base.json"
    chat_bot(knowledge_base_path)
