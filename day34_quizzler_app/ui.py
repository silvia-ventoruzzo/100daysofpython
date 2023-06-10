import tkinter
import os
from quiz_brain import QuizBrain

os.chdir('day34_quizzler_app/')

THEME_COLOR = "#375362"

class QuizInterface:
    
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        
        self.window = tkinter.Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.score_label = tkinter.Label(text='Score: 0', 
                                         bg=THEME_COLOR, 
                                         fg='white',
                                         font=('Arial'))
        self.score_label.grid(row=0, column=1)
        
        self.canvas = tkinter.Canvas(width=300, height=250, 
                                     bg='white', highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125,
                                                     width=280,
                                                    #  text='Question',
                                                     fill=THEME_COLOR,
                                                     font=('Aria', 20, 'italic'))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)
        self.get_next_question()
        
        # Buttons
        true_image = tkinter.PhotoImage(file='images/true.png')
        self.true_button = tkinter.Button(image=true_image, 
                                          highlightbackground=THEME_COLOR, highlightthickness=0,
                                          command=self.true_input)
        self.true_button.grid(row=2, column=0)
        
        false_image = tkinter.PhotoImage(file='images/false.png')
        self.false_button = tkinter.Button(image=false_image, 
                                           highlightbackground=THEME_COLOR, highlightthickness=0,
                                           command=self.false_input)
        self.false_button.grid(row=2, column=1)
        
        self.window.mainloop()
        
    def get_next_question(self):
        self.canvas.configure(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f'Score: {self.quiz.score}')
            next_question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=next_question_text)
        else:
            self.canvas.itemconfig(self.question_text,
                                   text=f"You've reached the end of the quiz\n You're final score is: {self.quiz.score}/{len(self.quiz.question_list)}")
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')
        
    def true_input(self):
        correct_answer = self.quiz.check_answer(user_answer='True')
        self.give_feedback(correct_answer)
        
    def false_input(self):
        correct_answer = self.quiz.check_answer(user_answer='False')
        self.give_feedback(correct_answer)

    def give_feedback(self, correct_answer):
        if correct_answer:
            self.canvas.configure(bg='green')
        else:
            self.canvas.configure(bg='red')
        self.window.after(1000, self.get_next_question)

