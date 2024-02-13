from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


if __name__ == "__main__":

    quiz = QuizBrain([Question(q['text'], q['answer']) for q in question_data])
    while quiz.still_has_questions():
        quiz.next_question()
    print()
    print("You completed the quiz.")
    print(f"Your final score was {quiz.score} out of {quiz.question_count}")