import os
from dotenv import load_dotenv, find_dotenv

load_dotenv()


print(os.getenv('OPEN_AI_KEY'))


if __name__ == '__main__':
    pass