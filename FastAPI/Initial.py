from fastapi import FastAPI

app = FastAPI()

@app.get("/welcome")

def Hello():
    message = "Hello developer"
    return {"Message" : message}