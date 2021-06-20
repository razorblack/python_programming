import QuizQuestions as ques
import QuizOptions as option

user_choice = input("Do you want to play the Quiz Game \nEnter 'y' for Yes and 'n' for no \n")

if user_choice == 'n' or user_choice == 'N':
    print("I hope you'll change your mind in next turn")
    exit(1)

elif user_choice == 'y' or user_choice == 'Y':
    score = 0
    print("Quiz is started! Give answers.")
    for i in range(0, ques.list_size()):
        ques.quiz_question(i)
        option.quiz_options(i)
        user_answer = int(input("Enter your answer: "))

        if user_answer == ques.quiz_answers(i):
            score += 1

    print(f"Quiz Completed! Your final score is {score}")
    print("Thank you! for playing the quiz")

else:
    print("Please! Enter valid choice. And restart again.")
