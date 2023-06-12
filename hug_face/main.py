import os
import requests
from dotenv import load_dotenv

load_dotenv()


FACE_TOKEN = os.getenv('FACE_TOKEN')
API_URL = 'https://api-inference.huggingface.co/models/google/tapas-large-finetuned-wtq'
headers = {'Authorization': f'Bearer {FACE_TOKEN}'}


def query(payload):
    payload['inputs']['query'] = input('what is your question? \n')
    print(f'\nthe query is <{payload["inputs"]["query"]}>')
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


data = {
    'inputs': {
        'query': ' ',
        'table': {
            'Product': ['Bush Somerset Collection Bookcase',
                        'Hon Deluxe Fabric Upholstered Stacking Chairs, Rounded Back',
                        'Self-Adhesive Address Labels for Typewriters by Universal'],
            'Sales': ['261.96', '731.94', '14.62'],
            'Quantity': ['2', '3', '2'],
            'Profit': [
                '41.9136',
                '219.582',
                '-383.031'
            ]
        }
    },
}


if __name__ == '__main__':

    print(query(data))
