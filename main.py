import os
from dotenv import load_dotenv
import openai
import requests
import json


load_dotenv()


openai.api_key = os.getenv('OPEN_AI_KEY')
# OPENAI_KEY = os.getenv('OPEN_AI_KEY')

# r = requests.get('https://api.openai.com/v1/engines', auth=f'Bearer {OPENAI_KEY}')
api_url = 'https://api.openai.com/v1/engines/davinci-codex/completions'

ENGINES_ENDPOINT = 'https://api.openai.com/v1/engines'
MODELS_ENDPOINT = 'https://api.openai.com/v1/models'

def get_models():
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {openai.api_key}'
    }
    response = requests.get(MODELS_ENDPOINT, headers=headers)
    return response.json()

def get_engines():
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {openai.api_key}'
    }
    response = requests.get(ENGINES_ENDPOINT, headers=headers)
    return response.json()


def generate_chat_response(prompt):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {openai.api_key}'
    }

    response = openai.Completion.create(model="text-davinci-003",
                                        prompt=prompt,
                                        max_tokens=50,  # = length of the answer
                                        temperature=1  
                                        )
    
    return response

    # data = {
    #     'prompt': prompt,
    #     'model': 'gpt-3.5-turbo',
    #     # 'content': 'Say this is a test!',
    #     'max_tokens': 100,
    #     'temperature': 0.7,
    #     'n': 1,
    #     'stop': None,
    # }
    
    # response = requests.post(api_url, headers=headers, data=json.dumps(data))
    # print(response.content)
    # response_json = response.json()
    # return response_json['choices'][0]['text'].strip()


if __name__ == '__main__':
    print('Enter a prompt:')
    prompt = input()
    print(f'the prompt is "{prompt}"')
    res = generate_chat_response(prompt)
    with open('gpt_responses.txt', 'w') as f:
        f.write(f'{res}')
    print(res)
    
    # print(get_models())
    # print(get_engines())