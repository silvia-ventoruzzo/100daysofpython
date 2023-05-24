class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list
        
    def still_has_questions(self):
        '''
        Check whether there are still questions in the question list.
        '''
        return self.question_number < len(self.question_list)
        
    def next_question(self):
        '''
        Shows the next questions and asks for an answer.
        '''
        question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q{self.question_number}: {question.text} (True/False):")
        self.check_answer(user_answer, question.answer)
    
    def check_answer(self, user_answer, correct_answer):
        '''
        Check whether the user answer is correct and prints text accordingly.
        '''
        if user_answer.lower() == correct_answer.lower():
            print('You got it right!')
            self.score += 1
        else:
            print(f"That's wrong. The correct answer was {correct_answer}.")
        print(f'Your current score is {self.score}/{self.question_number}')
        print('\n')
        