from fastapi import FastAPI

app = FastAPI(title="API Reza Ahmad Jahid")

@app.get("/")
def hello():
    return {"message": "Hello World dari Reza Ahmad Jahid!"}

@app.get("/nama")
def nama():
    return {"nama": "Reza Ahmad Jahid", "proyek": "fastapi-pertama"}
