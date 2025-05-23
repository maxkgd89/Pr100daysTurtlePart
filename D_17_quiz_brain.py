


class QuizBrain:
  def __init__(self,q_list,q_score):
    self.question_number = 0
    self.question_list = q_list
    self.score = q_score

  def next_question(self):
    current_question = self.question_list[self.question_number]
    self.question_number += 1
    user_answer = input(
        f"Q.{self.question_number}: {current_question.text} (True/False): " 
    )#in order to get "Q.1:" style notation
    self.check_answer(user_answer,current_question.answer)

  def still_has_questions(self):
    return self.question_number < len(self.question_list)  
 
  def check_answer(self,user_answer,correct_answer):
    if user_answer.lower() == correct_answer.lower():
      print("You got it right!")
      self.score += 1
      print(f"{self.score}/{self.question_number}")
    else:
      print("That's wrong.")
      print(f"The correct answer was: {correct_answer}.")
      print(self.score)