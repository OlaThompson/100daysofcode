from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

questions = []
for question in question_data:
    question_questions = question["text"]
    question_answers = question["answer"]
    current_question = Question(question_questions, question_answers)
    questions.append(current_question)

quiz = QuizBrain(questions)

while quiz.still_questions():
    quiz.next_question()


