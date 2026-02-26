from quiz.logic import build_questions, grade


def test_all_correct():
    questions = build_questions()
    answers = []

    for q in questions:
        answers.append(q.correct_index)

    assert grade(questions, answers) == len(questions)