from D_17_data import question_data
from D_17_question_model import Question
from D_17_quiz_brain import QuizBrain

question_bank = [] 
# prepare list of questions from database 
for question in question_data: # for each Que in list of dicts
  new_q= Question(question["text"],question["answer"])
  #new_q class filled with text and answer from dict
  # "text" and "answer" are keys in dicts in list question_data
  # keys are used to access values in dicts,but keys dont come into work

  question_bank.append(new_q)

quiz=QuizBrain(question_bank,0)
print(len(question_bank))

while quiz.still_has_questions():
  quiz.next_question()
print(f"total score is {quiz.score} / {quiz.question_number}")