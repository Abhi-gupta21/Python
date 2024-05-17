import tkinter
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tkinter.Tk()
        self.window.config(padx = 20, pady = 20, bg = THEME_COLOR)
        self.window.title("Quizzler")

        self.score = tkinter.Label(text = "score: 0")
        self.score.config(bg = THEME_COLOR, foreground = "white")
        self.score.grid(row = 0, column = 1)

        self.canvas = tkinter.Canvas(width = 300, height = 250)
        self.question = self.canvas.create_text(150, 125, text = "Question goes here.", font = ("Arial", 20, "italic"), width = 280)
        self.canvas.grid(row = 1, column = 0, columnspan = 2, pady=50)


        self.true_img = tkinter.PhotoImage(file = "day 34/images/true.png")
        self.true_button = tkinter.Button(image = self.true_img, highlightthickness=0, command = self.true_pressed)
        self.true_button.config(padx = 20, pady = 20)
        self.true_button.grid(row = 2, column = 0)
        
        self.false_img = tkinter.PhotoImage(file = "day 34/images/false.png")
        self.false_button = tkinter.Button(image = self.false_img, highlightthickness=0, command = self.false_pressed)
        self.false_button.config(padx = 20, pady = 20)
        self.false_button.grid(row = 2, column = 1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text = text)
            self.score.config(text = f"Score: {self.quiz.score}")
            self.canvas.config(bg = "white")
        else:
            self.canvas.itemconfig(self.question, text = f"Quiz Over.\nFinal score = {self.quiz.score}/10")
            self.true_button.config(state = 'disabled')
            self.false_button.config(state = 'disabled')


    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
        

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
    

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg = "green")
        else:
            self.canvas.config(bg = "red")
        self.window.after(1000, self.get_next_question)
