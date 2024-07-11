from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def root():
    return {"message":"Hello World"}


@app.get("/privet/{username}")
def privet(username):
    return {"message":f"Привет {username}"}

@app.get("/valute/{val}")
def get_valute_rate(val):

    return {val:rate}



@app.get("/obmen/")
def obmen(val1, val2, count):
    return (val1, val2, count)
