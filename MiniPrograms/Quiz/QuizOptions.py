# Module to contains options of all quiz questions
question_option = [
    """
    1.  largest railway station
    2.	highest railway station
    3.	longest railway station
    4.	None of the above""",

    """
    1.  Behavior of human beings
    2.	Insects
    3.	The origin and history of technical and scientific terms
    4.	The formation of rocks""",

    """
    1.  Asia
    2.	Africa
    3.	Europe
    4.	Australia""",

    """
    1.  Junagarh, Gujarat
    2.	Diphu, Assam
    3.	Kohima, Nagaland
    4.	Gangtok, Sikkim""",

    """
    A.  Physics and Chemistry
    B.	Physiology or Medicine
    C.	Literature, Peace and Economics
    D.	All of the above"""
]


def quiz_options(question_number):
    print(question_option[question_number])
