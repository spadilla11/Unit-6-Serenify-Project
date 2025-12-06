from decouple import config
import requests

QUIZAPI_TOKEN = config('QUIZAPI_TOKEN')

def fetch_quizapi_questions(subject, amount):
    url = f"https://quizapi.io/api/v1/questions?limit={amount}&category={subject}"
    headers = {
        "X-Api-Key": QUIZAPI_TOKEN
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    return data