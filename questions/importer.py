from .quizapi_questions import fetch_quizapi_questions
from app.models import Question

def normalize_quizapi_question(raw):
    question_text = raw['question']
    category = raw['category']
    difficulty = raw['difficulty']
    
    answers = raw['answers']
    correct_flags = raw['correct_answers']
    
    correct_answer = None
    incorrect_answers = []
    
    for key, text in answers.items():
        if text is None:
            continue
        if correct_flags.get(f"{key}_correct") == 'true':
            correct_answer = text
        else:
            incorrect_answers.append(text)
    
    return {
        'subject': category,
        'question_text': question_text,
        'correct_answer': correct_answer,
        'incorrect_answers': incorrect_answers,
        'difficulty': difficulty,
        'api_source': 'quizapi'
    }
