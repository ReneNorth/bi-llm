import os
from dotenv import load_dotenv
import openai
import requests
import json
import pandas as pd


load_dotenv()


FACE_TOKEN = os.getenv('FACE_TOKEN')


import requests

API_URL = "https://api-inference.huggingface.co/models/google/tapas-large-finetuned-wtq"
headers = {"Authorization": f"Bearer {FACE_TOKEN}"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()



data = {
    "inputs": {
        "query": "what is the correlation between sales and profit",
        "table": {
            "Product Name": ["Bush Somerset Collection Bookcase", "Hon Deluxe Fabric Upholstered Stacking Chairs, Rounded Back", "Self-Adhesive Address Labels for Typewriters by Universal"],
            "Sales": ["261.96", "731.94", "14.62"],
            "Quantity": ["2", "3", "2"],
            "Profit": [
                "41.9136",
                "219.582",
                "-383.031"
            ]
        }
    },
}


if __name__ == '__main__':
    
    print('run')
    print(query(data))