# Module to contain all quiz questions

question_list = [
    "Grand Central Terminal, Park Avenue, New York is the world's",
    "Entomology is the science that studies",
    "Eritrea, which became the 182nd member of the UN in 1993, is in the continent of",
    "Ghahramani sanctuary is located at",
    "For which of the following disciplines is Nobel Prize awarded?"
]

question_answer = [1, 2, 2, 2, 4]

question_list_size = len(question_list)

def list_size():
    return question_list_size

def quiz_question(question_number):
    print(f"Ques {question_number + 1}: {question_list[question_number]}")

def quiz_answers(question_number):
    return question_answer[question_number]
