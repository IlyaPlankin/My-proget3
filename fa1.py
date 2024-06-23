from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def root():
    return {"message":"Hello World"}


@app.get("/privet/{username}")
def privet(username):
    return {"message":f"Приветх"}