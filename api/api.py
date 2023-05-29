from fastapi import FastAPI
import messages
import datetime

app = FastAPI()

date_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

@app.get("/")
async def root():
    return {'message': f'as of {date_time}, {messages.TABLEAU_TEST}'}