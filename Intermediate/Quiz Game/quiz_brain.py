class QuizBrain:
  def __init__(self, q_list):
    self.question_number = 0
    self.questions_list = q_list
    self.score = 0

  def next_question(self):
    q = self.questions_list[self.question_number]
    self.question_number += 1
    ans = input(f"Q.{self.question_number}: {q.text} (True/False)?: ")
    self.check_answer(q.answer, ans)
  
  def still_has_questions(self):
    return self.question_number < len(self.questions_list)

  def check_answer(self,correct_answer, user_answer):
    if correct_answer.lower() == user_answer.lower():
      print("You got it right!")
      self.score += 1
    else:
      print("That's wrong.")
    print(f"The correct answer was: {correct_answer}.")
    print(f"Your current score is: {self.score}/{self.question_number}")
    print("\n")

