from quiz.models import Question


def build_questions():
    # Create and return a list of questions
    questions = []

    questions.append(
        Question(
            "What does AI stand for?",
            ["Automated Interface", "Artificial Intelligence", "Advanced Internet", "Applied Integration"],
            1
        )
    )

    questions.append(
        Question(
            "Do AI systems think like humans?",
            ["Yes", "Only LLMs", "No, they copy patterns", "Only online"],
            2
        )
    )

    questions.append(
        Question(
            "Why does AI need data?",
            ["To learn patterns", "To run faster", "To encrypt files", "To avoid testing"],
            0
        )
    )

    questions.append(
        Question(
            "What does LLM stand for?",
            ["Large Learning Machine", "Logical Language Model", "Large Language Model", "Linear Learning Method"],
            2
        )
    )

    questions.append(
        Question(
            "Why can AI give wrong answers?",
            ["It gets tired", "Weak data or context", "It has emotions", "It refuses"],
            1
        )
    )

    questions.append(
        Question(
            "What is overfitting?",
            ["Good on training, bad on new data", "Model too small", "Encrypting data", "Removing testing"],
            0
        )
    )

    questions.append(
        Question(
            "What is model drift?",
            ["File moved", "Data changes over time", "Formatting change", "Slow tests"],
            1
        )
    )

    return questions


def grade(questions, answers):
    # Count correct answers
    score = 0

    for i in range(len(questions)):
        if questions[i].is_correct(answers[i]):
            score += 1

    return score