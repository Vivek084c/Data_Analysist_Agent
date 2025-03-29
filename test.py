from fastapi import FastAPI

app = FastAPI()


@app.get("/vivek")
def hellow():
    return {"message": "Hello World"}