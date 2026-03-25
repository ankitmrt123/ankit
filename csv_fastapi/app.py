from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def home():
    return {"Message":"Welcome to FastAPI"}

# if "__name__"=="_main_":
