# QUIZ GAME
# Provided was the data and solutions after you've tried solving the project yourself

from day17_quiz_game_project.question_model import Question
from day17_quiz_game_project.data import question_data
from day17_quiz_game_project.quiz_brain import QuizBrain

question_bank = [Question(text=x['text'], answer=x['answer']) for x in question_data]

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f"You're final score was: {quiz.score}/{quiz.question_number+1}")