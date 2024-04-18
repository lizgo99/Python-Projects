from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizzInterface:
    
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.score_label = Label(text=f"Score: {self.quiz.score}", fg= "white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        
        self.canvas = Canvas(width=300, height=250, bg="white", highlightbackground=THEME_COLOR)
        self.question_text = self.canvas.create_text(
            150, 
            125, 
            width=260, 
            text="Question Here", 
            font=("Ariel", 20, "italic"), 
            fill=THEME_COLOR
            )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=40)
        
        check_img = PhotoImage(file="Intermediate/Quizzler App/images/true.png")
        self.check_button = Button(image=check_img, command=self.true_pressed, highlightbackground=THEME_COLOR)
        self.check_button.grid(row=2, column=0)
        
        x_img = PhotoImage(file="Intermediate/Quizzler App/images/false.png")
        self.x_button = Button(image=x_img, command=self.false_pressed, highlightbackground=THEME_COLOR) 
        self.x_button.grid(row=2, column=1)
        
        self.get_next_question()
        
        self.window.mainloop()
        
    def get_next_question(self):
        if self.quiz.still_has_questions:
            self.canvas.config(bg="white")
            self.score_label.config(text= f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.check_button.config(state="disabled")
            self.x_button.config(state="disabled")
    
    def true_pressed(self):
        is_correct = self.quiz.check_answer("true")
        self.give_feedback(is_correct)
        
    def false_pressed(self):
        is_correct = self.quiz.check_answer("false")
        self.give_feedback(is_correct)
        
    def give_feedback(self, is_correct):
        
        if is_correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
            
        self.window.after(1000, self.get_next_question)
        